"""
Scientific visualization module adhering to academic standards,
colorblind-safe palettes, and dual vector (PDF) / raster (PNG) exports.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns


def set_academic_style():
    """Sets academic plotting style with explicit units and accessible color palettes."""
    plt.style.use("seaborn-v0_8-whitegrid")
    sns.set_palette("colorblind")
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 10,
            "axes.labelsize": 11,
            "figure.dpi": 300,
        }
    )


def save_figure(fig, filename_base: str):
    """Exports plot in both PNG (300 DPI for README) and vector PDF (for publication/LaTeX)."""
    os.makedirs("reports/figures", exist_ok=True)
    fig.savefig(
        f"reports/figures/{filename_base}.png", dpi=300, bbox_inches="tight"
    )
    fig.savefig(f"reports/figures/{filename_base}.pdf", bbox_inches="tight")
    plt.close(fig)
