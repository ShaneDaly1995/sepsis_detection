# Link to challenge: https://www.physionet.org/challenge/2019/


## Introduction
Sepsis is a life-threatening condition that occurs when the body's response to infection causes tissue damage, organ failure, or death (Singer et al., 2016). In the U.S., nearly 1.7 million people develop sepsis and 270,000 people die from sepsis each year; over one third of people who die in U.S. hospitals have sepsis (CDC). Internationally, an estimated 30 million people develop sepsis and 6 million people die from sepsis each year; an estimated 4.2 million newborns and children are affected (WHO). Sepsis costs U.S. hospitals more than any other health condition at $24 billion (13% of U.S. healthcare expenses) a year, and a majority of these costs are for sepsis patients that were not diagnosed at admission (Paoli et al., 2018). Sepsis costs are even greater globally with the developing world at most risk. Altogether, sepsis is a major public health issue responsible for significant morbidity, mortality, and healthcare expenses.
Early detection and antibiotic treatment of sepsis are critical for improving sepsis outcomes, where each hour of delayed treatment has been associated with roughly an 4-8% increase in mortality (Kumar et al., 2006; Seymour et al., 2017). To help address this problem, clinicians have proposed new definitions for sepsis (Singer et al., 2016), but the fundamental need to detect and treat sepsis early still remains, and basic questions about the limits of early detection remain unanswered. The PhysioNet/Computing in Cardiology Challenge 2019 provides an opportunity to address these questions.

## Challenge Data
Data used in the competition is sourced from ICU patients in three separate hospital systems. Data from two hospital systems will be publicly available; however, one data set will be censored and used for scoring. The data for each patient will be contained within a single pipe-delimited text file. Each file will have the same header and each row will represent a single hour's worth of data. Available patient co-variates consist of Demographics, Vital Signs, and Laboratory values, which are defined in the tables below.
The following time points are defined for each patient:
tsuspicion
1. Clinical suspicion of infection identified as the earlier timestamp of IV antibiotics and blood cultures within a specified duration.
2. If antibiotics were given first, then the cultures must have been obtained within 24 hours. If cultures were obtained first, then antibiotic must have been subsequently ordered within 72 hours.
3. Antibiotics must have been administered for at least 72 consecutive hours to be considered.
tSOFA
The occurrence of end organ damage as identified by a two-point deterioration in SOFA score within a 24-hour period.
tsepsis
The onset time of sepsis is the earlier of tsuspicion and tSOFA as long as tSOFA occurs no more than 24 hours before or 12 hours after tsuspicion; otherwise, the patient is not marked as a sepsis patient. Specifically, if tsuspicion−24≤tSOFA≤tsuspicion+12, then tsepsis=min(tsuspicion,tSOFA).

## Vital signs (columns 1-8)
HR	Heart rate (beats per minute). 
O2Sat	Pulse oximetry (%). 
Temp	Temperature (Deg C). 
SBP	Systolic BP (mm Hg). 
MAP	Mean arterial pressure (mm Hg). 
DBP	Diastolic BP (mm Hg). 
Resp	Respiration rate (breaths per minute). 
EtCO2	End tidal carbon dioxide (mm Hg). 
Laboratory values (columns 9-34). 
BaseExcess	Measure of excess bicarbonate (mmol/L). 
HCO3	Bicarbonate (mmol/L). 
FiO2	Fraction of inspired oxygen (%). 
pH	N/A. 
PaCO2	Partial pressure of carbon dioxide from arterial blood (mm Hg). 
SaO2	Oxygen saturation from arterial blood (%). 
AST	Aspartate transaminase (IU/L). 
BUN	Blood urea nitrogen (mg/dL). 
Alkalinephos	Alkaline phosphatase (IU/L). 
Calcium	(mg/dL). 
Chloride	(mmol/L). 
Creatinine	(mg/dL). 
Bilirubin_direct	Bilirubin direct (mg/dL). 
Glucose	Serum glucose (mg/dL). 
Lactate	Lactic acid (mg/dL). 
Magnesium	(mmol/dL). 
Phosphate	(mg/dL). 
Potassium	(mmol/L). 
Bilirubin_total	Total bilirubin (mg/dL). 
TroponinI	Troponin I (ng/mL). 
Hct	Hematocrit (%). 
Hgb	Hemoglobin (g/dL). 
PTT	partial thromboplastin time (seconds). 
WBC	Leukocyte count (count/L). 
Fibrinogen	(mg/dL). 
Platelets	(count/mL). 
Demographics (columns 35-40)  
Age	Years. 
Gender	Female (0) or Male (1). 
Unit1	Administrative identifier for ICU unit (MICU). 
Unit2	Administrative identifier for ICU unit (SICU). 
HospAdmTime	Hours between hospital admit and ICU admit. 
ICULOS	ICU length-of-stay (hours since ICU admit). 
Outcome (column 41). 

SepsisLabel	For sepsis patients, SepsisLabel is 1 if t ≥ tsepsis−6 and 0 if t < tsepsis−6. For non-sepsis patients, SepsisLabel is 0.


## Objective of the Challenge
The goal of this Challenge is the early detection of sepsis using physiological data. For the purpose of the Challenge, we define sepsis according to the Sepsis-3 guidelines, i.e., a two-point change in the patient's Sequential Organ Failure Assessment (SOFA) score and clinical suspicion of infection (as defined by the ordering of blood cultures or IV antibiotics) (Singer et al., 2016).
The early prediction of sepsis is potentially life-saving, and we challenge participants to predict sepsis 6 hours before the clinical prediction of sepsis. Conversely, the late prediction of sepsis is potentially life-threatening, and predicting sepsis in non-sepsis patients (or predicting sepsis very early in sepsis patients) consumes limited hospital resources. For the challenge, we designed a utility function that rewards early predictions and penalizes late predictions as well as false alarms.
We ask participants to design and implement a working, open-source algorithm that can, based only on the clinical data provided, automatically identify a patient's risk of sepsis and make a positive or negative prediction of sepsis for every time interval. The winners of the Challenge will be the team whose algorithm gives predictions with the highest utility score for the patients in the hidden test set.

## Accessing the Data
Click here to download the complete training database (~ 6 MB) of 5,000 subjects.
The Challenge data repository contains one file per subject (e.g., training/p00101.psv for the training data).
Each training data file provides a table with measurements over time. Each column of the table provides a sequence of measurements over time (e.g., heart rate over several hours), where the header of the column describes the measurement. Each row of the table provides a collection of measurements at the same time (e.g., heart rate and oxygen level at the same time). The table is formatted in the following way:
HR |O2Sat|Temp|...|HospAdmTime|ICULOS|SepsisLabel
NaN|  NaN| NaN|...|        -50|     1|          0
 86|   98| NaN|...|        -50|     2|          0
 75|  NaN| NaN|...|        -50|     3|          1
 99|  100|35.5|...|        -50|     4|          1
There are 40 time-dependent variables HR, O2Sat, Temp ..., HospAdmTime, which are described here. The final column, SepsisLabel, indicates the onset of sepsis according to the Sepsis-3 definition, where 1 indicates sepsis and 0 indicates no sepsis. Entries of NaN (not a number) indicate that there was no recorded measurement of a variable at the time interval.
Note: spaces were added to this example to improve readability. They will not be present in the data files.

## Submitting Your Entry
All participants must submit working, open-source code. The details of the submission process are coming soon.
The test data is currently sequestered, and the submission process is not yet open. We will provide updates to this page when the submission process is open to participants.
Your entry must be in the form of a working program that takes a single pipe-delimited text file (.psv) as input and produces a text file as output. The input file will contain 40 columns (the same variables as are provided in the training data, except that the final column, SepsisLabel, will not be included. Your output should describe the probability of sepsis at each time interval as well as a positive or negative prediction at each time interval and be formatted in the following way with one prediction (output row) for each time interval (input row):

PredictedProbability|PredictedLabel
                 0.1|             0
                 0.3|             0
                 0.6|             1
                 0.8|             1

In this example, we chose probabilities above 0.5 to indicate positive predictions and probabilities below 0.5 to indicate negative predictions, but you can use any threshold.
Note: spaces were added to this example to improve readability. They will not be present in the data files.

## Scoring
Your final algorithm will be graded for its binary classification performance using a utility function that we created for the Challenge. This utility function rewards classifiers for early predictions of sepsis and penalizes them for late/missed predictions and for predictions of sepsis in non-sepsis patients.
We first define a score U(s,t) for each prediction, i.e., for each patient s and each time interval t (each line in the data file):
U(s,t)=⎧⎩⎨⎪⎪UTP(s,t),UFN(s,t),UFP(s,t),UTN(s,t),positive prediction at time t for sepsis patient snegative prediction at time t for sepsis patient spositive prediction at time t for non-sepsis patient snegative prediction at time t for non-sepsis patient s
The following figure illustrates the utility function for a sepsis patient (upper plot) with tsepsis = 48 as an example and a non-sepsis patient (lower plot):
 
This utility function rewards or penalizes classifiers using their predictions on each patient:
For patients that eventually have sepsis (i.e., with at least one SepsisLabel entry of 1), we reward classifiers that predict sepsis between 12 hours before and 3 hours after tsepsis, where the maximum reward is a parameter (1.0). We penalize classifiers that do not predict sepsis or predict sepsis more than 12 hours before tsepsis, where the maximum penalty for very early detection is a parameter (0.05) and the maximum penalty for late detection is also a parameter (-2.0).
For patients that do not eventually have sepsis (i.e., all SepsisLabel entries of 0), we penalize classifiers that predict sepsis, where the maximum penalty for false alarms is a parameter (0.05; equal to the very early detection penalty). We neither reward nor penalize those that do not predict sepsis.
We then compute a score for a classifier by summing U(s,t) over each prediction, i.e., over each patient s and each time interval t (each line in the data file):
Utotal=∑s∈S∑t∈T(s)U(s,t)
To improve interpretability, we normalized the above classifier score so that the optimal classifier (highest possible score) receives a normalized score of 1 and that a completely inactive classifier (no positive predictions) receives a normalized score of 0:
Unormalized=Utotal−Uno predictionsUoptimal−Uno predictions
Each classifier receives a Unormalized score, and the classifier with the highest Unormalized score wins.
A Python implementation of the scoring metric is available here, and a Matlab/Octave implementation is here.

## Sample Submission
A simple example algorithm is provided and may be used as a template for your own submission. Two implementations are provided:
Python (2.7 or 3.x), using numpy
Matlab or GNU Octave

## Rules and Deadlines
Entrants may have an overall total of up to three submitted entries over both the unofficial and official phases of the competition (see Table 2).
All deadlines occur at noon GMT (UTC) on the dates mentioned below. If you do not know the difference between GMT and your local time, find out what it is before the deadline!
Table 2: Challenge deadlines.
Start	Entry limit	End
Unofficial Phase	6 February	5	7 April
[Hiatus]	8 April	0	15 April
Official Phase	16 April	10	25 August
All official entries must be received no later than noon GMT on 25 August. In the interest of fairness to all participants, late entries will not be accepted or scored. Entries that cannot be scored (because of missing components, improper formatting, or excessive run time) are not counted against the entry limits.
To be eligible for the open-source award, you must do all of the following:
Submit at least one open-source entry that can be scored before the Phase I deadline (noon GMT on 7 April).
Submit at least one entry during the second phase (between noon GMT on 16 April and noon GMT on 25 August). Only your final entry will count for ranking.
Entering an Abstract to CinC: Submit an acceptable abstract (about 300 words) on your work on the Challenge to Computing in Cardiology no later than 9 April. Include the overall score for your Phase I entry in your abstract. Please select “PhysioNet/CinC Challenge” as the topic of your abstract, so it can be identified easily by the abstract review committee. You will be notified if your abstract has been accepted by email from CinC during the first week in June.
Submit a full (4-page) paper on your work on the Challenge to CinC no later than the deadline of conference paper submission.
Attend CinC 2019 (8-11 September 2019) in Singapore and present your work there.
Please do not submit analysis of this year’s Challenge data to other Conferences or Journals until after CinC 2019 has taken place, so the competitors are able to discuss the results in a single forum. We expect a special issue from a journal to follow the conference and encourage all entrants (and those who missed the opportunity to compete or attend CinC 2019) to submit extended analysis and articles to that issue, taking into account the publications and discussions at CinC 2019.
