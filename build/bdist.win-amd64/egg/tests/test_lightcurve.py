# -*- coding: utf-8 -*-
import lightkurve as lk
from chronos import ShortCadence, LongCadence

TICID = 460205581
SECTOR = 10
CUTOUT_SIZE = (15, 15)
QUALITY_BITMASK = "default"


def test_sc_pipeline():
    """
    """
    sc = ShortCadence(
        ticid=TICID, sap_mask="pipeline", quality_bitmask=QUALITY_BITMASK
    )
    _ = sc.get_lc()
    assert isinstance(sc.lc_pdcsap, lk.LightCurve)
    assert isinstance(sc.lc_sap, lk.LightCurve)


def test_sc_square():
    """
    """
    sc = ShortCadence(
        ticid=TICID,
        sap_mask="square",
        aper_radius=1,
        threshold_sigma=5,
        percentile=95,
        quality_bitmask=QUALITY_BITMASK,
    )
    _ = sc.make_custom_lc()
    assert isinstance(sc.lc_custom, lk.LightCurve)
    # assert sc.sap_mask == "square"


def test_sc_round():
    """
    """
    sc = ShortCadence(
        ticid=TICID,
        sap_mask="round",
        aper_radius=1,
        quality_bitmask=QUALITY_BITMASK,
    )
    _ = sc.make_custom_lc()
    assert isinstance(sc.lc_custom, lk.LightCurve)
    # assert sc.sap_mask == "round"


def test_sc_threshold():
    """
    """
    sc = ShortCadence(
        ticid=TICID,
        sap_mask="threshold",
        threshold_sigma=5,
        quality_bitmask=QUALITY_BITMASK,
    )
    _ = sc.make_custom_lc()
    assert isinstance(sc.lc_custom, lk.LightCurve)
    # assert sc.sap_mask == "threshold"


def test_sc_percentile():
    """
    """
    sc = ShortCadence(
        ticid=TICID,
        sap_mask="percentile",
        percentile=90,
        quality_bitmask=QUALITY_BITMASK,
    )
    _ = sc.make_custom_lc()
    assert isinstance(sc.lc_custom, lk.LightCurve)
    # assert sc.sap_mask == "percentile"


def test_sc_triceratops():
    """
    """
    sc = ShortCadence(ticid=TICID, calc_fpp=True)
    # df = sc.get_NEB_depths()
    # df = sc.get_fpp(flat=flat, plot=False)
    assert sc.triceratops is not None


def test_lc():
    """
    """
    lc = LongCadence(
        ticid=TICID,
        sap_mask="square",
        aper_radius=1,
        cutout_size=CUTOUT_SIZE,
        quality_bitmask=QUALITY_BITMASK,
    )
    _ = lc.make_custom_lc()
    assert isinstance(lc.lc_custom, lk.LightCurve)


def test_lc_triceratops():
    """
    """
    lc = LongCadence(ticid=TICID, calc_fpp=True)
    # df = sc.get_NEB_depths()
    # df = sc.get_fpp(flat=flat, plot=False)
    assert lc.triceratops is not None
