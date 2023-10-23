from sklearn import datasets

from evidently.test_suite import TestSuite
from evidently.test_preset import DataStabilityTestPreset

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

data = datasets.load_iris(as_frame=True).frame

data_stability= TestSuite(tests=[
    DataStabilityTestPreset(),
])
data_stability.run(current_data=data.iloc[:60], reference_data=data.iloc[60:], column_mapping=None)
data_stability.save_html('tests.html')

data_drift_report = Report(metrics=[
    DataDriftPreset(),
])
data_drift_report.run(current_data=data.iloc[:60], reference_data=data.iloc[60:], column_mapping=None)
data_drift_report.save_html('report.html')
