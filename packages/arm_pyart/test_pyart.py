from pytest_pyodide import run_in_pyodide


@run_in_pyodide(packages=["arm_pyart"])
def test_pyart(selenium):
    import pyart

    radar = pyart.testing.make_empty_ppi_radar(100, 100, 1)
    assert radar.range["data"][0] == 0.0