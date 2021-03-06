# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from chronos.star import Star


def test_star_attributes():
    # check inherited attributes
    s = Star(toiid=200)
    assert s.ticid is not None
    assert s.toiid is not None
    assert s.target_coord is not None
    gaia_params = s.query_gaia_dr2_catalog(return_nearest_xmatch=True)
    assert isinstance(gaia_params, pd.Series)
    tic_params = s.query_tic_catalog(return_nearest_xmatch=True)
    assert isinstance(tic_params, pd.Series)


def test_star_Av():
    s = Star(toiid=200)
    Av = s.estimate_Av(map="sfd")
    assert Av is not None


def test_star_spec_type():
    s = Star(toiid=200)
    # spec typing
    spec_types, samples = s.get_spectral_type(return_samples=True)
    assert (spec_types is not None) & (samples is not None)


def test_star_age():
    s = Star(toiid=200)
    # age
    # FIXME: add get_age_from_rotation_amplitude
    # FIXME: add get_age_from_isochrones
    mid, errp, errm, age_samples = s.get_age_from_rotation_period(
        prot=(5, 0.1), return_samples=True
    )
    assert np.all([mid, errp, errm])
    assert len(age_samples) > 10


def test_star_iso():
    s = Star(toiid=200)
    # iso
    iso_params1 = s.get_iso_params(bands="G BP RP".split())
    assert isinstance(iso_params1, dict)

    iso_params2 = s.get_iso_params(bands="G BP RP J H K".split())
    assert len(iso_params1) + 3 == len(iso_params2)
