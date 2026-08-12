import importlib
import sys
from typing import Any


def check_dependencies() -> None:
    installed = True
    packages = ["pandas", "numpy", "matplotlib"]
    msgs = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for package in packages:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            msg = msgs.get(package, "ready")
            print(f"[OK] {package} ({version}) - {msg}")
        except ImportError:
            print(f"[MISSING] {package} - not installed")
            installed = False

    if not installed:
        print("\nInstall with pip:")
        print("pip install -r requirements.txt")
        print("\nInstall with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        sys.exit(1)
    return


def show_compararison() -> None:
    print("\nDependency management comparison:")
    print("pip:    versions pinned/loose in requirements.txt, "
          "resolved at install time")
    print("poetry: versions locked in poetry.lock, "
          "reproducible across machines")


def generate_audio_stream() -> Any:
    import numpy
    import pandas
    samples = numpy.random.randn(1000, 2) * 0.3
    df = pandas.DataFrame(samples, columns=["channel_L", "channel_R"])
    return df


def generate_visual_data(df: Any) -> None:
    import matplotlib.pyplot as pyplot
    pyplot.figure(figsize=(10, 4))
    pyplot.plot(df["channel_L"], color="green", linewidth=0.7)
    pyplot.title("Matrix Audio Stream — Waveform")
    pyplot.xlabel("Sample")
    pyplot.ylabel("Amplitude")
    pyplot.ylim(-1, 1)
    pyplot.savefig("matrix_analysis.png")
    pyplot.close()


if __name__ == "__main__":
    check_dependencies()
    show_compararison()

    print("\nAnalyzing Matrix data...")
    df = generate_audio_stream()

    print("Generating visualization...")
    print("Processing 1000 data points...")
    generate_visual_data(df)

    print("\nAnalysis complete!")
    print("Results saved to:", "matrix_analysis.png")
