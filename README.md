# Liver-Cirrhosis-Stage-Prediction

<p>Liver cirrhosis is a widespread problem especially in North America due to high intake of alcohol. In this project, we will predict liver cirrhosis in a patient based on certain lifestyle and health conditions of a patient.</p>

![Liver Cirrhosis Prediction](https://guires.uk/newsroom/wp-content/uploads/2019/11/Predicting-Liver-Disease.jpg)
![Liver Cirrhosis Stages](https://img.freepik.com/free-vector/informative-illustration-stages-liver-disease-leading-cirrhosis_1308-50030.jpg?w=2000)
![Liver Cirrhosis](https://image.cnbcfm.com/api/v1/image/105649172-1545937328446gettyimages-911340738.jpeg?v=1545937849&w=1600&h=900)

## Objective

<p>In liver cirrhosis, there are mainly 4 stages which are as follows:</p>

<ol type="a">
  <li>Stage 1 : Normal</li>
  <li>Stage 2 : Fatty Liver</li>
  <li>Stage 3 : Liver Fibrosis</li>
  <li>Stage 4 : Liver Cirrhosis</li>
</ol>

<p>The primary target is to predict the stage of the liver cirrhosis disease. The dataset consists of both numerical as well as categorical features.</p>

## Deployed Web Application

Link: https://cirrhosis-stage-prediction.herokuapp.com/

## Context

<p>Cirrhosis is a late stage of scarring (fibrosis) of the liver caused by many forms of liver diseases and conditions, such as hepatitis and chronic alcoholism. The following data contains the information collected from the Mayo Clinic trial in primary biliary cirrhosis (PBC) of the liver conducted between 1974 and 1984. A description of the clinical background for the trial and the covariates recorded here is in Chapter 0, especially Section 0.2 of Fleming and Harrington, Counting
Processes and Survival Analysis, Wiley, 1991. A more extended discussion can be found in Dickson, et al., Hepatology 10:1-7 (1989) and in Markus, et al., N Eng J of Med 320:1709-13 (1989).</p>

<p>A total of 424 PBC patients, referred to Mayo Clinic during that ten-year interval, met eligibility criteria for the randomized placebo-controlled trial of the drug D-penicillamine. The first 312 cases in the dataset participated in the randomized trial and contain largely complete data. The additional 112 cases did not participate in the clinical trial but consented to have basic measurements recorded and to be followed for survival. Six of those cases were lost to follow-up shortly after diagnosis, so the data here are on an additional 106 cases as well as the 312 randomized participants.</p>

## Content

<table>
  <tr>
    <th><b>Feature</b></th>
    <th><b>Description</b></th>
  </tr>
  <tr>
    <td>ID</td>
    <td>Unique Identifier</td>
  </tr>
  <tr>
    <td>N_Days</td>
    <td>Number of days between registration and the earlier of death, transplantation, or study analysis time in July 1986</td>
  </tr>
  <tr>
    <td>Status</td>
    <td>Status of the patient: C (censored), CL (censored due to liver tx), or D (death)</td>
  </tr>
  <tr>
    <td>Drug</td>
    <td>Type of drug: D-penicillamine or Placebo</td>
  </tr>
  <tr>
    <td>Age</td>
    <td>Age (in days)</td>
  </tr>
  <tr>
    <td>Sex</td>
    <td>M (Male) or F (Female)</td>
  </tr>
  <tr>
    <td>Ascites</td>
    <td>Presence of Ascites: N (No) or Y (Yes)</td>
  </tr>
  <tr>
    <td>Hepatomegaly</td>
    <td>Presence of Hepatomegaly: N (No) or Y (Yes)</td>
  </tr>
  <tr>
    <td>Spiders</td>
    <td>Presence of Spiders: N (No) or Y (Yes)</td>
  </tr>
  <tr>
    <td>Edema</td>
    <td>Presence of Edema: N (no edema and no diuretic therapy for edema), S (edema present without diuretics, or edema resolved by diuretics), or Y (edema despite diuretic therapy)</td>
  </tr>
  <tr>
    <td>Bilirubin</td>
    <td>Serum Bilirubin (in mg/dl)</td>
  </tr>
  <tr>
    <td>Cholesterol</td>
    <td>Serum Cholesterol (in mg/dl)</td>
  </tr>
  <tr>
    <td>Albumin</td>
    <td>Albumin (in gm/dl)</td>
  </tr>
  <tr>
    <td>Copper</td>
    <td>Urine Copper (in ug/day)</td>
  </tr>
  <tr>
    <td>Alk_Phos</td>
    <td>Alkaline Phosphatase (in U/liter)</td>
  </tr>
  <tr>
    <td>SGOT</td>
    <td>SGOT (in U/ml)</td>
  </tr>
  <tr>
    <td>Triglycerides</td>
    <td>Triglicerides (in mg/dl)</td>
  </tr>
  <tr>
    <td>Platelets</td>
    <td>Platelets per cubic (ml/1000)</td>
  </tr>
  <tr>
    <td>Prothrombin</td>
    <td>Prothrombin time in seconds (s)</td>
  </tr>
  <tr>
    <td>Stage</td>
    <td>Histologic Stage of Disease (1, 2, 3 or 4)</td>
  </tr>
</table>

## Acknowledgements

<p>The dataset can be found in appendix D of:</p>

    Fleming, T.R. and Harrington, D.P. (1991) Counting Processes and Survival Analysis. Wiley Series in Probability and Mathematical Statistics: Applied Probability and Statistics, John Wiley and Sons Inc., New York.
