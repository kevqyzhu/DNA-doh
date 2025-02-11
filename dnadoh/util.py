"""Utilities."""

from typing import List, Optional

from pydantic import BaseModel

import plotly.io as pio

# Number of digits to use in person filenames.
WIDTH = 6


class Person(BaseModel):
    """An individual person.

    Values marked `Optional` are filled in one at a time.
    """

    # Person ID.
    pid: int

    # Genome.
    genome: str

    # Age in years.
    age: Optional[int] = None

    # Genetic sex {"F", "M", "O"}.
    gsex: Optional[str] = None

    # Weight in kg.
    weight: Optional[float] = None


def filename_overall(stem):
    """Where to store overall summary."""
    return f"{stem}-overall.csv"


def filename_parameter(stem):
    """Where to store parameters."""
    return f"{stem}-parameters.json"


def filename_person(stem, pid):
    """Where to store information about a single person."""
    pid_str = str(pid).zfill(WIDTH)
    return f"{stem}-pid{pid_str}.csv"


def filename_phenotypes(stem):
    """Where to store phenotypic data for all people."""
    return f"{stem}-phenotypes.csv"


def filename_reference_genome(stem):
    """Where to store reference genome."""
    return f"{stem}-reference.json"


def filename_assembled_data(stem):
    """Where to store phenotypic data joined to variant data for all individuals."""
    return f"{stem}-assembled.csv"


def pid_width(length):
    """Number of digits in personal information files' names."""
    return max(2, len(str(length)))

def plotly_to_html(fig, static=False):
    if static:
        img = fig.to_image(
            format="png",
            width=750,
            height=450,
        )
        b64 = base64.b64encode(img).decode()
        html = '<p><img src="data:image/png;base64,{}"></p>'.format(b64)
        return html
    else:
        return pio.to_html(
            fig,
            full_html=False,
            include_plotlyjs="cdn",
            include_mathjax="cdn",
            config={
                "showLink": True,
                "toImageButtonOptions": {
                    "format": "svg",
                    "width": 750,
                    "height": 600,
                },
            },
        )