import streamlit as st
import altair as alt

from utils.experiment import Experiment
from etf.models.naive_average import NaiveSeasonalAverage
from darts.models.forecasting.exponential_smoothing import ExponentialSmoothing
from testdata.utils.provider import DataProvider
from darts import TimeSeries
import pandas as pd


alt.themes.enable("streamlit")

st.write("test")