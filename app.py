{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ea7cc0a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (1.1.5)\n",
      "Requirement already satisfied: openpyxl in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (3.1.3)\n",
      "Requirement already satisfied: numpy>=1.15.4 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from pandas) (1.19.5)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2017.2 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: et-xmlfile in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from openpyxl) (1.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from python-dateutil>=2.7.3->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas openpyxl\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt \n",
    "import seaborn as sns\n",
    "sns.set_style('darkgrid')\n",
    "import statsmodels.api as sm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a3a65db7",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_excel(\"ESD.xlsx\", engine='openpyxl')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "47ce5119",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>EEID</th>\n",
       "      <th>Full Name</th>\n",
       "      <th>Job Title</th>\n",
       "      <th>Department</th>\n",
       "      <th>Business Unit</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Ethnicity</th>\n",
       "      <th>Age</th>\n",
       "      <th>Hire Date</th>\n",
       "      <th>Annual Salary</th>\n",
       "      <th>Bonus %</th>\n",
       "      <th>Country</th>\n",
       "      <th>City</th>\n",
       "      <th>Exit Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>E02387</td>\n",
       "      <td>Emily Davis</td>\n",
       "      <td>Sr. Manger</td>\n",
       "      <td>IT</td>\n",
       "      <td>Research &amp; Development</td>\n",
       "      <td>Female</td>\n",
       "      <td>Black</td>\n",
       "      <td>55</td>\n",
       "      <td>2016-04-08</td>\n",
       "      <td>141604</td>\n",
       "      <td>0.15</td>\n",
       "      <td>United States</td>\n",
       "      <td>Seattle</td>\n",
       "      <td>2021-10-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>E04105</td>\n",
       "      <td>Theodore Dinh</td>\n",
       "      <td>Technical Architect</td>\n",
       "      <td>IT</td>\n",
       "      <td>Manufacturing</td>\n",
       "      <td>Male</td>\n",
       "      <td>Asian</td>\n",
       "      <td>59</td>\n",
       "      <td>1997-11-29</td>\n",
       "      <td>99975</td>\n",
       "      <td>0.00</td>\n",
       "      <td>China</td>\n",
       "      <td>Chongqing</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>E02572</td>\n",
       "      <td>Luna Sanders</td>\n",
       "      <td>Director</td>\n",
       "      <td>Finance</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Female</td>\n",
       "      <td>Caucasian</td>\n",
       "      <td>50</td>\n",
       "      <td>2006-10-26</td>\n",
       "      <td>163099</td>\n",
       "      <td>0.20</td>\n",
       "      <td>United States</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>E02832</td>\n",
       "      <td>Penelope Jordan</td>\n",
       "      <td>Computer Systems Manager</td>\n",
       "      <td>IT</td>\n",
       "      <td>Manufacturing</td>\n",
       "      <td>Female</td>\n",
       "      <td>Caucasian</td>\n",
       "      <td>26</td>\n",
       "      <td>2019-09-27</td>\n",
       "      <td>84913</td>\n",
       "      <td>0.07</td>\n",
       "      <td>United States</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>E01639</td>\n",
       "      <td>Austin Vo</td>\n",
       "      <td>Sr. Analyst</td>\n",
       "      <td>Finance</td>\n",
       "      <td>Manufacturing</td>\n",
       "      <td>Male</td>\n",
       "      <td>Asian</td>\n",
       "      <td>55</td>\n",
       "      <td>1995-11-20</td>\n",
       "      <td>95409</td>\n",
       "      <td>0.00</td>\n",
       "      <td>United States</td>\n",
       "      <td>Phoenix</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>E03094</td>\n",
       "      <td>Wesley Young</td>\n",
       "      <td>Sr. Analyst</td>\n",
       "      <td>Marketing</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Male</td>\n",
       "      <td>Caucasian</td>\n",
       "      <td>33</td>\n",
       "      <td>2016-09-18</td>\n",
       "      <td>98427</td>\n",
       "      <td>0.00</td>\n",
       "      <td>United States</td>\n",
       "      <td>Columbus</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>E01909</td>\n",
       "      <td>Lillian Khan</td>\n",
       "      <td>Analyst</td>\n",
       "      <td>Finance</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Female</td>\n",
       "      <td>Asian</td>\n",
       "      <td>44</td>\n",
       "      <td>2010-05-31</td>\n",
       "      <td>47387</td>\n",
       "      <td>0.00</td>\n",
       "      <td>China</td>\n",
       "      <td>Chengdu</td>\n",
       "      <td>2018-01-08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>E04398</td>\n",
       "      <td>Oliver Yang</td>\n",
       "      <td>Director</td>\n",
       "      <td>Marketing</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Male</td>\n",
       "      <td>Asian</td>\n",
       "      <td>31</td>\n",
       "      <td>2019-06-10</td>\n",
       "      <td>176710</td>\n",
       "      <td>0.15</td>\n",
       "      <td>United States</td>\n",
       "      <td>Miami</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>E02521</td>\n",
       "      <td>Lily Nguyen</td>\n",
       "      <td>Sr. Analyst</td>\n",
       "      <td>Finance</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Female</td>\n",
       "      <td>Asian</td>\n",
       "      <td>33</td>\n",
       "      <td>2012-01-28</td>\n",
       "      <td>95960</td>\n",
       "      <td>0.00</td>\n",
       "      <td>China</td>\n",
       "      <td>Chengdu</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>E03545</td>\n",
       "      <td>Sofia Cheng</td>\n",
       "      <td>Vice President</td>\n",
       "      <td>Accounting</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Female</td>\n",
       "      <td>Asian</td>\n",
       "      <td>63</td>\n",
       "      <td>2020-07-26</td>\n",
       "      <td>216195</td>\n",
       "      <td>0.31</td>\n",
       "      <td>United States</td>\n",
       "      <td>Miami</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       EEID        Full Name                 Job Title  Department  \\\n",
       "0    E02387      Emily Davis                Sr. Manger          IT   \n",
       "1    E04105    Theodore Dinh       Technical Architect          IT   \n",
       "2    E02572     Luna Sanders                  Director     Finance   \n",
       "3    E02832  Penelope Jordan  Computer Systems Manager          IT   \n",
       "4    E01639        Austin Vo               Sr. Analyst     Finance   \n",
       "..      ...              ...                       ...         ...   \n",
       "995  E03094     Wesley Young               Sr. Analyst   Marketing   \n",
       "996  E01909     Lillian Khan                   Analyst     Finance   \n",
       "997  E04398      Oliver Yang                  Director   Marketing   \n",
       "998  E02521      Lily Nguyen               Sr. Analyst     Finance   \n",
       "999  E03545      Sofia Cheng            Vice President  Accounting   \n",
       "\n",
       "              Business Unit  Gender  Ethnicity  Age  Hire Date  Annual Salary  \\\n",
       "0    Research & Development  Female      Black   55 2016-04-08         141604   \n",
       "1             Manufacturing    Male      Asian   59 1997-11-29          99975   \n",
       "2       Speciality Products  Female  Caucasian   50 2006-10-26         163099   \n",
       "3             Manufacturing  Female  Caucasian   26 2019-09-27          84913   \n",
       "4             Manufacturing    Male      Asian   55 1995-11-20          95409   \n",
       "..                      ...     ...        ...  ...        ...            ...   \n",
       "995     Speciality Products    Male  Caucasian   33 2016-09-18          98427   \n",
       "996     Speciality Products  Female      Asian   44 2010-05-31          47387   \n",
       "997     Speciality Products    Male      Asian   31 2019-06-10         176710   \n",
       "998     Speciality Products  Female      Asian   33 2012-01-28          95960   \n",
       "999               Corporate  Female      Asian   63 2020-07-26         216195   \n",
       "\n",
       "     Bonus %        Country       City  Exit Date  \n",
       "0       0.15  United States    Seattle 2021-10-16  \n",
       "1       0.00          China  Chongqing        NaT  \n",
       "2       0.20  United States    Chicago        NaT  \n",
       "3       0.07  United States    Chicago        NaT  \n",
       "4       0.00  United States    Phoenix        NaT  \n",
       "..       ...            ...        ...        ...  \n",
       "995     0.00  United States   Columbus        NaT  \n",
       "996     0.00          China    Chengdu 2018-01-08  \n",
       "997     0.15  United States      Miami        NaT  \n",
       "998     0.00          China    Chengdu        NaT  \n",
       "999     0.31  United States      Miami        NaT  \n",
       "\n",
       "[1000 rows x 14 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "efea68bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.set_option('display.max_columns', None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b6e4ff32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Annual Salary</th>\n",
       "      <th>Bonus %</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1000.000000</td>\n",
       "      <td>1000.000000</td>\n",
       "      <td>1000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>44.382000</td>\n",
       "      <td>113217.365000</td>\n",
       "      <td>0.088660</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>11.246981</td>\n",
       "      <td>53545.985644</td>\n",
       "      <td>0.117856</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>25.000000</td>\n",
       "      <td>40063.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>35.000000</td>\n",
       "      <td>71430.250000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>45.000000</td>\n",
       "      <td>96557.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>54.000000</td>\n",
       "      <td>150782.250000</td>\n",
       "      <td>0.150000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>65.000000</td>\n",
       "      <td>258498.000000</td>\n",
       "      <td>0.400000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Age  Annual Salary      Bonus %\n",
       "count  1000.000000    1000.000000  1000.000000\n",
       "mean     44.382000  113217.365000     0.088660\n",
       "std      11.246981   53545.985644     0.117856\n",
       "min      25.000000   40063.000000     0.000000\n",
       "25%      35.000000   71430.250000     0.000000\n",
       "50%      45.000000   96557.000000     0.000000\n",
       "75%      54.000000  150782.250000     0.150000\n",
       "max      65.000000  258498.000000     0.400000"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "90802ccd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      141604\n",
       "1       99975\n",
       "2      163099\n",
       "3       84913\n",
       "4       95409\n",
       "        ...  \n",
       "995     98427\n",
       "996     47387\n",
       "997    176710\n",
       "998     95960\n",
       "999    216195\n",
       "Name: Annual Salary, Length: 1000, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Independent variable\n",
    "x = data['Age']\n",
    "x\n",
    "y = data['Annual Salary']\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3d32e711",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1000,)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.shape\n",
    "y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3d1e5c6b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(x,y)\n",
    "plt.xlabel('Age',fontsize=20)\n",
    "plt.ylabel('Annual Salary',fontsize=20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a458a44b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      55\n",
       "1      59\n",
       "2      50\n",
       "3      26\n",
       "4      55\n",
       "       ..\n",
       "995    33\n",
       "996    44\n",
       "997    31\n",
       "998    33\n",
       "999    63\n",
       "Name: Age, Length: 1000, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "91692931",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      141604\n",
       "1       99975\n",
       "2      163099\n",
       "3       84913\n",
       "4       95409\n",
       "        ...  \n",
       "995     98427\n",
       "996     47387\n",
       "997    176710\n",
       "998     95960\n",
       "999    216195\n",
       "Name: Annual Salary, Length: 1000, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2f900cc2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x256d37dc908>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result = sm.OLS(y,x).fit()\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c6799b11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"simpletable\">\n",
       "<caption>OLS Regression Results</caption>\n",
       "<tr>\n",
       "  <th>Dep. Variable:</th>      <td>Annual Salary</td>  <th>  R-squared (uncentered):</th>      <td>   0.764</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared (uncentered):</th> <td>   0.764</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>          <td>   3230.</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Date:</th>             <td>Tue, 08 Apr 2025</td> <th>  Prob (F-statistic):</th>          <td>2.79e-315</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Time:</th>                 <td>22:20:01</td>     <th>  Log-Likelihood:    </th>          <td> -12435.</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>No. Observations:</th>      <td>  1000</td>      <th>  AIC:               </th>          <td>2.487e+04</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Residuals:</th>          <td>   999</td>      <th>  BIC:               </th>          <td>2.488e+04</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>              <td> </td>    \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>              <td> </td>    \n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "   <td></td>      <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Age</th> <td> 2390.4416</td> <td>   42.062</td> <td>   56.832</td> <td> 0.000</td> <td> 2307.902</td> <td> 2472.981</td>\n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "  <th>Omnibus:</th>       <td>64.831</td> <th>  Durbin-Watson:     </th> <td>   2.021</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  76.713</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Skew:</th>          <td> 0.678</td> <th>  Prob(JB):          </th> <td>2.20e-17</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Kurtosis:</th>      <td> 3.026</td> <th>  Cond. No.          </th> <td>    1.00</td>\n",
       "</tr>\n",
       "</table><br/><br/>Notes:<br/>[1] R² is computed without centering (uncentered) since the model does not contain a constant.<br/>[2] Standard Errors assume that the covariance matrix of the errors is correctly specified."
      ],
      "text/plain": [
       "<class 'statsmodels.iolib.summary.Summary'>\n",
       "\"\"\"\n",
       "                                 OLS Regression Results                                \n",
       "=======================================================================================\n",
       "Dep. Variable:          Annual Salary   R-squared (uncentered):                   0.764\n",
       "Model:                            OLS   Adj. R-squared (uncentered):              0.764\n",
       "Method:                 Least Squares   F-statistic:                              3230.\n",
       "Date:                Tue, 08 Apr 2025   Prob (F-statistic):                   2.79e-315\n",
       "Time:                        22:20:01   Log-Likelihood:                         -12435.\n",
       "No. Observations:                1000   AIC:                                  2.487e+04\n",
       "Df Residuals:                     999   BIC:                                  2.488e+04\n",
       "Df Model:                           1                                                  \n",
       "Covariance Type:            nonrobust                                                  \n",
       "==============================================================================\n",
       "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
       "------------------------------------------------------------------------------\n",
       "Age         2390.4416     42.062     56.832      0.000    2307.902    2472.981\n",
       "==============================================================================\n",
       "Omnibus:                       64.831   Durbin-Watson:                   2.021\n",
       "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               76.713\n",
       "Skew:                           0.678   Prob(JB):                     2.20e-17\n",
       "Kurtosis:                       3.026   Cond. No.                         1.00\n",
       "==============================================================================\n",
       "\n",
       "Notes:\n",
       "[1] R² is computed without centering (uncentered) since the model does not contain a constant.\n",
       "[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
       "\"\"\""
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8b6fc5a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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paXh6aefxvvvv9/ot2vWrMEDDzyAQ4cOYfTo0Rg/fjx++uknPPHEE3j11VfFvZBEwkDGUpNITMLlcuFXv/oVKisrsX37dsTExKC+vh5ZWVm4ePEiioqK0KJFCwDApk2b8Pjjj2PYsGF48cUXPYEn33rrLSxevBgAUFhYiKuvvhpnzpzB8OHD0b59e7z11lu44oorAADV1dX4zW9+g127dmHdunXIyMgw58Ully1yhiORmMS2bdtw7tw5DB8+HDExMQAaEtONGjUKdXV1WLdunee3H3zwAQDgqaee8olynJubi/T0dJ/7rl+/HrW1tXj88cc9wgZoSEz2+OOPw+12e+4nkYQTmYBNIjEJVaD8+te/9jmek5ODt956C++99x4eeOABAA1ppZ1OJzp06ODzW7vdjuuuuw5Hjx71HNu7dy+AhjWc7777zuf3lZWVABrWjiSScCMFjkRiAuXl5SgoKAAA3c2eR44cwddff43rr78eFy5caDSTUbnqqqt8/lbTFLPSKJeWlgZTbImECylwJBIT+Pjjj1FdXY1rr70WPXr0aHT+6NGj2LlzJ9asWYPrr78ezZs3R3l5uea9/I/Hx8cDAAoKCtC+ffvQF14iCRIpcCQSE1DNabNnz9ZMK3z69GkMHToUH3/8MZ5++mn07NkTn332GX788cdGM5pdu3b5/N21a1cUFBRgz549jQTOsWPH8M4776B///4YMmRIiN9KImEjnQYkkjBz6tQpfPHFF2jXrh369u2r+ZuUlBTccMMNqKysxEcffYSxY8dCURT88Y9/hMvl8vxu3bp12LNnj8+1t912GxwOB1588UWcO3fOc7y+vh55eXn461//ipKSEiHvJpGwkDMciSTMrFu3DoqiICcnBzabTfd3Y8eOxWeffYY1a9ZgzZo1WLduHTZs2IAjR44gMzMTx48fx6effoorrrgCFy5cgMPhAACkpaXhySefxJIlS3DrrbdiyJAhSE5ORlFREb7//nvccsstuO2228L1uhKJB7kPRyIJMyNHjsSxY8ewceNGdOrUSfd31dXVGDRoEMrKyrB+/XqkpqbilVdewfr163Hu3DmkpqZi8uTJ+OSTT5Cfn4/PP//cxw363//+N/76179i7969cLvdaN++PcaMGYN77rkHzZo1C8erSiQ+SIEjkUQAxcXFSExMRPPmzRudu/fee7F371588803zBmTRGI2cg1HIokAXn/9dfTt2xc7d+70Of7NN9/gq6++woABA6SwkVgeOcORSCKAffv2Yfz48YiOjsaIESPQunVrnDx5EgUFBWjWrBneeecdpnlOIrECUuBIJBHC/v378dprr+Hbb7/FTz/9hBYtWuDGG2/E1KlTG0UgkEisiBQ4EolEIgkLcg1HIpFIJGFBChyJRCKRhAUpcCQSiUQSFqTAkUgkEklYkAJHIpFIJGHh/wPkY0OIwK3W5wAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(x,y)\n",
    "yhat = 1.182e+05 + (-111.8696) * x\n",
    "plt.plot(x,yhat,lw=3,c='purple')\n",
    "plt.xlabel('Age',fontsize=20)\n",
    "plt.ylabel('Annual Salary',fontsize=20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "fa11b3ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "import statsmodels.tsa.api as smt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "35f4854b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       10129.712053\n",
       "1      -41061.054343\n",
       "2       43576.920048\n",
       "3       22761.518425\n",
       "4      -36065.287947\n",
       "           ...      \n",
       "995     19542.427232\n",
       "996    -57792.430358\n",
       "997    102606.310430\n",
       "998     17075.427232\n",
       "999     65597.179260\n",
       "Length: 1000, dtype: float64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result.resid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b3308165",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages\\ipykernel_launcher.py:2: UserWarning: Matplotlib is currently using module://ipykernel.pylab.backend_inline, which is a non-GUI backend, so cannot show the figure.\n",
      "  \n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "acf = smt.graphics.plot_acf(result.resid)\n",
    "acf.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b2da2c5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages\\seaborn\\distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Density'>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(result.resid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "5d1b2058",
   "metadata": {},
   "outputs": [],
   "source": [
    "import statsmodels.api as sm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "418020ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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3ngDZrMZ+fn56NKlCwRBuGMzlh49euCHH37AQw89hD179uD69evYtWsXli9fjh49emD16tUt/rCIjIxE165d8d577yE1NRXLly+HyWTCgQMH8MILL+Dzzz9HeXk5AODEiRP1X7dw4ULs27ev/gav9YdBc/8P/Pz8WtxApnv37ujZsyc2btwIQRCwefNmxMbGorCwENOnT8ddd92FRYsWYd++ffX/j0hdGPjkNV577TVkZmbCaDRCEARkZ2ejW7duOHLkCJKTk2EwGDBy5Ej07du3ydcNHToUR44cwYQJE1BTU4PExESEhYXh17/+Nd566y306NGj/rVz5szBokWLUFBQgODgYCxbtgxGoxEzZsxA27ZtERUVhWvXrrVY49KlS7FixQqMGzcOfn5+CA4Oxt13341Tp04hISEB27ZtQ0pKCvr27Vvfu/2JJ55AamoqtFotOnTogLKyshbfPyYmBqdOncLmzZvv+FyfPn0waNAgpKSkoK6uDnFxcYiMjERcXBymTp2K0NBQhISE1G+oQerD5mlEbnbjxg1cuXIFvXr18nQppHIMfCIileDaLCIilWDgExGpBAOfiEglGPhERCrBwCciUgkGPhGRSvw/ByU6CbFma9UAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Q_Q_plot = sm.qqplot(result.resid,fit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "f8f718e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.9529560626110664, 0.7047840516182398)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sm.stats.diagnostic.linear_rainbow(res=result)   #2nd values is p value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "52141406",
   "metadata": {},
   "outputs": [],
   "source": [
    "import statsmodels.stats.api as sms"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "1ba75daf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.9842086960742523, 0.5705179412668011, 'increasing')"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sms.het_goldfeldquandt(result.resid,result.model.exog) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "fd3e3ee3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.9842086960742523, 0.5705179412668011, 'increasing')"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sms.het_goldfeldquandt(result.resid,result.model.exog) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "fef4a2ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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TOvWrfXJJ5+oa9euSktLU5MmTbznfr046syZM1WtWrUiExGJZAQAAFymmJgYpaamqlevXjIMQwkJCZo7d66ioqLUuXPny27PZpTiDngOZ+3SahplVPaJT80OAUEk//h+s0NAEAr7c9eAft/CWn1LvM2+JxaWeJtFoTICAICFeay/ACuzaQAAgLmojAAAYGFmrDNS0qiMAAAAU1EZAQDAwkptFkoAkYwAAGBhDGAFAADwE5URAAAsjAGsAAAAfqIyAgCAhVEZAQAA8BOVEQAALMwIgtk0JCMAAFgY3TQAAAB+ojICAICFURkBAADwE5URAAAsjL1pAACAqdibBgAAwE9URgAAsDAGsAIAAPiJyggAABYWDJURkhEAACwsGGbT0E0DAABMRWUEAAALY2ovAACAn6iMAABgYcEwgJXKCAAAMBWVEQAALCwYZtOUajISBGNqcIXJP77f7BAQROy1rzM7BMBvniBIR+imAQAApqKbBgAAC2MAKwAAgJ+ojAAAYGHWHzFCMgIAgKXRTQMAAOAnKiMAAFgYe9MAAAD4icoIAAAWFgyLnpGMAABgYdZPReimAQAAJqMyAgCAhTG1FwAAwE9URgAAsDAGsAIAAFNZPxWhmwYAAJiMyggAABbGAFYAAAA/URkBAMDCgmEAK5URAABgKiojAABYmPXrIiQjAABYGgNYAQAA/ERlBAAACzOCoKOGyggAADAVlREAACwsGMaMkIwAAGBhrDMCAADgJyojAABYmPXrIlRGAACAyaiMAABgYcEwZoRkBAAACwuG2TR00wAAAFNRGQEAwMJYgRUAAMBPVEYAALAwxowAAAD4icoIAAAWFgxjRkhGAACwMLppAAAA/ERlBAAAC/MY1u+moTICAABMRWUEAAALs35dhGQEAABLC4aN8uimAQAApqIyAgCAhQXDOiNURgAAgKmojAAAYGFmLHrm8Xg0fvx4HThwQE6nU5MmTVLdunW95+fNm6c1a9ZIkjp06KD4+Pgi26MyAgCAhXlklPjLlw0bNig3N1fJyckaPny4EhMTveeOHTumVatWacmSJfrggw+0detW7d+/v8j2qIwAAIDLsnPnTkVHR0uSWrZsqT179njP1axZU7Nnz5bdbpckud1ulStXrsj2SEYAALCw0hjAmpycrOTkZO9xbGysYmNjvccul0sRERHeY7vdLrfbLYfD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X75cOTk56t27t9q3by+n01loe3TTAACAy7Jz505FR0dLklq2bKk9e/Z4z+3evVutWrWS0+lUZGSkoqKitH///iLbozICAICFlUY3TXJyspKTk73HsbGxio2N9R67XC5FRER4j+12u9xutxwOh1wulyIjI73nKlSoIJfLVeT3kYwAAIACfpt8/FZERISysrK8xx6PRw6H45LnsrKyCiQnl0I3DQAAFmYYRom/fGndurVSUlIkSWlpaWrSpIn3XIsWLbRz507l5OQoMzNT6enpBc5fCpURAABwWWJiYpSamqpevXrJMAwlJCRo7ty5ioqKUufOnRUXF6fevXvLMAwNHTpU5cqVK7I9m1GKq6WEOmuXVtMoozJ3vGN2CAgi9trXmR0CglBotQYB/b5yYX8q8TZzfjxW4m0WhcoIAAAWxgqsAAAAfqIyAgCAhVEZAQAA8BOVEQAALMz6dZFSnk0DAADgC900AADAVCQjAADAVCQjAADAVCQjAADAVCQjAADAVCQjAADAVCQjAADAVCQjAfbOO+/o1ltvVU5OjtmhIIAC9Xv/4osvNHTo0N+9/+GHH+qRRx5RXFycevXqpa1btxbZTvv27UsrRATIF198oVtuuUVxcXHq27evHnroIX3zzTcB+/5Zs2YpNjZWb775piTJ7XbrmWeeUX5+fsBigHWQjATYqlWr1LVrV61Zs8bsUBBAZv7eMzMz9frrr2v27NlasGCBZsyYodGjR8vj8QQ8FgTWzTffrAULFmjhwoV65plnNGPGjIB997Zt25ScnKxPP/1UkpScnKwePXrIbrcHLAZYB8vBB9AXX3yhqKgo9erVSyNGjNADDzyg3bt3a8KECapQoYKuuuoqlStXTomJiVqwYIFWr14tm82mrl276pFHHjE7fPxBl/q9x8XF6brrrtOhQ4fkcrk0Y8YMGYah4cOHq2bNmjp27JiaN2+uCRMmaObMmapWrZoefvhhpaena/z48VqwYIHWrVunRYsWye12y2azadasWZf8fqfTqby8PL3//vvq2LGjoqKitGHDBoWEhOjgwYNKTExUfn6+zp07p/Hjx6t169bez27fvl2zZs2SYRjKysrS1KlTFRoaqkGDBqly5cq66aabtHLlSv3rX/+S3W5XUlKSmjVrpq5duwbqHy+K6cKFC6pataok6ZtvvtELL7wgu92ucuXK6YUXXpDH47ms52/atGn64osv5Ha71aVLF/3v//5vge9zOBzKz89XSEiIMjMz9eWXX6pPnz5m3DosgMpIAC1dulQPPvigGjRoIKfTqV27dmncuHFKTEzU/PnzFRUVJUn69ttvtXbtWi1evFiLFi3Shg0bdPjwYZOjxx91qd+7JLVo0ULz5s1T+/btvRWTI0eOaPLkyVq6dKlSUlJ0+vTpQts9cuSI3n77bb3//vtq1KhRoV0v5cqV03vvvaejR4+qf//+6tixo5YtWybpp2ft2Wef1XvvvacBAwZoxYoVBT576NAhJSUlacGCBerSpYvWrVsnSTp9+rTeffddxcfHq02bNtq6davy8/OVkpKiO+64w+9/ZigZn3/+ueLi4hQbG6tRo0apW7dukqQxY8Zo7NixWrhwoR5++GElJiZKurzn76OPPtLLL7+sxYsXq2LFir87HxcXp6FDh+qxxx7T22+/rX79+ikpKUkTJkzQmTNnSueGYVlURgLk/PnzSklJ0dmzZ7VgwQK5XC4tXLhQp06dUuPGjSVJbdq00dq1a3Xw4EGdOHFCjz32mPezR48eVYMGDUy8A/wRhf3eJen666+XJNWsWdP7L+eoqChFRERIkq6++uoix5hcddVVevbZZ1WhQgUdPnxYLVu2vOR1J0+e1I8//qixY8dKkv7f//t/6t+/v9q0aaPq1avr9ddfV1hYmLKysrzf/V81atTQ5MmTVb58eZ08edJbNalTp46cTqck6cEHH9SCBQvk8XjUrl077/sw380336xp06ZJkg4fPqxevXopJSVFp06dUtOmTSVJN954o6ZOnSrp8p6/pKQkTZ06VWfOnFF0dPTvzsfExCgmJkbHjh3T1q1b9cMPP6hq1aq66667tGDBgkuObULZRTISIKtWrVKPHj307LPPSpKys7PVuXNnhYWF6dtvv1WjRo28fzE3aNBAjRo10uzZs2Wz2TRv3jxde+21ZoaPP6iw33uVKlUueb3NZvvde+XKlfP+hbp3715JP40DefXVV7V582ZJ0uOPP67C9rw8c+aMRo0apcWLFysiIkK1a9dWlSpVFBoaqsmTJ+vll19Ww4YN9eqrr+r48eMFPvv3v/9d69evV0REhJ599lnvd4SE/FJUveGGG5SQkKBly5ZpyJAhxf+Hg4CqVq2a9+fq1atr//79uu6667Rjxw7Vq1dPUvGfv9zcXK1bt06vvPKKJKlr167q1q2bateu/bvPv/HGGxoyZIh27dolu90um82mrKyskr49WBzJSIAsXbpUU6ZM8R6Hh4erS5cuqlatmkaPHq3y5csrNDRUNWrU0HXXXadbbrlFDz/8sHJzc9WiRQvVqFHDxOjxRxX2e/9vN0lx3H333RoyZIh27NihZs2aSZIiIiLUunVrxcbGyuFwqGLFijp16pTq1Knzu883a9bMO6MiLCxM+fn53m6je++9V4MHD1bFihVVs2ZNnTt3rsBn7733XvXp00fh4eGqVq2aTp06dckY//KXv2jdunXeKh+uDP/tpgkJCVFWVpaee+45hYWFadKkSXrhhRdkGIbsdrsSEhIKbeNSz5/T6VSlSpX00EMPKSwsTO3bt1etWrV+99mvvvpKtWrVUvXq1dWuXTsNGjRI//znPzVhwoRSu2dYk80o7M8pBMSiRYt09913q2rVqpo2bZpCQ0MVHx9vdljAZZk9e7YqV66snj17mh0KAAuiMmKyq666Sk888YTKly+vyMhI70AywCqee+45nTp1yrueBABcLiojAADAVEztBQAApiIZAQAApiIZAQAApiIZAQAApiIZAQAApvr/T7WMpR2FQ3QAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 720x576 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,8))\n",
    "sns.heatmap(data.corr(),annot=True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "cc2b68f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "dd374460",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load data\n",
    "df = pd.read_excel(\"ESD.xlsx\", engine='openpyxl')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "2f6ce527",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Tenure Calculation\n",
    "# ===============================\n",
    "today = pd.to_datetime(\"today\")\n",
    "df[\"Hire Date\"] = pd.to_datetime(df[\"Hire Date\"])\n",
    "df[\"Exit Date\"] = pd.to_datetime(df[\"Exit Date\"])\n",
    "df[\"End Date\"] = df[\"Exit Date\"].fillna(today)\n",
    "df[\"Tenure (Years)\"] = (df[\"End Date\"] - df[\"Hire Date\"]).dt.days / 365"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "60626174",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>EEID</th>\n",
       "      <th>Full Name</th>\n",
       "      <th>Job Title</th>\n",
       "      <th>Department</th>\n",
       "      <th>Business Unit</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Ethnicity</th>\n",
       "      <th>Age</th>\n",
       "      <th>Hire Date</th>\n",
       "      <th>Annual Salary</th>\n",
       "      <th>Bonus %</th>\n",
       "      <th>Country</th>\n",
       "      <th>City</th>\n",
       "      <th>Exit Date</th>\n",
       "      <th>End Date</th>\n",
       "      <th>Tenure (Years)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>E02387</td>\n",
       "      <td>Emily Davis</td>\n",
       "      <td>Sr. Manger</td>\n",
       "      <td>IT</td>\n",
       "      <td>Research &amp; Development</td>\n",
       "      <td>Female</td>\n",
       "      <td>Black</td>\n",
       "      <td>55</td>\n",
       "      <td>2016-04-08</td>\n",
       "      <td>141604</td>\n",
       "      <td>0.15</td>\n",
       "      <td>United States</td>\n",
       "      <td>Seattle</td>\n",
       "      <td>2021-10-16</td>\n",
       "      <td>2021-10-16 00:00:00.000000</td>\n",
       "      <td>5.526027</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>E04105</td>\n",
       "      <td>Theodore Dinh</td>\n",
       "      <td>Technical Architect</td>\n",
       "      <td>IT</td>\n",
       "      <td>Manufacturing</td>\n",
       "      <td>Male</td>\n",
       "      <td>Asian</td>\n",
       "      <td>59</td>\n",
       "      <td>1997-11-29</td>\n",
       "      <td>99975</td>\n",
       "      <td>0.00</td>\n",
       "      <td>China</td>\n",
       "      <td>Chongqing</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2025-04-08 22:20:13.861085</td>\n",
       "      <td>27.375342</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>E02572</td>\n",
       "      <td>Luna Sanders</td>\n",
       "      <td>Director</td>\n",
       "      <td>Finance</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Female</td>\n",
       "      <td>Caucasian</td>\n",
       "      <td>50</td>\n",
       "      <td>2006-10-26</td>\n",
       "      <td>163099</td>\n",
       "      <td>0.20</td>\n",
       "      <td>United States</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2025-04-08 22:20:13.861085</td>\n",
       "      <td>18.463014</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>E02832</td>\n",
       "      <td>Penelope Jordan</td>\n",
       "      <td>Computer Systems Manager</td>\n",
       "      <td>IT</td>\n",
       "      <td>Manufacturing</td>\n",
       "      <td>Female</td>\n",
       "      <td>Caucasian</td>\n",
       "      <td>26</td>\n",
       "      <td>2019-09-27</td>\n",
       "      <td>84913</td>\n",
       "      <td>0.07</td>\n",
       "      <td>United States</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2025-04-08 22:20:13.861085</td>\n",
       "      <td>5.534247</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>E01639</td>\n",
       "      <td>Austin Vo</td>\n",
       "      <td>Sr. Analyst</td>\n",
       "      <td>Finance</td>\n",
       "      <td>Manufacturing</td>\n",
       "      <td>Male</td>\n",
       "      <td>Asian</td>\n",
       "      <td>55</td>\n",
       "      <td>1995-11-20</td>\n",
       "      <td>95409</td>\n",
       "      <td>0.00</td>\n",
       "      <td>United States</td>\n",
       "      <td>Phoenix</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2025-04-08 22:20:13.861085</td>\n",
       "      <td>29.402740</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>E03094</td>\n",
       "      <td>Wesley Young</td>\n",
       "      <td>Sr. Analyst</td>\n",
       "      <td>Marketing</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Male</td>\n",
       "      <td>Caucasian</td>\n",
       "      <td>33</td>\n",
       "      <td>2016-09-18</td>\n",
       "      <td>98427</td>\n",
       "      <td>0.00</td>\n",
       "      <td>United States</td>\n",
       "      <td>Columbus</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2025-04-08 22:20:13.861085</td>\n",
       "      <td>8.558904</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>E01909</td>\n",
       "      <td>Lillian Khan</td>\n",
       "      <td>Analyst</td>\n",
       "      <td>Finance</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Female</td>\n",
       "      <td>Asian</td>\n",
       "      <td>44</td>\n",
       "      <td>2010-05-31</td>\n",
       "      <td>47387</td>\n",
       "      <td>0.00</td>\n",
       "      <td>China</td>\n",
       "      <td>Chengdu</td>\n",
       "      <td>2018-01-08</td>\n",
       "      <td>2018-01-08 00:00:00.000000</td>\n",
       "      <td>7.613699</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>E04398</td>\n",
       "      <td>Oliver Yang</td>\n",
       "      <td>Director</td>\n",
       "      <td>Marketing</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Male</td>\n",
       "      <td>Asian</td>\n",
       "      <td>31</td>\n",
       "      <td>2019-06-10</td>\n",
       "      <td>176710</td>\n",
       "      <td>0.15</td>\n",
       "      <td>United States</td>\n",
       "      <td>Miami</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2025-04-08 22:20:13.861085</td>\n",
       "      <td>5.832877</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>E02521</td>\n",
       "      <td>Lily Nguyen</td>\n",
       "      <td>Sr. Analyst</td>\n",
       "      <td>Finance</td>\n",
       "      <td>Speciality Products</td>\n",
       "      <td>Female</td>\n",
       "      <td>Asian</td>\n",
       "      <td>33</td>\n",
       "      <td>2012-01-28</td>\n",
       "      <td>95960</td>\n",
       "      <td>0.00</td>\n",
       "      <td>China</td>\n",
       "      <td>Chengdu</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2025-04-08 22:20:13.861085</td>\n",
       "      <td>13.202740</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>E03545</td>\n",
       "      <td>Sofia Cheng</td>\n",
       "      <td>Vice President</td>\n",
       "      <td>Accounting</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Female</td>\n",
       "      <td>Asian</td>\n",
       "      <td>63</td>\n",
       "      <td>2020-07-26</td>\n",
       "      <td>216195</td>\n",
       "      <td>0.31</td>\n",
       "      <td>United States</td>\n",
       "      <td>Miami</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2025-04-08 22:20:13.861085</td>\n",
       "      <td>4.704110</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 16 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       EEID        Full Name                 Job Title  Department  \\\n",
       "0    E02387      Emily Davis                Sr. Manger          IT   \n",
       "1    E04105    Theodore Dinh       Technical Architect          IT   \n",
       "2    E02572     Luna Sanders                  Director     Finance   \n",
       "3    E02832  Penelope Jordan  Computer Systems Manager          IT   \n",
       "4    E01639        Austin Vo               Sr. Analyst     Finance   \n",
       "..      ...              ...                       ...         ...   \n",
       "995  E03094     Wesley Young               Sr. Analyst   Marketing   \n",
       "996  E01909     Lillian Khan                   Analyst     Finance   \n",
       "997  E04398      Oliver Yang                  Director   Marketing   \n",
       "998  E02521      Lily Nguyen               Sr. Analyst     Finance   \n",
       "999  E03545      Sofia Cheng            Vice President  Accounting   \n",
       "\n",
       "              Business Unit  Gender  Ethnicity  Age  Hire Date  Annual Salary  \\\n",
       "0    Research & Development  Female      Black   55 2016-04-08         141604   \n",
       "1             Manufacturing    Male      Asian   59 1997-11-29          99975   \n",
       "2       Speciality Products  Female  Caucasian   50 2006-10-26         163099   \n",
       "3             Manufacturing  Female  Caucasian   26 2019-09-27          84913   \n",
       "4             Manufacturing    Male      Asian   55 1995-11-20          95409   \n",
       "..                      ...     ...        ...  ...        ...            ...   \n",
       "995     Speciality Products    Male  Caucasian   33 2016-09-18          98427   \n",
       "996     Speciality Products  Female      Asian   44 2010-05-31          47387   \n",
       "997     Speciality Products    Male      Asian   31 2019-06-10         176710   \n",
       "998     Speciality Products  Female      Asian   33 2012-01-28          95960   \n",
       "999               Corporate  Female      Asian   63 2020-07-26         216195   \n",
       "\n",
       "     Bonus %        Country       City  Exit Date                   End Date  \\\n",
       "0       0.15  United States    Seattle 2021-10-16 2021-10-16 00:00:00.000000   \n",
       "1       0.00          China  Chongqing        NaT 2025-04-08 22:20:13.861085   \n",
       "2       0.20  United States    Chicago        NaT 2025-04-08 22:20:13.861085   \n",
       "3       0.07  United States    Chicago        NaT 2025-04-08 22:20:13.861085   \n",
       "4       0.00  United States    Phoenix        NaT 2025-04-08 22:20:13.861085   \n",
       "..       ...            ...        ...        ...                        ...   \n",
       "995     0.00  United States   Columbus        NaT 2025-04-08 22:20:13.861085   \n",
       "996     0.00          China    Chengdu 2018-01-08 2018-01-08 00:00:00.000000   \n",
       "997     0.15  United States      Miami        NaT 2025-04-08 22:20:13.861085   \n",
       "998     0.00          China    Chengdu        NaT 2025-04-08 22:20:13.861085   \n",
       "999     0.31  United States      Miami        NaT 2025-04-08 22:20:13.861085   \n",
       "\n",
       "     Tenure (Years)  \n",
       "0          5.526027  \n",
       "1         27.375342  \n",
       "2         18.463014  \n",
       "3          5.534247  \n",
       "4         29.402740  \n",
       "..              ...  \n",
       "995        8.558904  \n",
       "996        7.613699  \n",
       "997        5.832877  \n",
       "998       13.202740  \n",
       "999        4.704110  \n",
       "\n",
       "[1000 rows x 16 columns]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9509b93c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjgAAAFgCAYAAAC2QAPxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAB05ElEQVR4nO3deXxcdb3/8ddZZ8lkK03b0E1aKEoBS4v+fhdovYBehAsIClexFhEVXHADKgIuVWsFERfgKl7lXrhYoMgmiCJw+UFEUbCXAi3SymJbSpqmbUgyme1svz8mM50kM5OZZGYyJ/08Hw8fNjPnfL/fc76ZyZcz5z0fxfM8DyGEEEKISUSd6AEIIYQQQlSaLHCEEEIIMenIAkcIIYQQk44scIQQQggx6cgCRwghhBCTjixwhBBCCDHp6BM9ACFE6SzL4vjjj+fQQw/lpptuqnn/X/nKVzjkkEP4+Mc/PuK5n//85/zmN7/B8zxc12Xp0qV86UtfwjTNom0eeuihPPXUU0yZMqVawx6TE044AcMwCAaDuK6L67qce+65fPCDH5ywMW3bto0vfelLJJNJzjvvPM466ywAfv3rX/Pqq6/ypS99acLGJkS9kQWOED7yyCOPcOihh7Jp0yZeeeUV5s+fP9FDAuB3v/sdjz76KOvWrSMYDJJMJvn85z/PDTfcwMUXXzzRwxuz73//+xxxxBEAdHZ2ctJJJ7Fs2TLa29snZDxr167l/PPP5z3veQ+nnHIKZ511FtFolLVr13LLLbdMyJiEqFeywBHCR26//XZOOeUU5s6dyy233MK3vvUt/vKXv/DDH/6Q2bNn8/e//51UKsXXv/51/u///b985StfIRKJsHnzZnbu3Mm8efP4wQ9+QENDw4grJ5mfW1paWLNmDc899xwDAwN4nsfq1atZsmRJwXF1d3fjOA6JRIJgMEggEOBrX/sae/fuBeC1117jW9/6FrFYjF27dvHWt76VH/3oRwQCgWwbsViMVatW8Y9//IPe3l4aGhr4/ve/z7x581ixYgXNzc28+uqrnHLKKdx00010dHTQ2NiI53m8973v5cc//jFvfetbs+196EMf4rzzzuO9730vkF6seJ7Heeedx2WXXUZPTw8A73rXu/jiF7846rnv7e0lFAoRDocB+Otf/8r3vvc94vE4hmHwxS9+kWXLlnHPPffwyCOPoKoqW7duxTAMrr76ahYsWMCKFStYvnx5dky5P1933XU88sgjGIZBa2sr3/3ud5k2bdqQMZimSTweJ5lMoqrpOwz+/d//nY997GOEQqFRj0GI/YncgyOET7z88sts2LCBk08+mTPOOINf//rX2T/Szz//POeffz733XcfZ511FjfccEN2v40bN3LTTTfx29/+ll27dvHQQw8V7ee5555j165drFu3jt/+9receeaZ/PznPy+6z5lnnklTUxPHHXccH/zgB7nqqqvo7OzkyCOPBODOO+/kjDPOYN26dTz88MO8/vrrPP7440Pa6OjooKmpiTvvvJPf//73HH744axduzb7fFNTE7/97W+56KKL+Kd/+ifuv/9+AP785z/T0tIyZHEDcPbZZ3PvvfcC4DgO999/P2effTZ33nkns2bN4t5772Xt2rVs3bqV/v7+vMd16aWX8r73vY/3vve9nHnmmXzoQx+iubmZnp4ePv/5z3PllVfywAMPcPXVV7Ny5Uq2b98OwDPPPMPXvvY1fvOb37B48eJRP07s7Ozklltu4e677+aee+7h2GOP5fnnnx+x3YoVK/jtb3/LRz/6Ub785S/zyiuvsGXLFk4++eSi7QuxP5IrOEL4xO23384///M/09LSQktLC7NmzWLdunUcddRRHHjggbztbW8D4LDDDsv+YQdYunRp9j6YBQsW0NvbW7Sfo446iubmZu644w62b9/OX/7yFxoaGoru09jYyH/+53+yfft2/vznP/P0009zwQUX8OEPf5iVK1eycuVK/vjHP/Lzn/+cf/zjH+zatYtYLDakjfe+973Mnj2bW2+9la1bt/L0009z1FFHZZ8/+uijs/9evnw511xzDcuXL2fdunWcc845I8Z08skn873vfY/u7m5efPFF5s6dy1ve8haWLl3KBRdcQGdnJ8cccwyXXHIJjY2NeY8r9yOqrq4uPvrRj3LIIYfQ2NjInDlzePvb3w7AIYccwuLFi3n66adRFIWFCxcyY8YMID0fjzzySNHzN336dN761rdy5plnsmzZMpYtW8Y//dM/jdhu2rRp/Od//mf2509+8pNcfvnlPP7449x22220tLRwxRVX0NLSUrQ/IfYHcgVHCB+IxWLcd999rF+/nhNOOIETTjiB7u5u1q5di23bBIPB7LaKopBbYq7YcxmpVCr778cff5wLL7wQgBNPPDHv4mG4n//85/zv//4vs2fP5uyzz+aaa67h5z//ObfddhsAF198MXfeeSczZ87kvPPOY+HChSPGcdttt3HllVcSDAY57bTTOPXUU4dsk/loCOCYY44hHo/z1FNP8de//jXvFYxwOMxJJ53Eb37zG+6++27OPvtsAI488kj+53/+hw9+8IPs2LGDs88+m//93/8d9RinT5/OCSecwDPPPIPruiOe9zwP27aB4uc899+WZQGgqiq//OUv+e53v5v9iHD16tVFx/PQQw8xb948Dj74YL773e/y4x//mOOOO46bb7551GMRYn8gCxwhfOCBBx6gtbWVP/zhDzz22GM89thjPProo8RiMfbs2TOmNqdMmcILL7wAMOQKwx//+EeOP/54PvzhD3PEEUfw6KOP4jhO0bYSiQTXXnstb775Zvax1157jcMOOwyAJ598ks9+9rOccsopKIrCc889N6LNJ598kjPPPJOzzz6bgw46iMcee6xgv4qi8OEPf5grr7ySU089dci9PLn+7d/+jXvuuYdnn32Wk046CUhflfnJT37Cu9/9bq688koOPvhg/vGPfxQ9PkgvMv/0pz9x5JFH8va3v53XXnst+zHS3//+d5555hne+c53Fm1jypQpbNy4EUgnojZv3gzASy+9xKmnnsr8+fO58MILOe+887LP5ROPx7npppv43Oc+B4Bt22iahqqqJBKJUY9FiP2BfEQlhA/cfvvtfOxjH0PTtOxjTU1NrFixYszpma9+9at861vfoqmpiWOOOYa2tjYgfXPupZdeymmnnYamaRx99NE8/PDDea9aZHzmM59BURQ+9KEPoSgKruty+OGH86Mf/QiAL33pS3z2s5+lubmZUCjEO97xDrZt2zakjfPPP5+vf/3r3HPPPWiaxsKFC9myZUvBPs8880yuvvrqorHtww8/HF3XOemkk7KLoI9+9KN85Stf4dRTT8U0TQ499FBOPfXUvPtfeumlBINBFEUhHo9z8skn84EPfACAH//4x3z7298mkUigKArf/e53Oeigg3j22WcLjufTn/40X/nKV3jiiSeYN29e9mO3t771rdm2w+EwwWCQr371qwXbufHGG/nwhz9MJBLJnrszzjiDSCTCtddeW3A/IfYnipfverUQQtS5Bx98kHvvvZdf/OIXEz0UIUQdkis4QgjfWbFiBbt37+b666+f6KEIIeqUXMERQgghxKQjNxkLIYQQYtKRBY4QQgghJh1f34Pjui6O459P2DRN8dV492cyV/4i8+UfMlf+4Ze5Mgwt7+O+XuA4jsebb8ZG37BOtLSEfTXe/ZnMlb/IfPmHzJV/+GWu2tryfxO5fEQlhBBCiElHFjhCCCGEmHRkgSOEEEKISUcWOEIIIYSYdGSBI4QQQohJRxY4QgghhJh0ZIEjhBBCiElHFjhCCCGEmHRkgSOEEEKISacq32Tsui6rVq1i8+bNmKbJ6tWrmTt37ohtLrjgAk488UTOOeccEokEK1euZM+ePTQ0NHD11VczZcqUagxPCCEmpU2dfTywqYvO3gTtzUFOWzidhe1N427L1FVUBRKWO+52xzOOWvftF7U4R5k+tuyKMpByaDBUFkxvLNrXRM9dVa7gPProo6RSKdatW8cll1zCVVddNWKbH/3oR/T19WV/vv3221mwYAG33XYbZ5xxBj/5yU+qMTQhhJiUNnX2ceOfttIbt5jWaNIbt7jxT1vZ1Nk3+s5F2tJVeP6NPjbs6MPQlHG1O55xjPeYJqtanKNMH9t74uzsSxBN2nRFU2zbGyvYVz3MXVUWOOvXr2fp0qUALFq0iI0bNw55/qGHHkJRlOw2w/dZtmwZTz31VDWGJoQQk9IDm7qImBqNQR1FUWgM6kRMjQc2dY2rre29CUKGSsjQ2NaTGFe74xnHeI9psqrFOcr00R1NYeoaYVPD0BR2x1IF+6qHuavKR1TRaJRIJJL9WdM0bNtG13W2bNnCb37zG6677jr+/d//fcg+jY3pglkNDQ309/eP2o+mKbS0hCt/AFWiaaqvxrs/k7nyF5kv6I5ZTG8KoCpK9rFWQ6OrL1n2ucltK265hAwNRYFYysU09TG3C+XNVSWPabKq5jnKzFWmj/jOKGFTBRRMRSFuObQ2BvL2VQ9zV5UFTiQSYWBgIPuz67roerqr++67j66uLj760Y+yY8cODMNg5syZQ/YZGBigqWn0z+mkmrioFpkrf5H5grawQU9/ksbgvrf1/oRNW9go+9zkthUyVFK2AyiEdJVUyh5zu1DeXFXymCarap6jzFxl+gjpKknLxdAULMclZKj09Cfz9lXLuatpNfHFixfT0dEBwIYNG1iwYEH2uS9/+cv86le/4tZbb+XMM8/kvPPOY9myZSxevJgnnngCgI6ODpYsWVKNoQkhxKR02sLpRFMO/Qkbz/PoT9hEUw6nLZw+rrZmNweJWy5xy2FOa3Bc7Y5nHOM9psmqFuco00dbxCRlO8RSDpbjMTVsFuyrHuZO8TzPq3SjmRTVli1b8DyPNWvW0NHRwZw5czjxxBOz211//fVMnTqVc845h3g8zmWXXUZ3dzeGYXDttdfS1tZWtB/Lcny1ipf/yvQPmSt/kflK80OKqty5mugkjh9U6xzlzlU9p6gKXcGpygKnVmSBI6pF5spf9vf5qqdFwGhjyfdHsx7GXYpqLSArceyltFdqn5ntumMWbWEj73b3v9DJ2vU72DuQYkqDyfIlM5k/tWFC5lMWOHVgf38T9hOZK3/Zn+crE8eNmBqRgEY06RBNOXzqmLk1XyyUMpbMXNXTuEtRyfFW+thLaa/UPnO3a20M0NOfHLHd/S90cl3HawR0lZChErdcBlIO0yMm86Y21Hw+a3oPjhBCiNqohzjuWMZST+MuRbVi+JU49lLaK7XP3O3UAtutXb+DgK4SNjUURSFsarieR1c0VVfzKQscIYTwsc7eBJGANuSxSECjszdR12Opp3GXopLjrfSxl9JeqX2Wst3egRQhY+jywXU9LNsdtf1akgWOEEL4WHtzkGjSGfJYNOnQ3hys67HU07hLUcnxVvrYS2mv1D5L2W5Kg0ncGrqYUVUFQ1eL7ldrssARQggfq4c47ljGUk/jLkW1YviVOPZS2iu1z9zt3ALbLV8yk6TtEks5eJ5HLOWgKgrTI2ZdzafcZFxD+/ONkH4jc+Uv+/t81VMaaTKlqLLR6K5+BiwXBfCgpIh0qW3Xc4rq1b0xemNW3uOVFFWVyQJHVIvMlb/IfPmHX+YqkyZyHJetPXEAPM/joAMaUFWlbtNelbKps4+bnn6dgErdp9wkRSWEEEKUKJMm2h1LYWjppJCppwtOTnQ6qBYe2NRFJOiflFs+ssARQgghhsmkiWJJB11NF4w0NIVYyp7wdFAtpI9/aLlKvx23LHCEEEKIYTJponBAw3bTd3JYjkfY1Cc8HVQL6eO3hzzmt+OWBY4QQggxTCZNNDVsYjnppFDKThecnOh0UC2ctnA60YR/Um75yAJHCCGEGGZhexOfOmYuc6aEmR4xiQR0ZjQFmd0aqssbbSttYXsTXzjxYJpDBrv6UzSHDN8dtz76JkIIIfYn1Y5vV6P9ctssZfuF7U01/YNeaEyVOl/ltvP2WS3Mfbc5nkOaUHIFRwghRFYmHt0bt5jWaNIbt7jxT1vZ1NlXkfafe/3Nirdf7pirfYxjUWhM97/QWZGx1uMxV5sscIQQQmRVuwjmvc/uqHj75Y65Hgt9FhrT2vWVOV/1eMzVJgscIYQQWdUugrm9J17x9ssdcz0W+iw0pr0DqYqMtR6PudpkgSOEECKr2kUwZ7eGKt5+uWOux0KfhcY0pcGsyFjr8ZirTRY4QgghsqpdBPPMo2ZWvP1yx1yPhT4LjWn5ksqcr3o85mqTWlQ15JcaLELmym9kviqrmimqlpYwf/zbTl+kqGqt3lJUfnldSbHNOuCXXxYhc+U3Ml8j1eoPuN//aA4f/2HTI7zYFa1IVe5C2wIF96+neStlrjZ19vHfz2xn085+QOFt0yOc987ZNV0sygKnDtTbC1sUJnPlLzJfQ2UiwRFTq2ol6LH0U09zNXz8O95MsKV7gEOnRTiwOZD3eMo55nzb7uxL4uHR3hQcsT9QV/M22lxt6uzj+4+9wht9CYK6iqJA3HJpbwqw8oSDa7bIkWriQgixn6hVJNjv0ePh498dSxHQVbqjqYLHU84x59u2J27RG7fz7u+3eXtgUxc9cYuQoWHqKoamEjJUeuN2XfwOyAJHCCEmmVpFgv0ePR4+/ljSIWSoxFL7ikwOP55yjjnftpbtkHLcvPv7bd46exNYtoOhKdnHdFUh5bh18TsgCxwhhJhkahUJ9nv0ePj4wwGNuOUSNvdVMRp+POUcc75tDV3D1Ib+6c3s77d5a28OYugalrPvThfb9TA1tS5+B2SBI4QQk0ytIsF+jx4PH//UsEnSdmmLmAWPp5xjzrdta8igOaTn3d9v83bawum0hgzilkPKdrEcl7jl0hzS6+J3QG4yrqF6urlOFCdz5S8yXyPVIo2zqbOPm5/ezt+6ooDHwhmNnPuO4gma8c5VpY9LUlQJgoaK60HKdof0OZYU1YFNAVrDBgnLxdRVVAUSllvVY6lpisp1XVatWsXmzZsxTZPVq1czd+7c7PNr167lnnvuQVEUzj//fE455RQ8z2PZsmW85S1vAWDRokVccsklRfuRBY6oFpkrf5H5qr2xJrXGM1e1SoftT4qd02PfNqOsucptK2U7bNwZBeCI9kYMTa3aXBVa4Oh5Hx2nRx99lFQqxbp169iwYQNXXXUVP/3pTwHYu3cvt99+O/feey/JZJJ//dd/5eSTT2bbtm0sXLiQG2+8sRpDEkIIUUG5SRwg+/8PbOqq2mJjIvqc7Iqd02PfNmPMbW3YMUDIUAGFbT0JFs1qym5Tq7mqygJn/fr1LF26FEhfidm4cWP2uSlTpnDfffeh6zo7duwgEAigKAqbNm2iq6uLFStWEAwGufzyy5k3b17RfjRNoaUlXI1DqApNU3013v2ZzJW/yHzVXnfMYnpTAFXZl6BpNTS6+pJF52I8czXWPkVhxc5puXOV21bccgkZGooCsZSLaeo1n6uqLHCi0SiRSCT7s6Zp2LaNrqe703WdX/7yl1x//fWsWLECgLa2Ni644AJOPvlk/vrXv7Jy5Uruvvvuov04juery9JyGd0/ZK78Rear9trCBj39yex/8QP0J2zawkbRuRjPXI21T1FYsXPqOG5Z5zW3rZChkrIdQCGkq6RSdtXmqqZf9BeJRBgYGMj+7LpudnGT8ZGPfIQ//OEPPPPMM/z5z3/m8MMP58QTTwTg6KOPZteuXfj4/mchhJjUJiJB5ffUVj2q5DnNbWt2c5C45RK3HOa0BidkrqqywFm8eDEdHR0AbNiwgQULFmSfe/XVV7nooovwPA/DMDBNE1VVueGGG7jlllsAeOmll2hvb0fJuWQmhBCifixsb+JTx8ylOWSwqz9Fc8io+s2+E9HnZFfJc5rblu3CkQc2sWhmE5bjTchcVTVFtWXLFjzPY82aNXR0dDBnzhxOPPFEbrjhBjo6OlAUhaVLl3LRRRfR29vLypUricViaJrG17/+debPn1+0H0lRiWqRufIXma/STVQV7Uy/3TGLtrAxIdHosahGJe9Csexq9j+Wsb66N0ZvzKLBUFkwvbGu5iWXFNusA/Im7B8yV/4i81WaiYpZ5/bb2higpz9Z8wKT4x33eMaW247luLzQ2Q/A4TMimLpWVrHOap+bTJ+u67G1J569VWRuawhNU+tiXoaTYptCCLGfm6jimLn9qhNUYHK84x5vUcpMO9t6EoQMjZChsr03UXaxzmqfm0yf3dEUpq4SNjUMLV2ItF7mpVSywBFCiP3ERBXHLNZvPRfsrGRRykw7sZSNoSnoqkJssB5UOcU6q31uMn1mxglkx1ov81IqWeAIIcR+YqKKYxbrt54LdlayKGWmnbCpYzketusRHly8lFOss9rnJtNnZpxAdqz1Mi+lkgWOEELsJyYqZp3brztBBSbHO+7xFqXMtDOnNUjccohbLrObi8enJzKK3xYxSdkusZSD5aQLkdbLvJRKbjKuIbkR0j9krvxF5qt0kqIqj6SoJEU1IWSBI6pF5spfZL4q+4dwrG2Vsl815qrU8VZrsVAP577ctjLPbdkVZSDl5F3ElFpNfKIXp5KiEkKISSoT7e2NW0xrNOmNW9z4p61s6uyrWVuVHEM1xlut8dXDuS+3rcxz23vi7OxLEE3adEVTbNsbK6u/iZrzUskCRwghfK6SceKxtlUPEfRi/VZrfPVw7stta2gUXBtzFLyeI/4gCxwhhPC9SsaJx9pWPUbQazG+ejj35bZVqSh4PUf8QRY4Qgjhe5WME4+1rXqMoNdifPVw7sttq1JR8HqO+IMscIQQwveqVRG6nLbqIYJerN9qja8ezn25bQ2NgjtjjoLXc8QfJEVVU5L08A+ZK3+R+aqPJI+kqCRFVU8pKlng1JC8CfuHzJW/yHyNNNoft/9+ZjubdvYDCm+bHuG8d87O+7005XxnS6Ex5P4RPXJOK/NagrzYFaWzN4Gpq6gKJKzy2x+PUv4w59sGmPA/6KWOf7z88rqSBU4d8Msvi5C58huZr6GKVaEG+P5jr/BGX4KgrqIoELdc2psCrDzhYIAxVb4uNAbX9XhtzwCKkr6ZdVqTyfa9CQ6dFiGoK2zcGQXgiPZGDE2teXXzQlW6823T2ZdAQWFGU2BCK5/Xqsq4X15X8j04QgixnxgtItwTtwgZGqauYmgqIUOlN26PqO5dTuXrQmMYHkXetjdBQFfpjqbY3psgZKiEDI1tPeW1X63zU2yb3rhNT9ya8Fh0vcez64UscIQQYpIZLSJs2U42HgzpiHDKcUdU9y6n8nWhMQyPIicsh5ChEkvZxJIOuqpgaAqxlF1W++NRSrw53zYpx8WynaL71UK9x7PrhSxwhBBikhktImzoWjYeDOmIsKmpI6p7l1P5utAYhkeRg4ZG3HIJmzrhgIbteliOR9jUy2p/PEqJN+fbxtRUDF0rul8t1Hs8u17IAkcIISaZ0SLCrSGDuOWQsl0sxyVuuTSH9BHVvcupfF1oDMOjyHOmBEnaLm0Rk9nNQeKWS9xymNNaXvvVOj/FtmkO6bSGjAmPRdd7PLteyE3GNeSXG7aEzJXfyHyNVOkU1Z6BVME4caH+b356O3/rimI5LkFd5YCwMaYUVaVj4KMdf75jAI+FMxo59qAp2bFXI7002jGUEu8erZ1SnztoWoT3HHxAye1OFElR1QF5E/YPmSt/kfmqrnJTO8W2P/ZtM8qaq1L7rvR2Yznu8Rqtv0ocI1Dyc0kPeqKpsvuvNUlRCSGEGJNyUzsTUYCyGkU3a51WGq2/ShxjOc81BY0x9V8vZIEjhBCiqHJTOxNRgLIaRTdrnVYarb9KHONYnyun/3ohCxwhhBBFlZvamYgClNUoulnrtNJo/VXiGMf6XDn91wtZ4AghhCiq3NTORBSgrEbRzVqnlUbrrxLHWM5zfQlrTP3XC7nJuIbkRkj/kLnyF5mv6is3PVNo+7HMVTVSVKUeS61TQ6WmqMZzjJKiGgfXdVm1ahWbN2/GNE1Wr17N3Llzs8+vXbuWe+65B0VROP/88znllFNIJBKsXLmSPXv20NDQwNVXX82UKVOK9iMLHFEtMlf+kpmveq3qXIv2M5Hm59/oI245GKpCJKBzQIPJgmmRCf1DNNofzWLb556bas5JKfHrWv5xr0Vfw/s4bHqEP7y6NxuLXzS7lXMWtZddXLXWRVRrusB5+OGHeeyxx7jqqqvYsGEDP/vZz/jpT38KwN69ezn33HO59957SSaT/Ou//iuPP/44N998M9FolM997nM8+OCDPPvss3z1q18t2o8scES1yFz5S0tLmD/+bWfFIqzVjsNWuv1NnX1c89jLbH8zQcJy8Lz0twZrCjSYGodOb0RVlQmJ8w4/1uHR49G2z5yb9yyYyiNbdldlTgoVBp3bGkLT1FHj1dVYeFS7r+F9vNGbZFNnH5qaTkd5HqQcjxmNAS49YX7JxVUjpkbKdmpaRLWmMfH169ezdOlSABYtWsTGjRuzz02ZMoX77rsPwzDYvXs3gUAARVGG7LNs2TKeeuqpagxNCDFJTUQ0uR7GmmmvN27jOB66ln5bVwff3W0PuqOpCYvzjhY9Hm37zLlZu35H1eakUGHQ3bFUSfHqSqtFX8P76I6mcD1wXA9DUzF1lZCp0RO3yiqu2hjUJ6yI6nB6NRqNRqNEIpHsz5qmYds2up7uTtd1fvnLX3L99dezYsWK7D6NjelVWENDA/39/aP2o2kKLS3hKhxBdWia6qvx7s9krvxF01S6YxbTmwKoyr4ikq2GRldfsuy5rGRbtWi/O2Zhex6Ol/7jlMRDQcHFw/U84rZLa2OgYuMvd2y5x6oqStGxFDo3Pa/30tpYnTnJ9BnfGSVsqoCCqSjELSc7VqCqvxP5xlPNvob3EbddUMDxPNTB1bEKDNg23TFr1H5z24tbLiFDQ1EglnIxTb1q56qYqixwIpEIAwMD2Z9d180ubjI+8pGP8G//9m988pOf5M9//vOQfQYGBmhqGv0yluN4vvoYQT728A+ZK39paQnTFjbo6U/SGNz3XtOfsGkLG2XPZSXbqkX7bWGDVxUFTVFwXA91cHGjkl5QhHSVnv5kxcZf7thyj9U09aJjKXRuWkPVm5NMnyFdJWm5GJqC5biEjH3nDajq70S+8VSzr+F9hHSVXg80RcF1XQAcL10BvpR+c9sLGSop2wHSv3uplF21cwU1/ohq8eLFdHR0ALBhwwYWLFiQfe7VV1/loosuwvM8DMPANE1UVWXx4sU88cQTAHR0dLBkyZJqDE0IMUlNRDS5Hsaaaa85pKNpCraT/uM0+DcKXYG2iDlhcd7RosejbZ85N8uXzKzanBQqDDo1bJYUr660WvQ1vI+2iImqgKamF3cp2yWecmgNGWUVV+1P2BNWRHW4qqaotmzZgud5rFmzho6ODubMmcOJJ57IDTfcQEdHB4qisHTpUi666CLi8TiXXXYZ3d3dGIbBtddeS1tbW9F+5CZjUS0yV/4iKSpJUVVqjJKikhRVXZAFjqgWmSv/2NTZxyMv7+G1XdGCfwzH82ab7w8NMOofn7F8X8l4K2uPday1JK8t//DLXMkCpw745ZdFyFz5RSaa2hoxCSjkjRSPJ7KaL67b2ZdAQWFGU6BghHcsVZ9LGWe5VaJ39iXx8GhvCtZN9Wd5bfmHX+ZKqokLISadTDS1KWgUjBSPJ7KaL67bG7fpiVtFI7xjqfpcyjjLrRLdE7fojdu+qf4sRCXJAkcI4VuFqhvvHUhlH48lHXRVwdAUYik7u00pFZDztZ9yXCx7aMHB4e2NpepzKeMstxK0ZTukBm86LjYOISYjWeAIIXyrUHXjKQ1m9vFwQMN2PSzHI2zq2W1KqYCcr31TUzH0oQuJ4e2NpepzKeMstxK0oWuYmpp3eyEmO1ngCCF8KxNN7UtYBSPF44ms5ovrNod0WkNG0QjvWKo+lzLOcqtEt4YMmkO6b6o/C1FJcpNxDfnlhi0hc+UXmWj05u4BXNdl4YxGzn3H7FFTVIdNj/DH1/ayaWc/oPC26RHOe+dsYGTiKPexTDvd/UkGLJcGU6MtYuJ6kLLdsiPNmfFnYrmzmoM0h4wh43yxK1pyKmp4ewtnNHLsQVOGtDG8zdF+rnTqSl5b/uGXuZIUVR3wyy+LkLnyg9xEUWtjgJ7+ZEkJoU2dfXz/sVd4oy9BUFdRFIhbLs1BjQbTKJiOypdgGk9KabSk1VgKLpbb5o43E2zpHuDQaREObA7wRm+SzbuiLGhrYGZLsCqpK3lt+Ydf5kpSVEKISSU3NaSWkRB6YFMXPXGLkKFh6iqGphIyVHZFraLpqEqnlEZLWo2l4GK5be6OpQjoKt3RVLbgYkBX2R1LSepK+J4scIQQvlRqUinffpbtYGj7Chnqg19PXywdVemU0mjjH8vxldtmLOkQMtRsaiuWstM/59ysLKkr4VeywBFC+FKpSaV8+xm6huXs+3TedtNVuIuloyqdUhpt/GM5vnLbDAc04pabTW2FTT39c84iSFJXwq9kgSOE8KXc1JBbRkLotIXTaQ0ZxC2HlO1iOS5xy2VaxCiajqp0Smm0pNVYCi6W2+bUsEnSdmmLmNmCi0nbZWrYlNSV8D25ybiG/HLDlpC58otMUqk7ZtEWNkpO/Gzq7OO/n9leUopqeGmFStZ6Gi1pNZaCi+W2KSkqUYhf5kpSVHXAL78sQubKbwrN13grMo91/4moOr2lqz8bXZ/o6uHFyGvLP/wyV5KiEkLsVzKR6N64xbRGk964xY1/2sqmzr6q7j/efsuR6Wvb3hhd0RTRpM3OvgTbe+JV61MIv5AFjhBiUhpLzLoS+4+333Jk+todS2FoCmFTw9Q1uqMpiXeL/Z4scIQQk9JYY+Tj3X+8/ZYj01emUCeQLdYp8W6xv5MFjhBiUhprjHy8+4+333Jk+soU6gSyxTol3i32d7LAEUJMSmOJWVdi//H2W45MX1PDJpbjEUs5pGyHtogp8W6x35MFjhBiUlrY3sSnjplLc8hgV3+K5pBRVk2lse4/3n7LkelrzpQw0yMmkYDOjKYgs1tDVetTCL/QJ3oAQghRCYWi2eP5I1/O/uXGtUf7PppSY95jOcZaxtiFmChyBUcI4XvPvf5mzaLZ+ZQb1x4eJd/eE+e6jtfYtjdWs2j5RJ0rIWpFFjhCCN+799kdNYtm51NuXHt4lLyWVbxrGWMXYiLJAkcI4Xvbe+I1i2bnU25ce0RV7xpW8a5ljF2IiSQLHCGE781uDdUsmp1PuXHtEVW9a1jFu5YxdiEmkixwhBC+d+ZRM2sWzc6n3Lj28Ch5Lat41zLGLsREkmKbNeSXwmVC5spvWlrC/PFvOyc0GTRRKarxjHUizpW8tvzDL3NV02riruuyatUqNm/ejGmarF69mrlz52afv/nmm3nwwQcBeNe73sVFF12E53ksW7aMt7zlLQAsWrSISy65pGg/ssAR1SJz5R+bOvt45OU9vLYrOuKPdbX+kNd6gVCPxzHWfeW15R9+mauaVhN/9NFHSaVSrFu3jksuuYSrrroq+9z27du5//77ueOOO7jzzjt58skneemll9i2bRsLFy7k1ltv5dZbbx11cSOEEJnI895YakTkuVpx6FrHrOvxOCRqLvygKguc9evXs3TpUiB9JWbjxo3Z52bMmMEvfvELNE1DURRs2yYQCLBp0ya6urpYsWIFn/zkJ3n11VerMTQhxCSSiTw3BY0RkedqxaFrHbOux+OQqLnwg6p8k3E0GiUSiWR/1jQN27bRdR3DMJgyZQqe5/G9732Pww47jIMOOojdu3dzwQUXcPLJJ/PXv/6VlStXcvfddxftR9MUWlrC1TiEqtA01Vfj3Z/JXPlDd8xielMAVVEwzfTbWauh0dWXBMg+l5F5bjxzm9tnJdutdX/jaXc8+8pryz/8PldVWeBEIhEGBgayP7uui67v6yqZTHLFFVfQ0NDAN77xDQAOP/xwNC0dkTz66KPZtWsXnueh5LyAhnMczxefD2b45fNMIXPlF21hg57+JAc0BUmlbAD6EzZtYQOAnv4kjcF97z2Z58Yzt5k+K91urfsbT7vj2VdeW/7hl7mq6T04ixcvpqOjA4ANGzawYMGC7HOe5/GZz3yGQw89lG9961vZRc0NN9zALbfcAsBLL71Ee3t70cWNEEJkIs99CWtE5Llacehax6zr8Tgkai78oKopqi1btuB5HmvWrKGjo4M5c+bgui4XX3wxixYtym5/8cUXM2/ePFauXEksFkPTNL7+9a8zf/78ov1IikpUi8yVfxRKUd3/Qic3/XkbuwdSaKrCYdMjnHLY9LKj2PnSQkBJCaJKpZ/G0k7uPqauoiqQsNxsJP0Pr+7l+R29xG2XkKFx5IFNnPfO2RVPUQ3f7pz/O5e5EbPscyBqzy/vgzWNideKLHBEtchc+cvw+br/hU6u63iNgK4SMlTilstAymF6xGTe1AYiAY1o0iGacvjUMXML/lHPpIUiplbyPpXYd7xy+07ZDht3RgE4or2RuOWyqbMPTU3fHOx5kLBdDmwKcukJ8ys6tnznIOnCx985S6qX+4Bf3gdr+hGVEEJMpLXrdxDQVcJmOq0ZNjVcz6Mrmior+ePXpFFu39t7E4QMlZChsa0nQXc0heuB43oYmoqpp5/riVsVH1vecxCUtJWoDVngCCEmnb0DKULG0Lc31/WwbHfIY6MVmRxPYcqJLGqZ23emAGim+GcsZeORXuBkGJqCZTsVH1v+c6BLYU9RE7LAEUJMOlMaTOLW0MWMqioY+tC3vNGKTI6nMOVEFrXM7TtTADRT/DNs6iiApu4LcViOh6FrFR9b/nNgS2FPUROywBFCTDrLl8wkabvEUg6ely5+qSoK0yNmWckfvyaNcvue3RwkbrnELYc5rUHaIiaqkl7gWI5Lyk4/1xoyKj62vOcgIWkrURtyk3EN+eWGLSFz5Tf55uv+FzpZu34HewdSTGkwWb5kJvOnNowrjVSrek2VUEqK6m9dUcBj4YxGzn1H6QmqsY5DUlT+4pf3QUlR1QG//LIImSs/yY2JBw0V14OU7Y5pQVFuRfCxjvfmp7fnXVyMp8L4eBdTmf2fff1NdkctXM9jWmOA5UtmcvoR7RU5dpDXlp/4Za5kgVMH/PLLImSu/CITQ26NmMTiFi909gNw+IwIpq6VFcvOtOU4Llt74kD6i0kPOqABVVUqEu/e1NnHNY+9TGdfkpChDolon3nkDB7ZsjsbqX6jN8nmXVEWtDUwsyVYNGY+3kh6tnhmLMXLuwdQFAUFCJs6rufx+WUHVWyRI68t//DLXElMXAgx6eQW29zWkyBkaIQMle29ibJj2Zm2dsdSGFo6Wm7qGt3RVMXi3Q9s6qI3bhMy1BER7bXrdwyJVHdHUwR0ld2x1Kgx8/FG0jP7v96bRBscl6Yp2K5LQFdZu37HuI9diFqTBY4QwreGxKFTNoamoKsKscHkTjmx7ExbmVg1kI1WVyre3dmbIOW42fYzfVi2w96B1JBIdSyVXgjFclJIhcYx3kh6Zv+k7aANDk1FwXY8QobK3oFUOYcpRF2QBY4QwreGxKFNHcvxsF2P8OAf+3Ji2Zm2MrFqIButrlS8u705iKmp2fYzfRi6xpQGc0ikOmzqxC03eyzFjme8kfTM/gFdwxkcmouHrinELZcpDXJTsPCfkhY4e/fu5Yc//CFr1qxhy5Yt1R6TEEKUJLfY5pzWIHHLIW65zG4Olh3LzrQ1NWxiOeloecp2aIuYFYt3n7ZwOs2h9MJleER7+ZKZQyLVbRGTpO0yNWyOGjMfbyQ9s/+s5gDO4Lgcx0NXVZK2y/IlM8d97ELUWsGbjD3Py1bz/va3v8373//+7L/vuOOO2o2wCLnJWFSLzJV/SIpq6NglRSUqxS9zVegmY73QDl/4whc4++yzWbp0KaFQiKeffhpFUQgEAlUbpBBClGthexORxiC3/3nruBcCC9ubqv49NQvbm7jmfQsLPje8/9OPKL3d3H03dfZx1aN/L3nBk/tcpb63J9+5PrYlPOb2hChHwSs4juNwxx13sGHDBj7+8Y+ze/duEokExxxzDOFwffyCyhUcUS0yV/6xqbOPm55+nYDKqBHpiazwXUtjOc5Kn5tC7V160qHyRX8+4Zf3wbJj4pqmsXz5cr7xjW/w29/+lv/3//4fixYtqpvFjRBCwGDEOVhaRHoiK3zX0liOs9LnplB79z4rkXNRGwU/ovqP//gPOjo60DSN8847j0MOOYQf/vCHzJw5k8985jO1HKMQQhTU2Ztg5gFhbKu0OPW0xqFXD2pV4buWxnKclT43hdrbPvglikJUW8ErOI899hi//OUv+a//+i9+/etfM2vWLL7zne9wzDHH1HJ8QghRVDribA95rFpxar8Yy3FW+twUam92a2hM7QlRroILnOOOO46PfOQjnH/++Zx66qnZxxctWlSLcQkhRElOWzidaKK0iPREVviupbEcZ6XPTaH2zjxKIueiNqQWVQ355YYtIXPlN4++socb/t/LdEdTaKrCW6dF+MK75uW9OXYiK3wX6h/gv5/Zzqad/YDC26ZHOO+d46vuPZbjLDS2Yu0U6ycbu98VZSDl0GCoHDmnlfccfMCkuql7svLL+6AU26wDfvllETJXfrKps48fdrzG9r0xgrqKokDccmlvCrDyhIPr6g9pvmRRZ1+ChOXSE7fqbvyjJatKSV4N3ybpQU80NemSa5ORX94HpdimEGJSemBTFz0DKUKGhqmni1iGDJXeuF136ah8yaLeuM3OvmRdjn+0ZFUpyavh2zQFjUmZXBP1p6wFTmdnZ7XGIYQQY9LZmyBpuxjavgKWuqqQcty6S0flK4qZclxSjlOX4x+tiGcpRT7HWwhUiLEqGBPP+MUvfkFTUxN9fX3cc889LF26lMsvv7wWYxNCiFG1Nwd5vTeRLlo5uEiwXQ9TU+suHdXeHKQ3btEY3PfWa2oqpqbV5fjzjTc3WTXa86VuI0Q1jHoF5+GHH+aMM86go6OD3/72t/ztb3+rxbiEEKIkpy2cTmuDSdxySNnpIpZxy6U5pNddOipfsqg5pDOjKVCX4x8tWVVK8mr4Nn0Ja1Im10T9GXWBo6oqu3fvZurUqQAkEnJZUQhRPxa2N/G1f30bi2Y24XgetgtHHtg04Tfo5rOwvYlPHTOX5pDBrv4UzSGDlScczNdOWlCX48833tybg0d7Pt82U8Km3GAsamLUFNUPf/hDfvOb33DNNdfw0EMP0dzczGc/+9mijbquy6pVq9i8eTOmabJ69Wrmzp2bff7mm2/mwQcfBOBd73oXF110EYlEgpUrV7Jnzx4aGhq4+uqrmTJlStF+JEUlqkXmyl9aWsL88W87i0acTV1FVSBhja3SOBSORFejEvdofY234vlYIuHjHTvIa8tP/DJXFYmJW5aFYRijbvfwww/z2GOPcdVVV7FhwwZ+9rOf8dOf/hSA7du384UvfIFf/epXqKrKOeecw6pVq3jqqaeIRqN87nOf48EHH+TZZ5/lq1/96ijjkQWOqA6ZK3/ZGk3x/d9vHhJX3tmXxMOjvSlIynbYuDMKwBHtjRiaWnYhyUKR6PcsmMojW3bTG0vx8u4BFEVBAcKmjut5fH7ZQWUvckbry3Fctg6WPPA8j4MOaEBVlZKPJ1/7uedrPMU2R4uOy2vLP/wyV2OOia9YsYJzzz2Xc889l49//OOce+65o3a2fv16li5dCqS/+Xjjxo3Z52bMmMEvfvELNE1DURRs2yYQCAzZZ9myZTz11FMlHZgQQtz77I4RceWeuEVv3KYxqLO9N0HIUAkZGtt6EmMqJFkoEr12fbrv13uTaJqKqatomoLtugR0lbXryy8uOVpfu2MpDE0hbGqYukZ3NFXW8eRrP/d8jafY5v5S0FTUv1FTVN/85jeB9H8lbNq0qaSbjKPRKJFIJPuzpmnYto2u6xiGwZQpU/A8j+9973scdthhHHTQQUSjURob06uwhoYG+vv7R+1H0xRaWvxT3VzTVF+Nd38mc+Uvr7+ZYFpjAFXZF7W2XQ9FAdPUiVsuIUNDUSCWcjFNnVZDo6svWfI8d8cspjcN7aPV0Oh5vZfWxgBJ28XUFRRFQSO9wGkIaPTErbJ/l0brK76zf/B4FAKqRyzl0toYKPl48rWfe75y+yznHBUbe6YdeW35h9/natQFzrx587L/nj9/PnfdddeojUYiEQYGBrI/u66Lru/rKplMcsUVV9DQ0MA3vvGNEfsMDAzQ1DT6JVHH8Xxx+SzDL5f7hMyV38xqCdL1ZnxIFFlX0x8VpVI2IUMlZTuAQkhXSaVs+hM2bWGj5HluCxv09CeH9NGfsGkNpR8P6CqW66Kr4HoeuqowkHRoDZXeR6l9ZY7H0FQsxyOkq/T0J0s+nnzt556v3D7LOUfFxp5pR15b/uGXuRrzR1Tr1q3L/u+GG24gFhv9YBcvXkxHRwcAGzZsYMGCBdnnPM/jM5/5DIceeijf+ta30DQtu88TTzwBQEdHB0uWLBn9qIQQAjjzqJkj4sqtIYPmkE5/wmZ2c5C45RK3HOa0BsdUSLJQJHr5knTfs5oDOI5LynZxHA9dVUnaLsuXlF9ccrS+poZNLMcjlnJI2Q5tEbOs48nXfu75Gk+xzf2loKmof6PeZHzDDTdk/22aJqeccgqzZs0q2mgmRbVlyxY8z2PNmjV0dHQwZ84cXNfl4osvHlKV/OKLL+atb30rl112Gd3d3RiGwbXXXktbW1vRfuQmY1EtMlf+IikqSVGJyvPLXI0rRbVnzx6SyWT25wMPPLByIxsHWeCIapG58pdKz1c1K45Xuu2Jro5eLnlt+Ydf5mrMC5xvfvObPPHEE0ybNg3P81AUhTvuuKMqgyyXLHBEtchc+Usl56uUCtn10nY1x1ot8tryD7/MVaEFzqg3GT/33HM8+uijqKoUHhdCTH65MWcg+/8PbOoa96Kh0m1Xc6xC+N2oq5a5c+cO+XhKCCEms2pWv65021KpW4jCRr2C09nZyfHHH58ttVBPH1EJIUSlVbP6daXblkrdQhQ26gLn2muvrcU4hBCiLpy2cDo3/mkrwJD7Wj5ydPH06ES0Xc2xCuF3o35EpWkaV199NRdccAFr1qyhjNJVQgjhO6VUyK6Xtqs5ViH8btQrOF/96lc555xzeMc73sHTTz/NlVdeyS233FKLsQkhRE1s6uzj5qe387euKOCxcEYj575j9ri/Vyb3e2tyH//Kuw+p2NgXtjeVXGAzdxyHTY/wYlfUN/FyIco16hWcZDLJiSeeSFNTE+9+97uxbXu0XYQQwjc2dfZxzWMv8/wbfegqaIrChh19fP+xV9jU2VdyGzf+aSu9cYtpjSa9cYsb/7SV+1/ozPt4qe1WyvDxbdsb47qO19jeE5/QcQlRTaMucBzHYfPmzQBs3rwZJaeAmhBC+N0Dm7rojafrVRmD1cBDRrpI5niqc+dW/57oytrDx7c7liKgq3RHU1LxW0xaJX1EdcUVV7Br1y6mT5/Ot7/97VqMSwghaqKzN0HKcQkZ+/57z9AUYkm75Lh1Z2+CaY3mkMciAY29AymOPLBxxOO1jnEPH18s6RAyVGI5hTUlXi4mm1EXOIcddhh33303yWQSRVEwTXO0XYQQwjfam4Ns64ljux6Glr5CbTkehq6VHLcuFNee0mASTToTHuMePr5wQGMg6dBgSrxcTF4FP6J66aWX+NSnPsWVV17Jn/70J5YtW8bSpUu57777ajg8IYSortMWTqc5pBO3XKzBauBxy6E1ZIyrOndu9e+Jrqw9fHxTwyZJ26UtYkrFbzFpFbyCs2rVKj73uc/R29vLZz/7We69916mTJnCJz7xCc4444waDlEIIcavWFJq5QkHD3lu0cymESmq0Ypahg2VFzr7AIW3TY9k49rzpzaMqP6dudelVqmlTJw8M/45U8K8923ThqSoPnL0rIqOx29FQMXkU3CBYxgGxx57LAD//d//zVve8hYAwuFwTQYmhBCVkklKdfYlCRkqnpdOSu3qf4VLT5jPwvYmrnnfwqL7Z4pa5qaOPnVM+hveM8/901tas1+2l5H5o35jb4LpTemimLn713KRM7yv04+oTl/FztexLfI3RNRGwY+octNSuffduK5b3REJIUSFjTcpVSgl9cCmrqLPlbL/ZLS/Ha+oTwWv4Lz88stccskleJ435N+vvPJKLccnhBDjNt6kVKGUVGbfYs+Vsv9ks78dr6hPBRc4P/rRj7L//tCHPpT330II4QfjTUqNVtRytIKX+1tRzP3teEV9KrjAeec731nLcQghRNWctnA6L3X109mXBMDzIGG7HNgULCk5NFpRy9EKXu5vRTH3t+MV9WnUbzIWQgi/yySljjywCdsFx0snpTI3GJeyf6GilqUUvNzfimLub8cr6pPi+bg8uGU5vPlmbKKHUbKWlrCvxrs/k7nyl8x8VSOaXKzNWkWhJypyXYl+h8fzF81u5ZxF7bLY8QG/vA+2tTXmfVyu4AghJoVCBS/HU0CyWJvV6K/cMVRTJfrNV8h0/daesgqZCjFWssARQkwK1YgmjzceXgkTFbmuRL954/lmeYVMhRgrWeAIISaFzt4EkYA25LHxRpOLtVmN/sodQzVVot9MPF9X932vmqEpWLYjkXFRdbLAEUJMCu3NQaJJZ8hj440mF2uzGv2VO4ZqqkS/7c1BTE3Fdvfd6lluIVMhxkoWOEKISaFQwcvxFJAs1mY1+it3DNVUiX7zFjJNlVfIVIixkhRVDfnljnQhc+U3kqKqDklR7d/88j5YKEVVlQWO67qsWrWKzZs3Y5omq1evZu7cuUO22bt3L+eccw73338/gUAAz/NYtmxZtqjnokWLuOSSS4r2IwscUY5y3qzLnavR2q72H6hC7Q9/vDmg8fgre9k7kCJsajQFdXZFU8Qth6Cu8vaZzSydN4UXu6JDql8vmBbJe0z//cx2Nu3sJ1NB+7x3Fq7AHTRUXA9StkvSdunsSxBLOUxpMFm+ZCanH9E+ZPu45bArmmQguW8bgLXrd7B3IDVkv5aWMH/8284hf0hnNYdoDOqkbBdTV1EVSFhu9vwAo85JJectt6184ym0aDpsemRI1e+JrMpdifMh74P+4Ze5qukC5+GHH+axxx7jqquuYsOGDfzsZz/jpz/9afb5P/zhD1x77bVs27aNp556ikAgwNatW/nud7/LjTfeWHI/ssARpcqtbpz7zaqFvnysnLkare1y+67Usb1nwVQe2bI7+/jmrihbugdoChqYGuwZsLA90JT0jZ+eB6oCqqoypyXInpgFgOd5HHRAA6qqDDmm7z/2Cm/0JQjqKooCcculvSnAyhMOHnHcluPyQmc/AFPDOq/tjYOiMCWk46GQtF0+cOQMXtw1QMTU2B1NsHFnFEVROCBs4HrpcgiqAo1Bg5ChErfSC6XPLzuItx90AN/49cZstfCk5dKbsAiZOvOmBNn2ZvobjI9ob8TQVHb2JfHwaG8KFpyTSs5bblsp22HjzuiQ8WTaBYb0uePNBFu6Bzh0WoQDmwMV/90Z6zGM53zI+6B/+GWuavo9OOvXr2fp0qVA+krMxo0bh3aqqvzXf/0XLS0t2cc2bdpEV1cXK1as4JOf/CSvvvpqNYYm9lPVjNqO1na1Y76F2l+7fseQx1/vTaKpCrbrErPc7P6uB7qmoqkKluvheh6v9yYxNIWwqWHqGt3R1Ihj6olbhAwNU09HgEOGSm/cznvc23oShAyNkKHy2t4EmqpiqAoxyyVsagR0lbue25nd/pU9cXRNwdBUBlLpbWzPI+V4hE0NRVGy+61dv4N7n90xJI6cdFw0VcVxPF7ZEydkpKuHb+tJ0BjU6Ylb9MbtmlUAz21re29ixHgKRc93x1IEdJXuaGrCq3JLhXDhNwVrUY1HNBolEolkf9Y0Ddu20fV0d8cee+yIfdra2rjgggs4+eST+etf/8rKlSu5++67i/ajaQotLeHKDr6KNE311Xgnk+6YxfSmAKqyL67aamh09SXzzkk5czVa2+X2Xa5C7fe83ktr477Hk7aLqSnZREtmieMBiqKgquDa6Ss2SdvF1E0URSGgesRSLq2NgSHHZLseDQENSLdvKgpxy6E7Zo047rjtEjZVPA9s1yNoqHik/62qKg0B2BuzsuNNj1VFURVsJ72N56bHqqr7/rusIQA9cYvX30xgex4hI734yRTVtBwPy/YwdQ1FgVjKxTR1bNdDUcA09SHnLHdOKjlvQ86F5Q6Oc994Mu0CQ/qMWy4NAY245WbHWsnfnbEeQ8ZYxiLvg/7h97mqygInEokwMDCQ/dl13ezippDDDz8cTUt/58LRRx/Nrl278DwPJefFNJzjeL64fJbhl8t9k1Fb2KCnPzmkunF/wqYtbOSdk3LmarS2y+27XIXabw0NfTygqyRth4CeXiBYpBc5CulFjet6qEp6sRPQVFK2g6GpWI5HSFfp6U8OOaZXVIWk5eZU53bRFSXvcYf09MdG4KGr6YWHqoCuKriuSyzlEDa07PYBXcVyXVRXzW6jqKB46feTjNhgImdWS5BXuvqzY870oSkKhqaQsh1AIaSrpFI2uqqgAKmUXXBOKjlvQ86FoY4YT6ZdYEifIUNlIOnQYOrZsVbyd2esx5AxlrHI+6B/+GWuavoR1eLFi+no6ABgw4YNLFiwYNR9brjhBm655RYAXnrpJdrb24suboQoRzWjtqO1Xe2Yb6H2ly+ZOeTxWc0BHNdDV1XCxr6XvqqA7bg4roehKqiKwqzmAJbjEUs5pGyHtog54phaQwZxyyFlpyPAcculOaTnPe45rUHilkPccjloShDHdbFcj7ChEks5JG2Xs94+I7v9/ANC2I6H5bg0mOltdEXB1BRiKQfP87L7LV8ykzOPmjkkjhzQVBzXRdMU5h8QIm65xC2HOa3B7OKvOaQXnZNKzltuW7ObgyPGUyh6PjVskrRd2iJmTSPiox3DRI9FiFJUNUW1ZcsWPM9jzZo1dHR0MGfOHE488cTsdieccAK/+93vCAQC9Pb2snLlSmKxGJqm8fWvf5358+cX7UduMq5v5SQuahGDrVaKqtw0UTUSO/e/0Jk3XTSeFNWz23vYPWDjeh7TGgPZNjNjvfnp7fzv9jfpH/wyOF2FlpDJjEaTtsYArgd7oslsEqstYg5JUf1j7wD9SQdNVThseiOnHDaNP762N3semwMaA5aTTVH98/wpPPdGPy929eO46atKuqbguNDWFGDpW1p5dW+c53f0ErddDFUlEtA4IGxwQCSAqkB3NMVAyqHBULNjTNkjk0yVmJN8vyeSotr/3gf9zC9zVdMUVa3IAqd+lZO4qHbKaCxKnatKjX087VTj/BVrE9JJH8dx+Xt3lAHLBdfDG/x4Kzj4EZihqRw+I4Kpa6MmlN7oTbJ5V5QFbQ3MbAmOmkTbsivK5l0DNAY0mkMGSccjnnKGJLEKjbuefs/2R/vT+6Df+WWupJq4qKlyEhd+TmdUauzjaWeiikzujqWwBj/W8hQFSKee4ikH10vfP7K9N1FSQqk7mk4L7Y7lTwsN3377m+lEmOMxmKjSRySxJqo4phCiPsgCR1RFOYX6JqqYYCVUauzjaWeiikzGkg6OC4qSvknZ89I3Djseg/f6KMQGP74aPp7h7cdS6Yh3LKf2Ue4+w7dP2g7G4I3EGSFDJWbZE14cUwhRH2SBI6qinEJ9E1VMsBIqNfbxtDNRRSbDAQ1NBW/wKoqiKLiDXxyY/r4dj/DggmL4eIa3HzbTNwiHcxYgufsM3z6ga+mrR9q+IELccgkb+oQXxxRC1AdZ4IiqKCdx4ed0RqXGPp52JqrI5NSwmb6K4noongekU08hU0Md/Gbj2c3BkhJKbZF0WmhqOH9aaPj2s1vSiTBt8OpRLGWPSGJNVHFMIUR9kJuMa8gvN2xVSr2lqMpRboqqEmMfTzsTVWRyS1c/e2IWCTv93TQhQ2VKyBhTQmm0tFCxRFhbU4APLTowb3JsIopjisL2t/dBP/PLXEmKqg745ZfF7yqxsMqdK7/+USy1AOfwwpPDI8y5Cw9TV+lPWLzemwQ8Fs5o5Nx3zC4p6VXJc5jbXtJ26YomiCaGFu7M9dM/vMpdz+0kZtmEDZ2z3j6DTy+dN+b+xdjJ+6B/+GWuZIFTB/zyy+JnlYqnH/u2Gbz5ZqwuI+ylKLUAZzTp0NmXQEFhRlNgRCHIuOVm49shQ+XZHX3ErfS3BxuaSsJ2ObApyKUnzC+6iKzkOcxtb89Ako2d/SiKQmtO4c7PLzsou8j56R9e5ZZnXkdTlexHao7r8dF3zJJFzgSQ90H/8MtcSUxc7BcqHU/3a7S41AKcjUGd3rhNT9zKWwgyN769vTeB63nomkrC9jD19HY9cavo+aj0Ocxt7+Xd8XThTk0dUrhz7fod2e3vem4nmqpg6unaVqaeLix613M7x9S/EMIfZIEjJpVKx9P9Gi0uNO69A6kRj6ccF8tOp4tiSQddTddviqXsIfHtTCxcGyztAKQLWtpO0fNR6XOY217STo9XUchGxkOGyt6BVHb7mGVjqEPLvqQrmdsIISYvWeCISaXS8XS/RosLjXtKgznicVNTMfT0giEc0LBdD8vxCJv6kPh2JhbueKBrgwU7HQ9D14qej0qfw9z2Anp6vJ5HNjIet1ymNJjZ7cOGjuUO/SQ+XQerKrWGhRB1QhY4YlKpdDzdr9HiUgtw9idsmkM6rSEjbyHI3Pj27OYgqqJgOy5BXSFlu9n7cYqdj0qfw9z2Dp4aShfudNwhhTuXL5mZ3f6st8/AcT1Stos3+P+O63HW22eMqX8hhD/ITcY15JcbtvxOUlRpkqLaR1JU9UPeB/3DL3MlKao64Jdflv1V7h/NxpCBZTt5qz1Xsp/xVrHO910yf3h1L3/ripK7AIF9C5igoeb9jppCFcnLOa7RqqoPl9tn2NRobwrSE0+xO2qNqGKe+907A5aLAsQth4TlEDB13jatoeBiq9CiLt94c8+Vnxa0fiHvg/7hl7mSBU4d8Msvy/4oN3qcsh1e7BrA9TyOaG/E0NSKRcNLiUyXGqvOV5F7U2cfmppOKnkeJGyX1pBB0FBpbwpiOS4vdPYDDKn0fdi0Bu5+ficBXSVkqMQtd0TcerTj+v5jr/BGX4KgrqIMfpNxe1OAlSccnPe83f9CJ9d1vEZAV1Hw2Bu3sZ10PStNVVBIl3BwPS9bJdxxXLb2xLEcj764haKCqig0h3Qcl7yR9Xzns7MvQcJy6YlbQ8bbEtQJDS60/PS1AH4i74P+4Ze5kpi4EEXkRo+39yYIGlo2Kl3JaHglo+n5KnK7g4UuDU3Nxrh39iXpjds0BnW29SQIGdqISt93PZde3IRNbbA698i49WjH1RO3CBkapp6ObYcMld64XfC8rV2/I9tnzHKzSSfHIx3l1hRs1x1SJXx3LIUx+DgK4IGuKSRtr2BkPd/57I3b7OxLjhhvVzSVPVd++loAIcRIssARgqHR41jSwdD2RaWhctHwSkbT81Xk9kgvcDIMTSHlOKQGY92xlI2hKSMqfcesdBw81/C49WjHZdnOkOKXuqqQctyC523vQCrbp+V46arkOc+rKNiON6RKeCbGbg9Gwl0vvZ3luAUj6/nOZ8pxSTkjx2vZbvZcZfjhawGEECPJAkcIhkaPwwENy9kXlYbKRcMrGU3PV5FbIf3xTobleJiahjkY6w6bOpbjjaj0HTbScfBcw+PWox2XoWvZ76IBsF0PU1MLnrcpDWa2T0NT0lXJc5538dA1ZUiV8EyMXR9cmKhKejtDUwtG1vOdT1NTMbWR4zV0NXuuMvzwtQBCiJFkgSMEQ6PHs5uDJCwnG5WuZDS8ktH0fBW5M/evWI6bjXHPaArQHNLpT9jMaQ0St5wRlb7PevsMkrZLLOUMVuceGbce7bhaQwZxyyFlp2PbcculOaQXPG/Ll8zM9hk21Ox31WhK+gZox/HQVXVIlfCpYRNr8HE8QAHb8QjoSsHIer7z2RzSmdEUGDHe6REze6789LUAQoiR5CbjGvLLDVv7K0lRSYpKUlTVJ++D/uGXuZIUVR3wyy9LvanV99Dk9nPQtAjvOfiAmv1hK3aM5R5/se+/ufnp7UMWP8ceNGXEgujYg6Zkv/cmbjnsiiYZGPwW5H+eP4XepFORseQuVhpMjQXTIkUXe1t2RRlIOTQYKgumNw5p65GX9/Daruio3/czvO3hi7pyj0+UT94H/cMvcyULnDrgl1+WelKrat7D+0l60BNN1SQeXOwYgbKOv1gV8Xue76SzL0nIUPE8iCZtknY6pZSJlUeTNo4Hh02PYDnpyuKKonBA2CBhOfQnHQ6d1sCCaZFxjeWRLbuzkW8Az/M46IAGVFXJG5l3XY/X9gygKOl7b+a2htA0NdtWa8QkoFC0avrwsebG1NOJL6us4xNjI++D/uGXuZKYuPClWlXzHt5PU9CoWTy42DGWe/zFqoj3xtNJqUyE3PHA9rwhsXLHA8fz2B1L8cqeOLqmYGgqAykXx0vf37P9zeS4x5Ib+Q6bGqau0R1NFYzMd0dTmLpG2NQwNIXdsdSQtpqCxqhV04e3nRtTVxSl7OMTQtQ3WeCIularat4TWTW8WN/ljqtYFfGU46LnJKwc18N1h8bKHdfDcz1iyfRNxhoK6mD1cMvxMFSFpO0MaXssY8mNfAPZSH6hyHwm3g5kI+6FqqMXezy37dyYOlD28Qkh6psscERdq1U174msGl6s73LHVayKuKmp2DmLGU1VUNWhsXJNVVBUhXAg/UV/Dh7uYPVwQ1OwXI+Arg1peyxjyY18A9lIfqHIfCbeDmQj7oWqoxd7PLft3Jg6UPbxCSHqmyxwRF2rVTXv4f30JayaxYOLHWO5x1+sinhzKP1dN5kIuaaArihDYuWaApqiMDVsMv+AELbjYTkuDaaKpqSv8MxuCYx7LLmR71jKIWU7tEXMgpH5tohJynaIpRwsx2Nq2BzSVl/CGrVq+vC2c2PqnueVfXxCiPomNxnXkF9u2Ko3lUhRlZLaGZ6imtcS5I+v7WXDjj7ilkNQV3n7zOZs9DlfKikTU86NTFuOR1BXOSBsDEn/DB9foYh1Oamo4ZHwTHQ8cxwDKQfPc9P/ZaOoJOx9VzBUBQ6Z2sC/HXXgiBTVmzELTVVpDGoEdG1EkqnQOS92fkqdj2dff5PdUWvw24pVpkYMjprVMuQ83L6hkw3be8gX997S1c+emEU06WC5LiFd5ciZzSydN4XfvtjFxp1RLMcFD3K/6rAlqPO5EmtxidLJ+6B/+GWuapqicl2XVatWsXnzZkzTZPXq1cydO3fINnv37uWcc87h/vvvJxAIkEgkWLlyJXv27KGhoYGrr76aKVOmFO1HFjiiFJkkTimpnYyt0RSrfr2JbT1xEraDqoA3WCNpTmuI9x/ZPiKVlLBdDmwKcuaRM7j3+Z280ZdAVaAvkS6h0GCoHNIWQdPUUQtnlpJQuuaxl/P2n1tsMl8RzJ6YRdxyGf7C14CgqXHxP88b8kd9LEm28abfRktPDU9a3fT06wRU8qbQrnnsZba/mSBhOZnyVdm6V3NaQ+weSBFN2MRzvtU4s92BjSZrTjtMUlQVJO+D/uGXuappiurRRx8llUqxbt06LrnkEq666qohz//hD3/g/PPPp7u7O/vY7bffzoIFC7jttts444wz+MlPflKNoYn9UCaJU0pqJ+PeZ3fQE7ewPQ9dU9E1FU1VcD2P3ridN5WUKfa4dv2ObOHJpJ3e31DT93dk0j+lFIQcLaFUqP/hKaThRTBTjjdkcaMM/s8lnaAaXmBzLEm28abfRktPjUhaBQun0HrjdvpbkTUVQ1cHi3O6uB683pvE1DWSwxY3CukrWrsGRhbvFEL4g16NRtevX8/SpUsBWLRoERs3bhzyvKqq/Nd//Rcf+MAHhuzziU98AoBly5aVtMDRNIWWlnAFR15dmqb6aryTRXfMYnpTgPjOfkJGOhIcUD1iKZfWxgBdfckR8/L6mwls18MbXOAAqGr6Hg3b8xiIW4Pfn6Jlry4EVI+BpEMsbmFqKg0BDTuWrpvkDVb5jlv5+8yMUVX23fDbamh5x5bZ3va8vP13x6zsPt0xC9v1aAhoZCo9ue7QazfK4NUpD8Dz6Ilb4xrbWPfJt398Z5SwqQIKpjJYjmHY+euOWSNuBM70BYNReC8dhQfQUHA8F0Mh/T1AhjrkoylInwuV9Jzlnk8xfvI+6B9+n6uqLHCi0SiRSCT7s6Zp2LaNrqe7O/bYY/Pu09iYvszU0NBAf3//qP04jueLy2cZfrncN9m0hQ16+tMf5aRsJ1uYMaSr9PQnaQsbI+ZlVkuQl7v609+P4nrpoo6D/68rCuGQQcp2s+0BgzWSFBpMg6TtkrTSsWzH9cBL7xsy8veZGWNjcN9Lsj9h5x1bZvtXFSVv/7n7tIUNXlEVkpabjVmrqjJkkZP5kFoBUBRaQ+Mb21j3ybd/SFezY7ccN+/5awsb9CUsgjlpsExfAK8qClruPA7eUIwHgcH2VYbef5P5iEobdj7F+Mn7oH/4Za5q+hFVJBJhYGAg+7PrutnFTSn7DAwM0NQkn3mLysgkcUpJ7WScedRMWkMGuqJgOy624w7+gVRoDul5U0mZYo/Ll8zMFp4M6On9LTf9HSuZ9E8pBSFHSygV6n94Cml4EUxTU4ZU7fbYd8VCU5QRBTbHkmQbb/pttPTUiKRVonAKrTmko2mD82C7g8U5VVQFZjUHSNkOAW3fGcmcD9eDaQ0ji3cKIfyhKgucxYsX09HRAcCGDRtYsGBBSfs88cQTAHR0dLBkyZJqDE3shxa2N/GpY+YyZ0qY6RGTSEBnRlOQ2a2hgje9vn1WC5eeMJ+j5zQTCaTv7QibGktmt7DyhIM5/Yh2Vp5wMEce2ITtpu9dWTSziUtPmM/pR7Rz6QnzWTSzCU1ViAR02hpMZreEmDMlnLfPzBibQwa7+lM0h4yiN+QubG8q2H/uPgvbm7JjcTwP24V3zm3lY++cxczmAOkPf9IVvGc0B0bcYDyWsY11n3z7z24NMaMpSCSgMz1i5j1/C9ub+MKJB+ftK3OeFs9Kz6OqKkRMjXfMbeXi4+dzWHsTM5qCtLeEOCCsoQ++I6oqHNoWlhuMhfCxqqaotmzZgud5rFmzho6ODubMmcOJJ56Y3e6EE07gd7/7HYFAgHg8zmWXXUZ3dzeGYXDttdfS1tZWtB9JUQ1V7aKUue0Xqkg9njGUU4CxWjJj6I5ZtIWNEX3nFmdsCGhMiwQIGdqISt6W42aj4W2NAVwP9kSTeY9rtCrc5VTCHi1WnnncHLyCUY1q6RPBL5fShcyVn/hlrqTYZh2o5i9LtYtS5rZvOS4vdKbvkTp8RgRT10oucDha++VEuSst9xhbGwP09CeHjD+3OKOqwJ5Y+svlDp8RwdA0XtzZj6apBDSF3sFoeFDfd5FUV9N1nXKP6z0LpmYj5ZkYd9xyaW8KsPKEg4GRxTY7+xIkLJeeuDVin/cf2Z53DnLnJmWni2gCHNHeiKGpvi8q6Zc3YiFz5Sd+mSsptjnJVbsoZW7723oShAyNkKGyvTdRVoHD0dovJ8pdabnHqOYZf25xxoFU+kvndE3hlT1xdsdSuF76xvdEJhquKcRTDq6XvrE1Zbsjjis3Up6JcacrW9sFi232xm129iXz7lNoDnIf396bIGSkE2DbehJSVFIIMSnJAmeSqHaxyNz2M4UPM0UPM32VUuBwtPZLKcBYLaOdw9zijLbjoirpyHHSdoklHTzAcd3scyrpCtWO6+HkFLXMPa69Ayks28kmnCB9pSfluAWLbaYcl5STf59Sik9mznFmHMOPUwghJgNZ4EwS1S4Wmdt+pvBhpuhhpq9SChyO1n4pBRirZbRzmFucUdfS9yA5pBM54YCWvllXVbPPuaTjyJqqoOUUtcw9rikNJoauZQtJQrqYpKmpBYttmpqKqeXfp5Tik5lznBnH8OMUQojJQBY4k0S1i1Lmtj+nNUjccohbLrObg2UVOByt/XKi3JWWe4xunvHnFmdsMFUsJx05nn9AiKlhM31FR1MIZqLhjkfI1NJXcxQFU1dHHFdupDwT445bLs0hvWCxzeaQzoymQN59Cs1B7uOzm4PErXSsfE5rUIpKCiEmJbnJuIYkRVVa+5KikhRVufxyM6SQufITv8yVpKjqQK1/WUpZbFR7UVRp5Y53LMe3qbOPR17ew2u7otmFS6a6du4CYyznrdh4SlmYFFpYjqeP3GPx68LHL2/EQubKT/wyV7LAqQO1/GUpJTZe7Wh5pY2l4vZYq2C3RkwCCux4M8GW7gEOnRbhwOZANqatoDCjKVDWeSs2HhgZBx8e7y4Uzy91TvP1kXssfo6P++WNWMhc+Ylf5kpi4vuZUmLj1Y6WV9pYKm6PtQp2U9BAUdLVqwO6Snc0NSSm3RO3yj5vxcZT6LnceHeheH6pc1oocp45FomPCyEmE1ngTFKlxMarHS2vtHLHO5bjG75PLOkQMtRsnBrSMW3LHppUKuW8FRtPoeeGxLsLxPNLndNCkfPMsUh8XAgxmcgCZ5IqJTZe7Wh5pZU73rEc3/B9wgGNuOVm49SQjmkb+tCFQinnrdh4Cj03JN5dIJ5f6pwWipxnjkXi40KIyUQWOJNUKbHxakfLK20sFbfHWgW7L5EuwzA1bJK0Xdoi5pCYdmvIKPu8FRtPoedy492F4vmlzmmhyHnmWCQ+LoSYTOQm4xqqtxRVoXgyjC0hVKsxjzUhNNYUVXNA4/FX9vLGm3Fsz8N1wSP9P11VaA0ZBHWF3TELx/Voi5ic/3/mcPoR7dkxPbu9h90DNpbrYqgqUxt0jprdOmL8Nz+9nb91RQGPhTMaOfagKfz2xV1s3NmH5XioQIOpoWnpEg2zmtMR9Df6kkP2+eNre9mwo4+45RDUVd4+sznv3B42PcIfX9ub/R04sClAa9iQFJWoGpkr//DLXEmKqg7U0y9LobTNeApmVmtM5RTrrNS4M3OVabc3luLv3QPYRV4tpgaaomB76Y9+PrionRd3DdAbS/HynhgKoADhgI7renx+2UGcfkR7wWPY8WaCF7ui4HlYroeq7Cv7EAlozJ8a5pXdMWKWQ0tIx9Q0ErZLy+BNxPmKca484WDfpuiKqafXlihO5so//DJXkqISQ5SS2ql1smo8qa5qJcIy7b7em8QjvUApxPOU7JUVx/O467mdg/sm0FQwdRVNU7GddHmHtet3FD2G3bEUjueRdNLFO3VNxfNAUcHx4OXdcRwPdE0haXuYejoB1RVNFSzG6ecUnRBClEMWOPupUlI7uY/XQ7HLau1bSrtJ22G0a53u4AaqAp7rEbPswX1dtMGlkaqkC3WGDJW9A6mixxBLOniuhzt49SbdB3iDBTyTtoPjemgo2bpUhqZg2YWLcfo5RSeEEOWQBc5+qpTUTu7j9VDsslr7ltJuQNdQil2+IV1vCtKLEEVVCBv64L4q6Vrj6ed0TSVuuUxpMIseQzigoagKqqowWH8UVQFlsIBnQNfQVAUHL7uYsRwPQy9cjNPPKTohhCiHLHD2U6WkdmqdrBpPqqtaibBMu7OaAyhAsYs4iuLhOOnil5qicNbbZwzuG8Rx0+UVHMcd/EjJZfmSmUWPYWrYRFMUAlq6eKftuCgKeC5oChw8NYSmMPiRl0LKTiegpkfMgsU4/ZyiE0KIcshNxjVUbzdslVL7qN5SVNXad7jcucomoV5/k67+JAnLxSP9XwdNIYODpoTpT1hs702MmqJyPY9pjQGWL5k55AbjQseQSTnlJqLeMiWcTToFDZWemDUkRXXuO9JpqWIFPKtxziZSvb22RGEyV/7hl7mSFFUd8MsvS72YyD++LS1h/vi3nenq5ruidPYl6EtYOC4EDZUZjUEWzWrOW4gzM8bcyuNTGkz+ef4UepNO3gVlJh6esm3Cpk5Q1/CABkNlwfTGkgt+5nss36J1eDy80ALIL+S15R8yV/7hl7mSBU4d8MsvSz2Y6Ajz1miK7/9+M67r8eLOPqIpF9iXolIVmN0SoCfuDCnEmRnjK7sHuK7jNQJ6JsFk0Z90OHRaAwumRYbE8u95vpPOviSq4tGfSN847AFNQQNDUzggbPBGX3JIPzv7knh4tDcF8xbOLBb9f6M3yaad/agKNAb0gjFyP5HXln/IXPmHX+ZKYuLCVyY6wnzvs+m4fHc0RcL20FSy9+BoqgIK7OgdWYgzM8a163cQ0FXCpoaiKDheer/tbyZHxPJ74zYhQyVpe4Ntp9u3XRdDU3i9NzGin564RW/cLlg4s1j0vzuajp+7HkVj5EII4WeywBF1aaIjzNt74kQCGrFU+r6Z4TcYe146mTS8EGdmjHsHUoSMfS8vy/EwVIVkTpHOTCw/5bjoajrqrSjgeV66fcdDV9M3JA/vx7IdUo47ZMyFioAOj/7HUjae6+G4+44oX4xcCCH8TBY4oi5NdIR5dmuIaNIhbOqoijLiS/4UJb0oGF6IMzPGKQ0mcWvfAsTQFCzXI5BTpDMTyzc1FdtNR709DxRFSbevKdhu+ksBh/dj6BqmNvTlW6gI6PDof9jUUVQlfbVoUL4YuRBC+JkscERdmugI85lHpePybRGToK7gDNafUkh/yR4ezGweWYgzM8blS2aStF1iKQfP89AGyyzMbgmMiOU3h3TilktAVwbbTrevqyqW4zGrOTiin9aQQXNIL1g4s1j0vy2Sjp+rCkVj5EII4Wdyk3EN+eWGrXohKSpJUZVKXlv+IXPlH36Zq0I3Get5Hx0n13VZtWoVmzdvxjRNVq9ezdy5c7PP33nnndxxxx3ous6nP/1pjj/+eN58801OOukkFixYAMC73/1uPvrRj1ZjeCKPchYT5S48xrpQWdjeVNU/uKONK/PvB0injZK2y9aeAfoSDm/0JWjanb7ikfm+m/9+ZjuXPfAiuVW5ZzQGOGpWc96FRu4NvQc0mMw/IDxi8TGQUjhgIMX8qQ0jvjdnU2cfAP1Jm52v97Klqz+7GAKG9JHvXGbay4zpP/60laCh4nrpKzt+/l4cIYSoyhWchx9+mMcee4yrrrqKDRs28LOf/Yyf/vSnAHR3d3P++edz9913k0wm+fCHP8zdd9/NX//6V/7nf/6Hr33tayX3I1dwKqOcSHa58e2JjnsXMtq4MldwMtvsGUjy/Bv9OB6YKqiagu14zG4J8pGjZ3Pv8zt5oy9BUFdJOS5vxi1ChsbiWc0YmlqwUvvwuHemgrimKEQC2qiVwF3X47U9AyiDZSIykfIFbQ3MbAmWNT+W4/JCZz8Ah8+IYOpaXcxVKer1tSVGkrnyD7/MVU1j4uvXr2fp0qUALFq0iI0bN2afe/755znqqKMwTZPGxkbmzJnDSy+9xMaNG9m0aRMf+chH+PznP8+uXbuqMTSRRzmR7HLj2xMd9y6klHHlbvPy7jgo6RIJLgq6qqJrCruiFmvX76BncEFj6ipJO12OwfVgW0+iaKX24XHv3bEUrudhe15JlcC7oylMXSNsaoOR8iQBXWV3bGR0fbTzsK0nQcjQCBkq23sTdTNXQggxFlX5iCoajRKJRLI/a5qGbdvouk40GqWxcd9qq6GhgWg0yrx58zj88MM55phjuP/++1m9ejXXXXdd0X40TaGlJVyNQ6gKTVPrcrzdMYvpTYFssUiAVkOjqy85YrzlbDuW7WtltHFpmjpkm+TgXcaKAh4eiqKgK+mrNT1xC1NTaQhoQDr5pCsqjucRt11MU6fV0Oh5vZfWxqF92m46Gm4OJqTilkvmoqqqpv/7w1QU4pZDd8zKnrPM2OI7o4RNFVAwFYWkbTE1YhC33Gybpc5P3HYJmyqeB3HLyY57oueqFPX62hIjyVz5h9/nqioLnEgkwsDAQPZn13XRdT3vcwMDAzQ2NnLkkUcSCoUAeM973jPq4gbAcTxfXD7LqNfLfW1hg57+JI3Bfb8O/QmbtrAxYrzlbDuW7WtltHG1tISHbBPQVGKum41xe56H7bkYmkpryCBpuySt9Bfz6aqC5bpoikpIV0ml7GzyaXifuqqgAKnB77gJGSq9ioKiKLhuOmZuOS66ogw5Z5mxhXQ126/luAR0lYGkQ0NAy7ZZ6vxk2oL09/tkxj3Rc1WKen1tiZFkrvzDL3NV04+oFi9eTEdHBwAbNmzI3jgMcOSRR7J+/XqSyST9/f288sorLFiwgK9+9av8/ve/B+Cpp55i4cKF1RiayKOcSHa58e2JjnsXUsq4crc5eGoIPHA8UPGwXRfb8ZgWMVi+ZCatISNbvTugq9iOh6rAnNZg0Urtw+PeU8MmqqKgK0pJlcDbIiYp2yGWcgYj5QGStsvU8Mjo+mjnYU5rkLjlELdcZjcH62auhBBiLKpyk3EmRbVlyxY8z2PNmjV0dHQwZ84cTjzxRO68807WrVuH53lceOGFnHTSSWzfvp0rrrgCgFAoxOrVq5k2bVrRfuQm48qpxxRVtRUbV2aucrfJTVFpqsJbp0X4wrvmZdNRudW7MymqhOUWjWvni3aXGuHOtLVlV5SBlFM0Ul7q/Pg1RVXPry0xlMyVf/hlrqTYZh3wyy+LkLnyG5kv/5C58g+/zJUU2xRCCCHEfkMWOEIIIYSYdGSBI4QQQohJRxY4QgghhJh0ZIEjhBBCiElHFjhCCCGEmHRkgSOEEEKISUcWOEIIIYSYdGSBI4QQQohJRxY4QgghhJh0ZIEjhBBCiElHFjhCCCGEmHRkgSOEEEKISUcWOEIIIYSYdGSBI4QQQohJRxY4QgghhJh0ZIEjhBBCiElHFjhCCCGEmHRkgSOEEEKISUcWOEIIIYSYdGSBI4QQQohJRxY4QgghhJh0ZIEjhBBCiElHFjhCCCGEmHRkgSOEEEKISUef6AHUm/tf6OSnf3yNPQM2XpHtFCj6vBgfU1NIORN/ho+Y3sAlJx7CA5u62NLVz4Dl0mBqLJgW4bSF01nY3jRqG/e/0Ml//mUb3dEUmqowuznIrNYQCculvTnIaQun0/Hybu56bicxyyZs6Bwxo4HOqMXegRRTGkyWL5nJ6Ue0D2l3U2dfely7ogykHBoMlQXTG7Pjyjzf2ZvA1FVUhSF9ljJ2IYTwK8XzvIr/FXFdl1WrVrF582ZM02T16tXMnTs3+/ydd97JHXfcga7rfPrTn+b4449n7969XHrppSQSCaZNm8Z3v/tdQqFQ0X4sy+HNN2MVG/f9L3Tyvf95mWQd/GEV9aNBh8Pam9naEwfA8zwOOqABVVX41DFziy4U7n+hkx88/iopx0VXwPY8LAcaDJWj57RgaCp/29nPG31JDE3BUBUStovjQUhXmNYYIG65JG2Xzy87KLvI2dTZx41/2orrery2ZwBFUQCY2xpC01Tes2Aqj2zZTcTUSNkOG3dGATiivRFDU4mmnFHH7ictLeGKvheI6pG58g+/zFVbW2Pex6vyEdWjjz5KKpVi3bp1XHLJJVx11VXZ57q7u7n11lu54447uOmmm/jBD35AKpXiJz/5Caeeeiq33XYbhx12GOvWravG0Ipau34HduXXe8LnBmzYHUthaAphU8PUNbqjKSKmxgObuoruu3b9DhzPw9BUNE3F8xRUBZKOx7aeBI1Bna7+JIoCpq6iqAqZX8Gk7aEo6T4Dusra9Tuy7T6wqYuImR6HqWuETQ1DU9gdS49r7fodREyNxqDO9t4EIUMlZGjZPksZuxBC+FlVPqJav349S5cuBWDRokVs3Lgx+9zzzz/PUUcdhWmamKbJnDlzeOmll1i/fj0XXnghAMuWLeMHP/gB5513XtF+NE2hpSVcsXH3xC08t2LNiUkkbrmEDA1FUQioHrGUS2tjgK6+ZNHfwZ64BZ6HpqX/W8LDQwFczyNuu5imju2BppC9CpP5FXQBVU3v1xBIt5XpqztmMb0pQHxnlLCpAgqmohC3HFobA/S83ktrYwBVUXLGDrFUus9WQxt17H6iaeqkOZbJTubKP/w+V1VZ4ESjUSKRSPZnTdOwbRtd14lGozQ27ruc1NDQQDQaHfJ4Q0MD/f39o/bjOF5FL5+1hgz6Eta+vzBCDAoZKinbwdBULMcjpKv09CdpCxtFfwdbQwZxy8FxPVQFFBRcPFRFIaSrpFI2upL+lct8WqwyuLgh/XEvQCzl0Bra11db2KCnP0lIV0laLoamYDkuISM9rtZQ+vnGoJ4dO+zrsz9hjzp2P/HLpXQhc+Unfpmrmn5EFYlEGBgYyP7sui66rud9bmBggMbGxiGPDwwM0NRU+3sDli+ZiT74X9FCZDToMDVsYjkesZRDynZoi5hEUw6nLZxedN/lS2aiKenFh+O4KIqH60FAU5jTGqQ/YTO9MYDnQcp28VyPzK9gQFfwvHSfSdtl+ZKZ2XZPWzidaCo9jpTtEEs5WI7H1HB6XMuXzCSacuhP2MxuDhK3XOKWk+2zlLELIYSfVWWBs3jxYjo6OgDYsGEDCxYsyD535JFHsn79epLJJP39/bzyyissWLCAxYsX88QTTwDQ0dHBkiVLqjG0ok4/op0vn3gwUxt0RlvmyDKoukytPs7wEdMb+Pd/W8ScKWGmR0wiAZ0ZTUFmt4ZKukn39CPaufif5zEtYuJ4oKsqC6aG+T9vacVyPJpDBt859W187J2zCOoaScelwdQ5dm4z7c0heuM2kYA+5AZjgIXtTXzqmLnMbg0xoylIJKAzPWIyZ0qYTx0zl9OPaOdTx8ylOWRgu3DkgU0smtmU7XMy3WAshBD5VDVFtWXLFjzPY82aNXR0dDBnzhxOPPFE7rzzTtatW4fneVx44YWcdNJJ7N69m8suu4yBgQFaW1u59tprCYeLf/ZX6RRVtfnlcp+QufIbmS//kLnyD7/MVaGPqKqywKkVWeCIapG58heZL/+QufIPv8xVTe/BEUIIIYSYSLLAEUIIIcSkIwscIYQQQkw6ssARQgghxKQjCxwhhBBCTDqywBFCCCHEpCMLHCGEEEJMOrLAEUIIIcSk4+sv+hNCCCGEyEeu4AghhBBi0pEFjhBCCCEmHVngCCGEEGLSkQWOEEIIISYdWeAIIYQQYtKRBY4QQgghJh1Z4AghhBBi0tEnegB+duaZZxKJRACYNWsWH/zgB/nOd76Dpmkcd9xxXHTRRbiuy6pVq9i8eTOmabJ69Wrmzp3Lhg0bSt5WjN1zzz3H97//fW699Va2bt3KV77yFRRF4ZBDDuEb3/gGqqpyww038Pjjj6PrOldccQVHHnlkRbYV5cmdqxdffJELL7yQt7zlLQCcc845nHLKKTJXdcCyLK644gp27NhBKpXi05/+NAcffLC8tupQvrlqb2/ff15bnhiTRCLhve997xvy2Omnn+5t3brVc13X+8QnPuFt2rTJ+/3vf+9ddtllnud53rPPPut96lOfKntbMTb/8R//4Z166qne2Wef7Xme51144YXen//8Z8/zPO9rX/ua9/DDD3sbN270VqxY4bmu6+3YscN7//vfX5FtRXmGz9Wdd97p3XTTTUO2kbmqD3fddZe3evVqz/M8r6enx3vXu94lr606lW+u9qfXliyFx+ill14iHo9z/vnnc+655/LMM8+QSqWYM2cOiqJw3HHH8ac//Yn169ezdOlSABYtWsTGjRuJRqMlbyvGbs6cOVx//fXZnzdt2sQ73/lOAJYtW5Y958cddxyKonDggQfiOA579+4d97aiPMPnauPGjTz++OMsX76cK664gmg0KnNVJ9773vfyhS98AQDP89A0TV5bdSrfXO1Pry1Z4IxRMBjk4x//ODfddBPf/OY3ufzyywmFQtnnGxoa6O/vJxqNZj/GAtA0bcRjxba1bbs2BzQJnXTSSej6vk9hPc9DURSg8DnPPD7ebUV5hs/VkUceyZe//GXWrl3L7Nmz+fd//3eZqzrR0NBAJBIhGo3y+c9/ni9+8Yvy2qpT+eZqf3ptyQJnjA466CBOP/10FEXhoIMOorGxkTfffDP7/MDAAE1NTUQiEQYGBrKPu6474rFi2+a+6Yvxyf08uNA5HxgYoLGxcdzbivF5z3vew+GHH57994svvihzVUc6Ozs599xzed/73sdpp50mr606Nnyu9qfXlixwxuiuu+7iqquuAqCrq4t4PE44HGbbtm14nseTTz7J0UcfzeLFi+no6ABgw4YNLFiwgEgkgmEYJW0rKuewww7jL3/5CwAdHR3Zc/7kk0/iui5vvPEGrusyZcqUcW8rxufjH/84zz//PABPPfUUCxculLmqE7t37+b8889n5cqVnHXWWYC8tupVvrnan15bUk18jFKpFJdffjlvvPEGiqJw6aWXoqoqa9aswXEcjjvuOL70pS9lk1FbtmzB8zzWrFnD/Pnz2bBhQ8nbirF7/fXXufjii7nzzjt57bXX+NrXvoZlWcybN4/Vq1ejaRrXX389HR0duK7L5ZdfztFHH12RbUV5cudq06ZNfPvb38YwDKZOncq3v/1tIpGIzFUdWL16Nb/73e+YN29e9rErr7yS1atXy2urzuSbqy9+8Ytcc801+8VrSxY4QgghhJh05CMqIYQQQkw6ssARQgghxKQjCxwhhBBCTDqywBFCCCHEpCMLHCGEEEJMOrLAEUJUzM9//nOOO+44kslkVfv5y1/+wpe+9KURj997772ce+65rFixgg996EM8+eSTRds59thjqzVEIcQEk6/JFUJUzP33388pp5zCgw8+yPvf//6a9t3f389PfvITHnzwQUzTpKuri7PPPpvHH3984qsaCyFqThY4QoiK+Mtf/sKcOXP40Ic+xMqVK3n/+9/PihUreOtb38rf//53otEoP/7xj/E8j0suuYQZM2awfft2jjjiCL75zW9y/fXXM3XqVM455xxeeeUVVq1axa233spDDz3E2rVrsW0bRVG44YYb8vZvmiaWZXH77bdz/PHHM2fOHB599FFUVWXLli1cddVVOI5DT08Pq1atYvHixdl9n376aW644QY8z2NgYIBrr70WwzD49Kc/TUtLC//n//wf7rvvPn7/+9+jaRrXXHMNCxcu5JRTTqnV6RVClEn+s0YIURG/+tWvOPvss5k3bx6mafLcc88B6cKZN998M8ceeywPPvggAP/4xz/4zne+w69+9Ss6Ojro7u4u2O4//vEP/uM//oPbb7+dgw8+uODHToFAgFtuuYWtW7fyiU98guOPP5677roLgJdffpnLLruMW265hU9+8pPcc889Q/b9+9//zjXXXMOtt97Kv/zLv/DQQw8B0N3dzU033cRFF13EkiVLePLJJ3Ech46ODt797neP+5wJIapHruAIIcatt7eXjo4O9u7dy6233ko0GuWXv/wlkK5TBDBjxgx2794NwJw5c7IVidva2ores3PAAQdw2WWX0dDQwKuvvsqiRYvybtfV1UUikeDrX/86AK+99hqf+MQnWLJkCdOmTeMnP/kJwWCQgYGBIdWQAaZPn853vvMdwuEwXV1d2as7s2bNwjRNAM4++2xuvfVWXNflmGOOyT4uhKhPssARQozb/fffzwc+8AEuu+wyAOLxOCeeeCKtra15t1cUZcRjgUAgeyVn06ZNQPq+muuuu47HH38cgI997GMUqi6ze/duLr/8cm677TYikQgzZ86ktbUVwzD4zne+w/e//33mz5/Pddddx44dO4bs+7WvfY1HHnmESCTCZZddlu0j996do48+mjVr1nDXXXfxxS9+sfSTI4SYELLAEUKM269+9Su+973vZX8OhUL8y7/8S/YjolKcfPLJfPGLX+SZZ55h4cKFAEQiERYvXswHP/hBdF2nqamJXbt2MWvWrBH7L1y4kBUrVvCRj3yEYDCI4zjZj8xOP/10vvCFL9DU1MSMGTPo6ekZsu/pp5/O8uXLCYVCTJ06lV27duUd42mnncZDDz3EIYccUvJxCSEmhhTbFEKIEv3iF7+gpaWFs846a6KHIoQYhVzBEUKIEnzlK19h165d3HjjjRM9FCFECeQKjhBCCCEmHYmJCyGEEGLSkQWOEEIIISYdWeAIIYQQYtKRBY4QQgghJh1Z4AghhBBi0vn/zZsO/O+Y+N8AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 2. Salary vs Bonus % Scatter\n",
    "# ===============================\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.scatter(df[\"Annual Salary\"], df[\"Bonus %\"], alpha=0.6)\n",
    "plt.title(\"Annual Salary vs Bonus %\")\n",
    "plt.xlabel(\"Annual Salary\")\n",
    "plt.ylabel(\"Bonus %\")\n",
    "plt.grid(True)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a192fbae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Attrition Rate by Department:\n",
      " Department\n",
      "Marketing          0.125000\n",
      "Engineering        0.107595\n",
      "Human Resources    0.088000\n",
      "Finance            0.075000\n",
      "Accounting         0.072917\n",
      "Sales              0.071429\n",
      "IT                 0.066390\n",
      "Name: Exited, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# 3. Attrition Rate by Department\n",
    "# ===============================\n",
    "attrition = df.copy()\n",
    "attrition[\"Exited\"] = attrition[\"Exit Date\"].notna()\n",
    "dept_attrition = attrition.groupby(\"Department\")[\"Exited\"].mean().sort_values(ascending=False)\n",
    "\n",
    "print(\"Attrition Rate by Department:\\n\", dept_attrition)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "aafe25e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjgAAAFgCAYAAAC2QAPxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAli0lEQVR4nO3df1iUZb7H8c8wCAJChKmrIQWFpnVx1vSgFqutrVKeLPMYKi7l2q9Vy7A1RRS01FXXIls9lnI6WwdQwx+n7NSe8kelaZJZ4pEs0zqWoq2GbjC0gMNz/uhyNozVgeYH3PN+XddeF/PMzP18v97XNJ+9n2eex2ZZliUAAACDBPm7AAAAAE8j4AAAAOMQcAAAgHEIOAAAwDgEHAAAYBwCDgAAMA4BB0Cj6urqlJKSonvvvdej427YsEG9e/fWHXfcoTvuuEPDhg1TRkaG9u3b53rN/fffr0OHDl1wnPHjx6uioqLR5869v6SkRLfddluTa1y7dq2KiookSatXr9bKlSubPAYA/wr2dwEAWqZNmzape/fuKisr0+HDh3XVVVd5bOw+ffpoxYoVrsc7d+7UAw88oPXr1+vyyy9Xfn7+RcfYsWPHP3zu3Pu/+eabZtW3Z88eJSYmSpLGjBnTrDEA+BcBB0CjVq9eraFDh+qKK67Qiy++qCeeeEKStHLlSq1bt04RERHq06ePtmzZoq1bt6q2tlZPPvmkdu/eLafTqZ49e2rWrFlq167dRfd1ww03aPDgwVq9erWmTp2qQYMG6ZlnnlFCQoJmzJihI0eOKCgoSNdee62eeOIJzZw5U5J0zz33aOXKlRo7dqySkpL06aef6tFHH9WCBQv0zDPPSJKqq6s1efJkHTlyRFFRUXriiScUHx+vrKwsJSYmulaozj2Oi4vT1q1btWPHDrVt21YVFRU6ffq0cnNz9dlnn+mJJ57QmTNnZLPZNH78eA0fPlwlJSV6+umn1bVrV3322Weqra1Vbm6u+vXr56XZAXAxHKIC8COHDh3S3r17deutt2r48OF65ZVXdPr0aW3fvl0bNmzQunXrtGHDBjkcDtd7Vq5cKbvdrg0bNmjjxo3q2LGjnnzySbf3ec011+jgwYMNtm3atEkOh0OvvPKK1q1bJ0n66quvtGDBAknSiy++qM6dO0uSEhMT9ec//1mDBw9uMMbx48c1btw4vfLKK7rttts0bdq0C9YxePBgDRo0SOPGjdPYsWNd28+ePasJEyYoIyNDr776qvLz85WXl6ePPvpIkrRv3z6NHz9eL7/8skaOHKlly5a53TsAz2MFB8CPrF69WjfddJOio6MVHR2t2NhYvfTSSzp16pRuueUWRUVFSZLGjh2rXbt2SZLefvttVVZWaufOnZK+P4enffv2Tdpv27ZtGzzu3bu3nn76aWVkZOiGG27QPffcoyuuuKLR9/bp06fR7d27d9f1118vSbrzzjs1Z84cVVZWNqkuSfq///s/1dTUaMiQIZKkTp06aciQIdq+fbv69u2rLl26qEePHpKknj176r/+67+avA8AnkPAAdBAdXW1Xn75ZYWGhmrQoEGSpKqqKhUVFelf/uVf9MPb19ntdtff9fX1ys7O1sCBAyVJDodDNTU1bu93//796tatW4NtXbt21aZNm1RSUqJdu3bpN7/5jWbNmqVbbrnlR+8PDw9vdNygoIYL1TabTcHBwbLZbA16qauru2B99fX1P9pmWZbOnj0rqWE4O39sAL7HISoADbz66qu69NJLtX37dm3dulVbt27V5s2bVV1drZ49e+rNN990rYCcO2wkSSkpKSoqKlJtba3q6+uVk5OjvLw8t/b5zjvv6O2339aoUaMabF+1apVmzJihlJQUPfbYY0pJSdFnn30m6ftwdS5cXMinn36qAwcOSJJeeukl9e7dW2FhYbr00ku1f/9+SVJFRYU++OAD13saGzs+Pl5t2rTRm2++KUn6+uuv9cYbb+iGG25wq0cAvsUKDoAGVq9erd/85jcNVmeioqKUkZGhF198UWlpaRo1apTatm2rxMREhYWFSZImTpyoRYsW6c4775TT6VSPHj2UlZXV6D4++OAD3XHHHZK+X+3o2LGjnn/+eXXo0KHB64YPH673339fQ4cOVVhYmLp06aK7775b0vfnyqSnp2v58uUX7CchIUHLli3TV199pfbt22vhwoWSpIyMDE2dOlWpqamKjY1VcnKy6z0DBgzQ3LlzG4zTpk0bLV++XPPmzdPSpUvldDo1adIk9evXTyUlJe780wLwIZvFOioAN/3v//6vPvroI1fI+NOf/qTS0lItWbLEv4UBwHkIOADcVlVVpezsbH3++eey2Wzq3Lmz5s6dq06dOvm7NABogIADAACMw0nGAADAOF4LOKWlpcrIyJD0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ZVmWlZOTY7355pv+LNFjGuvV1Hm1LMuqra21Jk6caA0ZMsQ6dOiQsfN6fp8mz+nf/vY364477miw7fbbb7eOHDli1dfXW/fdd59VVlbmn+I8qLE+8/LyrP/5n//xT0FetGvXLuvBBx+0nE6nVVVVZf3xj3809rPaWK/++ryaEReb4ZZbbtEjjzwiSbIsS3a7Xfv379fbb7+tsWPHKjs7W1VVVX6u0jN+9atfae7cuZKk8vJyRUVFqayszPX/jAYMGKCdO3f6s0SPaaxXU+dVkhYtWqTRo0erY8eOkmTsvJ7fp8lz+sknn+i7777T+PHjdffdd2v37t2qra1VXFycbDabUlJSjJjX8/vcu3evysrKtH79eqWnp2vhwoU6e/asv8v0iHfffVfdunXTpEmT9Nvf/lY33XSTsZ/Vxnr11+c1YANORESE2rVrp6qqKk2ePFmZmZlKSkrStGnTVFRUpK5du+rf/u3f/F2mxwQHB2v69OmaO3euhg0bJsuyZLPZJH3/b1FZWennCj3n/F5NndcNGzYoJibGdS83SUbOa2N9mjqnktS2bVvde++9ev755/X4449rxowZCgsLcz1vyrye3+fUqVPVt29f5eTkqKioSNXV1VqzZo2/y/SI06dPa//+/XrmmWdcvZr4WZUa79Vfn9eAPQdHko4fP65JkyYpPT1dw4YN07fffquoqChJ0uDBg10rAaZYtGiRpk6dqrS0NNXU1Li2OxwOV9+m+GGva9asUadOnSSZNa/r16+XzWbTe++9pwMHDmj69OmqqKhwPW/KvDbW57PPPqsOHTpIMmtOJSk+Pl5XXHGFbDab4uPjFRkZqTNnzrieN2Vez+8zOjpat912m+v8m5tvvllvvPGGn6v0jOjoaCUkJCgkJEQJCQkKDQ3ViRMnXM+bMqdS473edNNNat++vSTffl4DdgXn1KlTGj9+vB577DGNHDlSknTvvfdq3759kqT33ntP1157rT9L9JiXX35ZK1askCSFhYXJZrPpuuuuU0lJiSRp27Zt6tOnjz9L9JjGen3ooYeMnNeioiIVFhaqoKBAPXr00KJFizRgwADj5rWxPidOnGjknErSunXrtHDhQknS119/re+++07h4eH68ssvZVmW3n33XSPm9fw+Kysrddddd7m++E2a1969e2v79u2yLMs1p/379zfusyo13usDDzzgl89rwF7JeN68efrzn/+shIQE17bMzEwtXrxYbdq00WWXXaa5c+e6zvBvzaqrqzVjxgydOnVKZ8+e1f3336+rrrpKOTk5qqurU0JCgubNmye73e7vUn+yxnrt3Lmz5s6da9y8/lBGRobmzJmjoKAgI+f1nHN9/u1vfzN2TmtrazVjxgyVl5fLZrNp6tSpCgoK0u9//3s5nU6lpKRoypQp/i7zJ2usz+rqai1ZskRt27bVVVddpVmzZqlNmzb+LtUj/vCHP6ikpESWZWnKlCmKjY019rN6fq8xMTF++bwGbMABAADmCthDVAAAwFwEHAAAYBwCDgAAMA4BBwAAGIeAAwAAjEPAAdCi5efnKyUlpcHFKQHgYgg4AFq0jRs3aujQoXrttdf8XQqAViSgb9UAoGUrKSlRXFycRo8erccee0wjRozQvn379PjjjysiIkLt27dXaGioFi5cqIKCAv33f/+3bDabhg4dqrvvvtvf5QPwI1ZwALRYa9eu1V133eW6t01paalmz56thQsX6j//8z8VFxcnSTp06JBef/11rVq1SkVFRdq8ebM+//xzP1cPwJ9YwQHQIv31r3/Vtm3bVFFRoYKCAlVVVamwsFB/+ctflJiYKOn7+968/vrrOnjwoMrLyzVu3DjXe48cOdLgViwAAgsBB0CLtHHjRv3rv/6rpk+fLkn67rvvdPPNN6tt27Y6dOiQrr76apWWlkqSEhISdPXVV+vf//3fZbPZ9MILL6h79+7+LB+AnxFwALRIa9eu1R/+8AfX47CwMA0ZMkSXXXaZsrOzFR4erjZt2qhTp0665ppr1L9/f40ZM0a1tbVKSkpSp06d/Fg9AH/jZpsAWpWioiLdeuutiomJ0dNPP602bdrooYce8ndZAFoYVnAAtCrt27fX+PHjFR4ersjISC1cuNDfJQFogVjBAQAAxuFn4gAAwDgEHAAAYBwCDgAAMA4BBwAAGIeAAwAAjPP/ExYiwz8XjtsAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 4. Histogram of Ages\n",
    "# ===============================\n",
    "plt.figure(figsize=(8, 5))\n",
    "df[\"Age\"].plot(kind='hist', bins=10, color='slateblue', edgecolor='black')\n",
    "plt.title(\"Age Distribution\")\n",
    "plt.xlabel(\"Age\")\n",
    "plt.ylabel(\"Frequency\")\n",
    "plt.grid(True)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "079829ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Extract hire year\n",
    "df[\"Hire Year\"] = df[\"Hire Date\"].dt.year\n",
    "\n",
    "# Average salary by hire year\n",
    "salary_by_year = df.groupby(\"Hire Year\")[\"Annual Salary\"].mean()\n",
    "\n",
    "# Plot it\n",
    "salary_by_year.plot(kind=\"line\", marker=\"o\", title=\"Average Salary by Hire Year\", figsize=(8, 5))\n",
    "plt.xlabel(\"Hire Year\")\n",
    "plt.ylabel(\"Average Salary\")\n",
    "plt.grid(True)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "19f12aa3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create age groups\n",
    "df[\"Age Group\"] = pd.cut(df[\"Age\"], bins=[20, 30, 40, 50, 60, 70], labels=[\"20s\", \"30s\", \"40s\", \"50s\", \"60s\"])\n",
    "\n",
    "# Prepare attrition data\n",
    "df[\"Exited\"] = df[\"Exit Date\"].notna()\n",
    "\n",
    "# Create a pivot table\n",
    "pivot = df.pivot_table(values=\"Exited\", index=\"Age Group\", columns=\"Gender\", aggfunc=\"mean\")\n",
    "\n",
    "# Heatmap\n",
    "plt.figure(figsize=(6, 4))\n",
    "sns.heatmap(pivot, annot=True, cmap=\"Reds\", fmt=\".2f\")\n",
    "plt.title(\"Attrition Rate by Age Group and Gender\")\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25e469e9",
   "metadata": {},
   "source": [
    "# Export Filtered Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d002717b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exported exited employees to Exited_Employees.xlsx\n"
     ]
    }
   ],
   "source": [
    "# Filter employees who exited\n",
    "exited_df = df[df[\"Exited\"] == True]\n",
    "\n",
    "# Export to Excel\n",
    "exited_df.to_excel(\"Exited_Employees.xlsx\", index=False)\n",
    "\n",
    "print(\"Exported exited employees to Exited_Employees.xlsx\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5f1219c",
   "metadata": {},
   "source": [
    "# PREDICTIONS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "362f5f52",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Prepare the data (clean, encode, handle missing values)\n",
    "\n",
    "#Train a model (Logistic Regression or Random Forest)\n",
    "\n",
    "#Evaluate accuracy\n",
    "\n",
    "#Predict on current employees"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "39474412",
   "metadata": {},
   "outputs": [],
   "source": [
    "#✅ Code to Build an Attrition Prediction Model:\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "e7796f77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fill missing values and create target\n",
    "df[\"Exited\"] = df[\"Exit Date\"].notna().astype(int)\n",
    "df[\"Bonus %\"] = df[\"Bonus %\"].fillna(0)\n",
    "df[\"Tenure (Years)\"] = (df[\"End Date\"] - df[\"Hire Date\"]).dt.days / 365"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "50b6ec02",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Select relevant features\n",
    "features = [\"Age\", \"Annual Salary\", \"Bonus %\", \"Tenure (Years)\", \"Gender\", \"Department\"]\n",
    "df_model = df[features + [\"Exited\"]].dropna()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "da03767f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Encode categorical features\n",
    "df_model_encoded = df_model.copy()\n",
    "label_encoders = {}\n",
    "for col in [\"Gender\", \"Department\"]:\n",
    "    le = LabelEncoder()\n",
    "    df_model_encoded[col] = le.fit_transform(df_model_encoded[col])\n",
    "    label_encoders[col] = le"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "881e88c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Train/test split\n",
    "X = df_model_encoded.drop(\"Exited\", axis=1)\n",
    "y = df_model_encoded[\"Exited\"]\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "f583d114",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(random_state=42)"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Train Random Forest model\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "0c693244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0       0.97      1.00      0.99       187\n",
      "           1       1.00      0.62      0.76        13\n",
      "\n",
      "    accuracy                           0.97       200\n",
      "   macro avg       0.99      0.81      0.87       200\n",
      "weighted avg       0.98      0.97      0.97       200\n",
      "\n",
      "Confusion Matrix:\n",
      " [[187   0]\n",
      " [  5   8]]\n"
     ]
    }
   ],
   "source": [
    "# Predictions and evaluation\n",
    "y_pred = model.predict(X_test)\n",
    "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
    "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b84e2cd3",
   "metadata": {},
   "source": [
    "# 1. Feature Importance (Random Forest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "058ddf19",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import matplotlib.pyplot as plt\n",
    "# Get feature importances from model\n",
    "importances = model.feature_importances_\n",
    "feature_names = X.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "53cc2f83",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjgAAAFgCAYAAAC2QAPxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAA0FUlEQVR4nO3deVhV5f7//9feG1AmRRSn0o5Dapmk5ifnyhwK00w7opKkecxz/DZpWmimOUc4VRo2aGk4lTnkSet0HFIzpxzTtBxyTGVQFFBA2PfvD4/7J4moW2Tj8vm4rq7LvfZa9/1e7w3xYq3FWjZjjBEAAICF2D1dAAAAQH4j4AAAAMsh4AAAAMsh4AAAAMsh4AAAAMsh4AAAAMsh4AD5oHr16mrbtq3atWvn+m/QoEFuj7d9+3YNGTIkHyu8XPXq1XXy5MmbOkdu5s6dq5kzZxb4vNdi27ZtevDBB+V0Ol3L+vXrp/vuu0+pqamuZcOGDVNMTIzmz5+vf/7zn9c9z5tvvqkdO3Zctnz9+vUKDQ11fQ21bdtWnTp10sqVK6841qBBg/TTTz9ddw3Xa/ny5apevboWL16cY/lfv1Z79Ohxxa+r559/Xnv37r1svUuXA/nFy9MFAFYxffp0BQcH58tYe/fu1YkTJ/JlrMJm06ZNuvvuuz1dRq5q1aolm82m3377Tffcc4+ysrK0bt061a9fX6tXr1ZYWJgkae3atRo+fLiOHDni1jw//fSTOnXqlOt7FStW1Ndff+16vXv3bv3jH/9QbGys7r///svWHzVqlFs1XK/Zs2erbdu2mj59up544gnX8r9+ra5Zs+aKY3zyySe5rnfpciC/EHCAm2zfvn0aNWqUkpOTlZ2drcjISP3973+X0+nU6NGjtW3bNqWlpckYo5EjR6p8+fJ6//33lZKSooEDB+qpp57SiBEj9M0330i68Fv+xdcTJ07U1q1bFR8fr+rVq2vs2LGaPHmyvv/+ezmdTt1xxx166623VKZMmSvWd+TIEXXr1k0NGjTQ1q1blZWVpddff11ffPGF9u/fr/vuu0/jx4/Xn3/+qcjISD344IPavXu3jDEaMmSI6tWrp/Pnzys6Olpr166Vw+FQaGioBg4cqICAAD366KMKDQ3Vb7/9pldffVXLly/XmjVrVLRoUT322GMaMmSIkpKSlJCQoDvuuEPvvvuuSpYsqUcffVTt27fX2rVrdezYMYWFhen111+XJH311Vf67LPPZLfbVaJECb3zzjsqV66cli9frsmTJ+v8+fMqWrSooqKiVKdOnWv+rOx2u5o0aaL169frnnvu0aZNm1S9enU9/vjjWr58ucLCwnTixAklJSWpbt26OnLkiBISEtSrVy8dO3ZMDodD48aNU5UqVbR161aNGTNGmZmZSkhIUKNGjTR69GhNmDBB8fHx6t+/v2JiYnINLZeqUaOGIiMjNW3aNE2YMEGRkZEqXry49u/fry5duuj777/XM888o19//VWpqamuoymrVq3SxIkTNXfuXG3evFljx47VuXPnZLPZ9NJLL6lZs2ZKSEhQVFSUTp06JUl6+OGH1adPn8tqOHz4sNavX68VK1aodevW2rJli+rUqaNjx47l+Fq9qFu3bvr444/1zDPP5Pjs3377bb333nuaNWvWZeu99957qlWrlr744gvFxcXJbrerVKlSGjx4sCpVqqQBAwYoICBAv/32m44fP67KlStr/Pjx8vf3v+bPF7cZA+CGVatWzbRp08Y8+eSTrv8SExPN+fPnTevWrc2OHTuMMcacOXPGhIWFmS1btpjNmzebl156yWRnZxtjjPnoo4/MP//5T2OMMfPmzTO9evUyxhizbt0688QTT7jmuvT1+++/bx577DFz/vx5Y4wxCxYsMH369HG9njNnjunZs+cVa05KSjKHDx821apVM0uXLjXGGDNkyBDTrFkzk5KSYtLT003jxo3Npk2bXOstWrTIGGPMDz/8YBo3bmwyMzPNe++9Z1588UWTmZlpsrOzzYABA8zgwYONMcY0a9bMTJo0yTVvVFSUmTJlijHGmGnTppmPPvrIGGOM0+k0PXv2NFOnTnVtFx0dbYwx5vjx46ZWrVrm0KFDZteuXaZ+/frmzz//NMYY89lnn5nBgwebP/74w7Rp08acPHnSGGPM77//bho3bmzS0tKu67NcuHCh6d27tzHGmLfffttMnz7dnDhxwtSvX99kZWWZBQsWmFdeecX1OdWrV88cOHDAGGPMiBEjzMCBA40xxvTt29esW7fOGGNMamqqqV+/vvnll19c+7Z9+/bL5v7rZ33RihUrTOvWrY0xxnTt2tU1x8XX3377rTl06JCpX7++ycjIMMYY88orr5gvv/zSJCcnm1atWpnDhw+7evnQQw+Zo0ePmkmTJrk+p7S0NNOnTx9z5syZy+aPiYkxL730kjHGmKFDh7r2/2IPLn6tGvP/f11d3M9LP/tL9/uv623fvt389NNPpkWLFq7l8+bNM2FhYcbpdJqoqCjTqVMnk5GRYTIzM81TTz1lvvrqq8tqBS7iCA6QT3I7RbV3714dOnRIb7zxhmtZenq6fv31V0VERKh48eKaM2eO6zdkd34brV27try8Lnwrr1ixQr/88ouefvppSZLT6dS5c+euOoa3t7ceffRRSRdOkdSpU0cBAQGSpNKlS+v06dMqXbq0ihcvrrZt20q68Nu+w+HQb7/9plWrVqlv377y9vaWJEVGRuqFF15wjV+vXr1c5+3WrZt+/vlnffbZZzpw4ID27NmT44hG8+bNJUllypRRyZIldfr0aW3cuFFNmjRRuXLlJEndu3eXJM2cOVPx8fGu15Jks9l06NAh1ahR46o9uKhp06YaPXq0nE6nVqxYoSlTpqh06dIqX768duzYoXXr1umRRx5xrR8aGqq77rpLknTPPffov//9ryQpOjpaq1at0ocffqj9+/crPT1dZ8+eveY6LmWz2VS0aFHX69z6WaFCBdWoUUPLly9Xw4YNtXbtWo0aNUo///yzEhIScnweF0/DNW3a1HX0qVGjRurXr58CAwNzjJuZmal58+Zp9OjRkqT27durS5cuOnbsmOszyMuVPvvcrF69Wq1bt3Z9H3Xo0EGjRo1ynQps2rSpfHx8JEnVqlXT6dOnr3ls3H4IOMBNlJ2drWLFiuW4piIxMVGBgYH64YcfNGrUKD333HNq3ry5KleurEWLFl02hs1mk7nkkXHnz5/P8b6fn5/r306nUz179lRERISkCz+cruWHgLe3t2w2W47XuXE4HDleO51OORyOHBflXlx+aZ2X1nipMWPGaPv27Xr66adVv359ZWVl5djXIkWKuP59sQ8OhyNHrenp6Tp69KicTqcaNmyod9991/XesWPHVLp06Rxzzp49W3PmzJEk3XfffZddwxIcHKwKFSro+++/l8PhUIUKFSRJjzzyiDZt2qQNGza4TpVJcoXLS2uUpGeeeUY1atRQ06ZNFRYWpm3btuXYt+vxyy+/qFq1aq7XV+pnx44dtXDhQiUlJally5by9/dXdna2qlSporlz57rWO3HihIKDg+Xt7a1ly5Zp7dq1WrdunTp27KgPPvhAdevWda377bff6syZMxoxYoRGjhzp2s+4uLgcfbiSK9Wam9z6Y4xRVlaWJOUIeX/9vgD+ir+iAm6iSpUqqUiRIq6Ac+zYMbVp00Y7duzQmjVr1KxZM0VERKhWrVpaunSpsrOzJV0IEhf/px4cHKw///xTSUlJMsZo6dKlV5yvSZMm+uqrr1x/8fPee+9d0w+ha3Xy5EmtWrVK0oW/qvH29la1atXUtGlTzZkzR+fPn5fT6dTMmTPVuHHjXMe4dN9+/PFHdevWTU899ZRKliypn376ydWDK6lfv77Wrl2r+Ph4SdKcOXM0ZswYNWjQQGvWrNG+ffskSStXrtSTTz6pjIyMHNt36dJFX3/9tb7++usrXqD70EMPKTY2NseRmkceeURff/21SpUqddWLyU+fPq0dO3aof//+atWqlU6cOKFDhw65guClPbia7du3a/bs2erWrdtV123ZsqV27typL7/8UuHh4ZIuHOE7ePCgNm7cKEnatWuXHnvsMcXHx2vs2LGKjY1VixYtNGjQIFWtWlUHDhzIMebs2bP1r3/9SytWrNDy5cu1fPlyDR06VHPnztXZs2cv25dr3bfc1mvSpImWLFni+uuqefPmKSgoyHWEDLgeHMEBbiIfHx/FxsZq1KhRmjJlirKysvTKK6/ogQceUFBQkPr376+2bdvK4XCoXr16rouD69Spo3fffVcvvPCCPvjgA3Xu3FlPP/20QkJCcvzQ/auOHTvqxIkTCg8Pl81mU7ly5RQdHZ1v+3MxrI0dO1ZFixbVBx98IIfDod69e+udd97RU089paysLIWGhmrw4MG5jvHQQw9pxIgRkqQXXnhBMTExio2NlcPhUN26dXXo0KE8a6hevbpee+019ezZU5IUEhKi0aNHq0yZMho+fLheffVVGWPk5eWlyZMnX9cRhEtr/OCDD3LsQ61atZSYmOg6OpaX4sWLq1evXmrfvr2CgoJUokQJ1a1bVwcPHlTDhg3VokUL9e3bVyNHjlSTJk1ybHvo0CG1a9dO0oWLngMCAjR27NhrOs3m4+Oj1q1b66efflJoaKikCwH5/fffV0xMjDIyMmSMUUxMjO644w5169ZNAwYMUJs2beTj46Pq1aurTZs2rvF2796tXbt2KTY2Nsc8Tz31lCZPnqwFCxaoadOmOb5WW7ZsqYiIiMu2+avc1mvcuLG6d++ubt26yel0Kjg4WB999JHsdn4Xx/WzGY7xAbgGR44cUdu2bbVlyxZPlwIAV0UsBgAAlsMRHAAAYDkcwQEAAJZDwAEAAJbDX1HdoAv3aHBefUXk4HDYlJ3N2dHrRd/cQ9/cQ9/cQ9/c427fvL0duS4n4NwgY6TkZPfuTno7Cwryo29uoG/uoW/uoW/uoW/ucbdvISGBuS7nFBUAALAcAg4AALAcAg4AALAcAg4AALAcAg4AALAcAg4AALAcAg4AALAcAg4AALAcAg4AALAcAg4AALAcAg4AALAcAg4AALAcHrZ5g2w2c8UHfRUWTudZJSVle7oMAAAKDAHnBtlsdkk2T5eRJ7vdSErxdBkAABQYTlEBAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLIeAAAADLuSkBZ/369WrYsKEiIyPVtWtXde7cWUuWLLkZU2nGjBk3ZdyNGzdq9+7dN2VsAABwc920IzgNGjRQXFycZsyYoalTp2rKlCnatWtXvs8zefLkfB9TkubNm6f4+PibMjYAALi5vApiEn9/f3Xq1EnfffedlixZop9//llOp1Pdu3dXWFiYIiMjValSJf3xxx8yxmjChAkKDg7WkCFDdPz4ccXHx+vRRx9V3759NWDAACUnJys5OVkPP/ywTp8+raFDhyo0NFQrVqxQenq6EhIS9Oyzz2rZsmXas2ePXn/9dbVo0ULffvutpk2bJrvdrgceeED9+/fXxIkTdeTIESUlJenPP//UwIEDVaJECa1evVo7d+5U1apVVb58+YJo000VFOTn6RJycDjsha6mWwF9cw99cw99cw99c09+961AAo4klSxZUp9++qnuvfdezZ49WxkZGQoPD1fjxo0lSXXr1tXw4cM1c+ZMffTRR+revbtq166tjh07KiMjQw899JD69u0r6cLRoe7du0u6cIpq6NChmj9/vtLS0vTpp59q8eLFmjZtmr788kutX79en3/+uerVq6eJEydq3rx58vX11WuvvaY1a9ZIknx8fDRlyhStWbNGn376qaZOnaqmTZuqdevWlgg3kpScfNbTJeQQFORX6Gq6FdA399A399A399A397jbt5CQwFyXF1jA+fPPP9W2bVstWrRIkZGRkqSsrCwdPXpU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MGCAJGn+/Pnav3+/+vfvXyBF/dXWrVvl5eWlcuXKafTo0XrzzTe1YMEC2e12DR48WNHR0fL398+3+YoWLao6depo4cKFat++fb6NCwAACkaeASc358+f11tvvaWDBw/K6XSqT58+ql+/vtq2basHH3xQv/32m2w2m2JjY/Xrr79qzpw5mjBhgiSpcePGWrNmjQYMGKDk5GQlJyfro48+0pQpU/Tzzz/L6XSqe/fuCgsLyzFnXFycnnvuOUnSgw8+qIcffliTJk2Sr6+vmjdvrvvvv18bNmzQhAkT5HA4VKFCBQ0fPlwZGRkaNGiQUlJSFB8fr4iICEVERCgyMlLBwcE6ffq0hgwZojfeeENeXl5yOp0aN26cypUrp7CwMPXs2ZOAAwDALei6A87cuXNVokQJjR49WqdOnVLXrl21ePFipaWl6YknntDgwYPVr18/rVq1SqVKlbriOA0aNFD37t21cuVKHTlyRLNnz1ZGRobCw8PVuHFjFStWzLXuhg0b9Pbbb7te9+3bV+Hh4SpRooSmTp0qY4wGDx6sWbNmqWTJknr33Xe1YMEC1axZU0888YRatWqlEydOKDIyUhEREZKkNm3aqGXLlpo5c6ZCQ0P12muv6eeff1ZKSorKlSun4sWL69SpU0pJSVFgYOD1tgkAAFwiKMgvz/cdDvtV17ke1x1wfv/9d23atEnbt2+XJGVlZenkyZOSpHvvvVeSVK5cOWVkZFy27aXXtFSqVMk13s6dOxUZGeka7+jRozkCjtPplI+Pj+t1kSJF1KJFC5UqVUoOh0NJSUmKj49Xnz59JF24hqZRo0Z6+OGHNX36dH3//fcKCAhQVlbWZfP//e9/1yeffKKePXsqMDBQffv2da1TqlQpJScnE3AAALhBycln83w/KMjvquvkJiQk95/R1x1wKleurLJly+pf//qX0tPTNXnyZAUFBUmSbDZbjnWLFCmihIQESdLRo0d1+vRp13sX161cubLq16+vESNGyOl0KjY2VhUqVLhsnOzsbDkcjlxrKlGihMqWLavY2FgFBgZq2bJl8vPz06effqratWsrIiJC69at08qVKy+bf9myZXrggQf04osv6ptvvtGUKVNcR4vOnDmj4ODg620RAADwsOsOOJ07d9abb76prl27KjU1VREREbLbc/9jrPvuu0+BgYHq2LGjqlSpojvvvPOy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+nT98ccfbs1DwLkGAQEBSktLc712Op3y8vLK9b20tDTOsf5PXn3DlV2tbxkZGerfv7/S0tL01ltveaLEQulavt66du2q1atXa+PGjVq3bl1Bl1ho5dW7hQsX6sSJE+rWrZsWLFigadOmadWqVZ4qtVDJq2++vr569tln5evrq4CAADVo0ICA8z959S0oKEi1atVSSEiI/P39Va9ePe3atcuteQg416Bu3bqub+itW7eqWrVqrvdCQ0O1adMmZWRkKCUlRfv27cvx/u0sr77hyvLqmzFG/+///T9Vr15dw4cPl8Ph8FSZhU5efdu/f79efPFFGWPk7e0tHx8f2e387++ivHr3+uuva+7cuYqLi1P79u3VvXt3PfTQQ54qtVDJq28HDhxQly5dlJ2drfPnz2vz5s2qWbOmp0otVPLqW82aNfX777/r5MmTysrK0rZt21S1alW35uHX6WvQsmVLrVmzRp07d5YxRqNHj9Znn32mihUrqnnz5oqMjFRERISMMerbty/XRPzP1fqG3OXVN6fTqQ0bNigzM1OrV6+WJL366quqU6eOh6v2vKt9vdWoUUOdOnVyXUvy4IMPerrkQoPvVfdcrW/t2rVTeHi4vL291a5dO919992eLrlQuFrf+vXrp549e0qSHn/8cbd/ObYZY0x+Fg4AAOBpHKMFAACWQ8ABAACWQ8ABAACWQ8ABAACWQ8ABAACWQ8ABcFMdOXJE4eHhN32ejRs3FtiN1JxOp95++20999xzeuaZZ9SzZ08dPny4QOYGcG0IOAAsYd68eYqPjy+QuVavXq34+Hh99tlnmjlzpjp37qzRo0cXyNwArg03+gNQYCIjI1W9enXt2bNHfn5+qlevnn788UedOXNGn376qZYtW6alS5cqLS1Np06d0gsvvKDHHntMa9as0bvvvqsiRYooKChIo0eP1q5duzR27Fh5e3urUaNGWr16tXbu3KmqVatq+fLl+v7773Xu3DmVKFFCkyZN0jfffKOVK1cqPT1dhw4d0vPPP68OHTpo27ZtGj16tJxOp8qUKaOxY8fq4MGDGjlypCS55rv0ESwlSpTQjh07tGTJEjVo0EDNmzd33d13xYoVmjRpkowxqlmzpoYNG6a1a9fmWX94eLjKly+vCRMmyOFwqEKFCho+fLi8vb098jkBluDWM8gB4BodPnzYdOzY0RhjTNeuXc3XX39tjDGmR48eZsaMGcYYY15//XXz3//+18ybN890797dZGdnm4SEBPPII4+YzMxM06xZM3P8+HFjjDHTpk0z0dHRZt26daZt27aueaKioszKlStNdna2mThxosnOznbN8/PPP5t58+aZHj16GGOM+eOPP8xjjz1mjDHmySefNHv37jXGGPPll1+aHTt2mI4dO5o9e/a4lo0fP/6y/Vq7dq3p27evadiwoWnfvr1Zv369OX/+vGnWrJlJTEw0xhjz8ccfmyNHjly1fqfTaVq1auXabsKECeaLL77Il/4DtyuO4AAoUBefx1OsWDHXM2aKFSumjIwMSdL//d//yW63q1SpUipWrJgSExMVEBCgMmXKuN4fP368HnnkkVyfpG632+Xt7a1XX31Vfn5+On78uOtJxTVq1JAklStXTpmZmZKkxMREValSRZLUsWNHSdK+ffs0bNgwSdL58+f1t7/9Lcccu3fvVqVKlTR+/HgZY7RmzRr16dNHCxcuVLFixVSyZElJ0vPPP6+TJ09etf6TJ08qPj5effr0kSSlp6erUaNGN9Jm4LZHwAFQqOzcuVPSheCRmpqq0qVLKzU1VfHx8SpdurQ2bNjgChyXPjDTZrPJGKPdu3dr6dKlmjt3rs6dO6cOHTrI/O+JNDab7bL5SpcurQMHDuhvf/ubPv74Y1WqVEmVKlXSO++8o/Lly2vTpk1KSEjIsc3atWu1d+9ejRgxQna7XXfffbd8fX1VqlQpnTlzRsnJyQoKCtLIkSPVtm3bq9ZfokQJlS1bVrGxsQoMDNSyZcvk5+eX360FbisEHACFSmJiorp166aUlBS99dZbcjgcGjlypF566SXZbDYVL15cb7/9tvbs2ZNju/vvv19jx47V+PHj5evrq86dO0uSQkJC8rz4eNiwYXrjjTdkt9sVEhKi7t27q1y5coqKilJWVpZsNptGjRqVY5vIyEi98847ateunQICAmS32xUTEyO73a633npL//znP2W323XvvfcqNDT0qvXb7XYNGjRIvXr1kjFG/v7+iomJyceuArcfHrYJoNCYP3++9u/fr/79+3u6FAC3OP5MHAAAWA5HcAAAgOVwBAcAAFgOAQcAAFgOAQcAAFgOAQcAAFgOAQcAAFjO/wcvGWve7w07EwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.barh(feature_names, importances, color='yellow')\n",
    "plt.title(\"Feature Importance - What Drives Attrition\")\n",
    "plt.xlabel(\"Importance Score\")\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90d609b5",
   "metadata": {},
   "source": [
    "# 2. Predict Risk for All Employees"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "cd02fa76",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Apply same encoding to the full dataset\n",
    "df_predict = df[features].copy()\n",
    "for col in [\"Gender\", \"Department\"]:\n",
    "    df_predict[col] = label_encoders[col].transform(df_predict[col])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "21265c8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Predict probability of exiting\n",
    "df[\"Attrition Risk\"] = model.predict_proba(df_predict)[:, 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "18bd3e11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                Full Name              Job Title       Department  \\\n",
      "748        Anthony Carter               Director      Engineering   \n",
      "40               Owen Lam   Sr. Business Partner  Human Resources   \n",
      "895            Julia Doan       Business Partner  Human Resources   \n",
      "90             Jack Huynh                Manager        Marketing   \n",
      "350          Andrew Huynh       Business Partner  Human Resources   \n",
      "750      Sebastian Rogers           HRIS Analyst  Human Resources   \n",
      "242        Jack Maldonado               Director      Engineering   \n",
      "834  Josephine Richardson  System Administrator                IT   \n",
      "908    Jeremiah Hernandez       Network Engineer               IT   \n",
      "742          Dylan Wilson  Network Administrator               IT   \n",
      "\n",
      "     Attrition Risk  \n",
      "748            1.00  \n",
      "40             0.99  \n",
      "895            0.99  \n",
      "90             0.99  \n",
      "350            0.99  \n",
      "750            0.99  \n",
      "242            0.98  \n",
      "834            0.98  \n",
      "908            0.98  \n",
      "742            0.98  \n"
     ]
    }
   ],
   "source": [
    "# Sort and display top 10 at-risk employees\n",
    "top_risk = df.sort_values(\"Attrition Risk\", ascending=False)\n",
    "print(top_risk[[\"Full Name\", \"Job Title\", \"Department\", \"Attrition Risk\"]].head(10))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "efafc59d",
   "metadata": {},
   "source": [
    "# 3. Export At-Risk Employees"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c08903e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Top 20 high-risk employees exported to High_Attrition_Risk.xlsx\n"
     ]
    }
   ],
   "source": [
    "# Export top 20 at-risk employees\n",
    "top_risk.head(20).to_excel(\"High_Attrition_Risk.xlsx\", index=False)\n",
    "print(\"Top 20 high-risk employees exported to High_Attrition_Risk.xlsx\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "a9d1a9a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: dash in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (2.15.0)\n",
      "Requirement already satisfied: plotly in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (5.18.0)\n",
      "Requirement already satisfied: contextvars==2.4 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.4)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (1.5.1)\n",
      "Requirement already satisfied: Werkzeug<3.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.0.3)\n",
      "Requirement already satisfied: setuptools in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (58.0.4)\n",
      "Requirement already satisfied: importlib-metadata==4.8.3 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (4.8.3)\n",
      "Requirement already satisfied: requests in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.27.1)\n",
      "Requirement already satisfied: typing-extensions>=4.1.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (4.1.1)\n",
      "Requirement already satisfied: dash-html-components==2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.0.0)\n",
      "Requirement already satisfied: Flask<3.1,>=1.0.4 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.0.3)\n",
      "Requirement already satisfied: dash-table==5.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (5.0.0)\n",
      "Requirement already satisfied: retrying in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (1.3.4)\n",
      "Requirement already satisfied: dash-core-components==2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.0.0)\n",
      "Requirement already satisfied: immutables>=0.9 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from contextvars==2.4->dash) (0.19)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from importlib-metadata==4.8.3->dash) (3.6.0)\n",
      "Requirement already satisfied: tenacity>=6.2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from plotly) (8.2.2)\n",
      "Requirement already satisfied: packaging in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from plotly) (21.3)\n",
      "Requirement already satisfied: click>=7.1.2 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (8.0.4)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (2.0.1)\n",
      "Requirement already satisfied: Jinja2>=3.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (3.0.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from click>=7.1.2->Flask<3.1,>=1.0.4->dash) (0.4.4)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Jinja2>=3.0->Flask<3.1,>=1.0.4->dash) (2.0.1)\n",
      "Requirement already satisfied: dataclasses in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Werkzeug<3.1->dash) (0.8)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from packaging->plotly) (3.1.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash) (2021.5.30)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash) (1.26.18)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash) (2.0.12)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash) (3.6)\n",
      "Requirement already satisfied: six>=1.7.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from retrying->dash) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install dash plotly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "a8234d40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: dash in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (2.15.0)\n",
      "Requirement already satisfied: pandas in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (1.1.5)\n",
      "Requirement already satisfied: openpyxl in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (3.1.3)\n",
      "Requirement already satisfied: plotly in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (5.18.0)\n",
      "Requirement already satisfied: dash-html-components==2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.0.0)\n",
      "Requirement already satisfied: requests in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.27.1)\n",
      "Requirement already satisfied: Flask<3.1,>=1.0.4 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.0.3)\n",
      "Requirement already satisfied: contextvars==2.4 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.4)\n",
      "Requirement already satisfied: retrying in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (1.3.4)\n",
      "Requirement already satisfied: typing-extensions>=4.1.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (4.1.1)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (1.5.1)\n",
      "Requirement already satisfied: Werkzeug<3.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.0.3)\n",
      "Requirement already satisfied: importlib-metadata==4.8.3 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (4.8.3)\n",
      "Requirement already satisfied: setuptools in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (58.0.4)\n",
      "Requirement already satisfied: dash-core-components==2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (2.0.0)\n",
      "Requirement already satisfied: dash-table==5.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash) (5.0.0)\n",
      "Requirement already satisfied: immutables>=0.9 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from contextvars==2.4->dash) (0.19)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from importlib-metadata==4.8.3->dash) (3.6.0)\n",
      "Requirement already satisfied: numpy>=1.15.4 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from pandas) (1.19.5)\n",
      "Requirement already satisfied: pytz>=2017.2 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: et-xmlfile in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from openpyxl) (1.1.0)\n",
      "Requirement already satisfied: packaging in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from plotly) (21.3)\n",
      "Requirement already satisfied: tenacity>=6.2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from plotly) (8.2.2)\n",
      "Requirement already satisfied: click>=7.1.2 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (8.0.4)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (2.0.1)\n",
      "Requirement already satisfied: Jinja2>=3.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (3.0.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from click>=7.1.2->Flask<3.1,>=1.0.4->dash) (0.4.4)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Jinja2>=3.0->Flask<3.1,>=1.0.4->dash) (2.0.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from python-dateutil>=2.7.3->pandas) (1.16.0)\n",
      "Requirement already satisfied: dataclasses in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Werkzeug<3.1->dash) (0.8)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from packaging->plotly) (3.1.1)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash) (3.6)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash) (2.0.12)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash) (2021.5.30)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash) (1.26.18)\n"
     ]
    }
   ],
   "source": [
    "!pip install dash pandas openpyxl plotly\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "b7356b5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x256da55ff98>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import dash\n",
    "from dash import dcc, html, dash_table, Input, Output\n",
    "import plotly.express as px\n",
    "from datetime import datetime\n",
    "\n",
    "# Load data\n",
    "df = pd.read_excel(\"ESD.xlsx\", engine=\"openpyxl\")\n",
    "df[\"Hire Date\"] = pd.to_datetime(df[\"Hire Date\"])\n",
    "df[\"Exit Date\"] = pd.to_datetime(df[\"Exit Date\"])\n",
    "df[\"End Date\"] = df[\"Exit Date\"].fillna(pd.to_datetime(\"today\"))\n",
    "df[\"Tenure (Years)\"] = (df[\"End Date\"] - df[\"Hire Date\"]).dt.days / 365\n",
    "df[\"Hire Year\"] = df[\"Hire Date\"].dt.year\n",
    "df[\"Exited\"] = df[\"Exit Date\"].notna().astype(int)\n",
    "df[\"Bonus %\"] = df[\"Bonus %\"].fillna(0)\n",
    "\n",
    "# If you trained a model earlier, reuse and predict risk\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "features = [\"Age\", \"Annual Salary\", \"Bonus %\", \"Tenure (Years)\", \"Gender\", \"Department\"]\n",
    "df_model = df[features + [\"Exited\"]].dropna()\n",
    "\n",
    "# Encode\n",
    "label_encoders = {}\n",
    "df_encoded = df_model.copy()\n",
    "for col in [\"Gender\", \"Department\"]:\n",
    "    le = LabelEncoder()\n",
    "    df_encoded[col] = le.fit_transform(df_encoded[col])\n",
    "    label_encoders[col] = le\n",
    "\n",
    "X = df_encoded.drop(\"Exited\", axis=1)\n",
    "y = df_encoded[\"Exited\"]\n",
    "model = RandomForestClassifier()\n",
    "model.fit(X, y)\n",
    "\n",
    "# Predict on full data\n",
    "df_pred = df[features].copy()\n",
    "for col in [\"Gender\", \"Department\"]:\n",
    "    df_pred[col] = label_encoders[col].transform(df_pred[col])\n",
    "df[\"Attrition Risk\"] = model.predict_proba(df_pred)[:, 1]\n",
    "\n",
    "# Initialize Dash app\n",
    "app = dash.Dash(__name__)\n",
    "app.title = \"Employee Attrition Dashboard\"\n",
    "\n",
    "# Layout\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"Employee Attrition Dashboard\", style={'textAlign': 'center'}),\n",
    "    \n",
    "    html.Div([\n",
    "        html.Label(\"Select Department:\"),\n",
    "        dcc.Dropdown(\n",
    "            options=[{\"label\": d, \"value\": d} for d in sorted(df[\"Department\"].dropna().unique())],\n",
    "            value=None, id=\"dept-filter\", placeholder=\"All Departments\"\n",
    "        ),\n",
    "        html.Label(\"Select Gender:\"),\n",
    "        dcc.Dropdown(\n",
    "            options=[{\"label\": g, \"value\": g} for g in sorted(df[\"Gender\"].dropna().unique())],\n",
    "            value=None, id=\"gender-filter\", placeholder=\"All Genders\"\n",
    "        ),\n",
    "    ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '20px'}),\n",
    "    \n",
    "    html.Div([\n",
    "        dcc.Graph(id=\"salary-trend\"),\n",
    "        dcc.Graph(id=\"attrition-dept\"),\n",
    "        dcc.Graph(id=\"age-hist\"),\n",
    "    ], style={'width': '68%', 'display': 'inline-block', 'padding': '20px'}),\n",
    "\n",
    "    html.H2(\"Top At-Risk Employees\"),\n",
    "    dash_table.DataTable(\n",
    "        id='risk-table',\n",
    "        columns=[{\"name\": i, \"id\": i} for i in [\"Full Name\", \"Job Title\", \"Department\", \"Attrition Risk\"]],\n",
    "        style_table={'overflowX': 'auto'},\n",
    "        style_cell={'textAlign': 'left'},\n",
    "        page_size=10\n",
    "    )\n",
    "])\n",
    "\n",
    "# Callbacks\n",
    "@app.callback(\n",
    "    [Output(\"salary-trend\", \"figure\"),\n",
    "     Output(\"attrition-dept\", \"figure\"),\n",
    "     Output(\"age-hist\", \"figure\"),\n",
    "     Output(\"risk-table\", \"data\")],\n",
    "    [Input(\"dept-filter\", \"value\"),\n",
    "     Input(\"gender-filter\", \"value\")]\n",
    ")\n",
    "def update_charts(dept, gender):\n",
    "    dff = df.copy()\n",
    "    if dept:\n",
    "        dff = dff[dff[\"Department\"] == dept]\n",
    "    if gender:\n",
    "        dff = dff[dff[\"Gender\"] == gender]\n",
    "\n",
    "    # Salary trend\n",
    "    salary_trend = dff.groupby(\"Hire Year\")[\"Annual Salary\"].mean().reset_index()\n",
    "    fig1 = px.line(salary_trend, x=\"Hire Year\", y=\"Annual Salary\", title=\"Average Salary by Hire Year\")\n",
    "\n",
    "    # Attrition by Department\n",
    "    attrition = dff.groupby(\"Department\")[\"Exited\"].mean().reset_index()\n",
    "    fig2 = px.bar(attrition, x=\"Department\", y=\"Exited\", title=\"Attrition Rate by Department\")\n",
    "\n",
    "    # Age histogram\n",
    "    fig3 = px.histogram(dff, x=\"Age\", nbins=10, title=\"Age Distribution\")\n",
    "\n",
    "    # Risk table\n",
    "    top_risk = dff[[\"Full Name\", \"Job Title\", \"Department\", \"Attrition Risk\"]].sort_values(\"Attrition Risk\", ascending=False).head(10)\n",
    "    return fig1, fig2, fig3, top_risk.to_dict(\"records\")\n",
    "\n",
    "# Run app\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b6d1f7d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1.Export High-Risk Employees (Download Button)\n",
    "#2.More Filters (like Age Range or Business Unit)\n",
    "#3.Deploy the Dashboard (Optional)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "5401288c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting dash-extensions\n",
      "  Downloading dash_extensions-0.0.71-py3-none-any.whl (1.6 MB)\n",
      "Collecting jsbeautifier\n",
      "  Downloading jsbeautifier-1.15.4-py3-none-any.whl (94 kB)\n",
      "Requirement already satisfied: dash in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash-extensions) (2.15.0)\n",
      "Collecting more-itertools\n",
      "  Downloading more_itertools-8.14.0-py3-none-any.whl (52 kB)\n",
      "Collecting Flask-Caching\n",
      "  Downloading Flask_Caching-1.10.1-py3-none-any.whl (34 kB)\n",
      "Requirement already satisfied: contextvars==2.4 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (2.4)\n",
      "Requirement already satisfied: Flask<3.1,>=1.0.4 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (2.0.3)\n",
      "Requirement already satisfied: typing-extensions>=4.1.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (4.1.1)\n",
      "Requirement already satisfied: importlib-metadata==4.8.3 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (4.8.3)\n",
      "Requirement already satisfied: dash-table==5.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (5.0.0)\n",
      "Requirement already satisfied: requests in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (2.27.1)\n",
      "Requirement already satisfied: retrying in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (1.3.4)\n",
      "Requirement already satisfied: dash-core-components==2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (2.0.0)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (1.5.1)\n",
      "Requirement already satisfied: dash-html-components==2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (2.0.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (58.0.4)\n",
      "Requirement already satisfied: Werkzeug<3.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (2.0.3)\n",
      "Requirement already satisfied: plotly>=5.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from dash->dash-extensions) (5.18.0)\n",
      "Requirement already satisfied: immutables>=0.9 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from contextvars==2.4->dash->dash-extensions) (0.19)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from importlib-metadata==4.8.3->dash->dash-extensions) (3.6.0)\n",
      "Requirement already satisfied: Jinja2>=3.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash->dash-extensions) (3.0.3)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash->dash-extensions) (2.0.1)\n",
      "Requirement already satisfied: click>=7.1.2 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash->dash-extensions) (8.0.4)\n",
      "Requirement already satisfied: colorama in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from click>=7.1.2->Flask<3.1,>=1.0.4->dash->dash-extensions) (0.4.4)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Jinja2>=3.0->Flask<3.1,>=1.0.4->dash->dash-extensions) (2.0.1)\n",
      "Requirement already satisfied: packaging in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from plotly>=5.0.0->dash->dash-extensions) (21.3)\n",
      "Requirement already satisfied: tenacity>=6.2.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from plotly>=5.0.0->dash->dash-extensions) (8.2.2)\n",
      "Requirement already satisfied: dataclasses in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from Werkzeug<3.1->dash->dash-extensions) (0.8)\n",
      "Requirement already satisfied: six>=1.13.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from jsbeautifier->dash-extensions) (1.16.0)\n",
      "Collecting editorconfig>=0.12.2\n",
      "  Downloading EditorConfig-0.17.0-py3-none-any.whl (16 kB)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from packaging->plotly>=5.0.0->dash->dash-extensions) (3.1.1)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash->dash-extensions) (3.6)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash->dash-extensions) (2.0.12)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash->dash-extensions) (2021.5.30)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\rajvi\\.conda\\envs\\deepl\\lib\\site-packages (from requests->dash->dash-extensions) (1.26.18)\n",
      "Installing collected packages: editorconfig, more-itertools, jsbeautifier, Flask-Caching, dash-extensions\n",
      "Successfully installed Flask-Caching-1.10.1 dash-extensions-0.0.71 editorconfig-0.17.0 jsbeautifier-1.15.4 more-itertools-8.14.0\n"
     ]
    }
   ],
   "source": [
    "!pip install dash-extensions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f8b1f3e",
   "metadata": {},
   "source": [
    "# Modified App Layout (add this inside html.Div([...])):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "aed86056",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(Download(id='download-dataframe-csv'),)"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html.Button(\"Download High-Risk Employees\", id=\"btn-download\", n_clicks=0),\n",
    "dcc.Download(id=\"download-dataframe-csv\"),"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b40e6cd3",
   "metadata": {},
   "source": [
    "# Add This Callback Below the Others:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "46b09822",
   "metadata": {},
   "outputs": [],
   "source": [
    "from dash.dependencies import State\n",
    "from dash import ctx\n",
    "from dash_extensions.snippets import send_data_frame\n",
    "\n",
    "@app.callback(\n",
    "    Output(\"download-dataframe-csv\", \"data\"),\n",
    "    Input(\"btn-download\", \"n_clicks\"),\n",
    "    State(\"dept-filter\", \"value\"),\n",
    "    State(\"gender-filter\", \"value\"),\n",
    "    prevent_initial_call=True\n",
    ")\n",
    "def download_data(n_clicks, dept, gender):\n",
    "    dff = df.copy()\n",
    "    if dept:\n",
    "        dff = dff[dff[\"Department\"] == dept]\n",
    "    if gender:\n",
    "        dff = dff[dff[\"Gender\"] == gender]\n",
    "    top_risk = dff.sort_values(\"Attrition Risk\", ascending=False).head(20)\n",
    "    return send_data_frame(top_risk.to_csv, filename=\"high_attrition_risk.csv\", index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "c57d6e88",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-60-4ad6b77c7937>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-60-4ad6b77c7937>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    employee-dashboard/\u001b[0m\n\u001b[1;37m                       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "employee-dashboard/\n",
    "│\n",
    "├── app.py              # Your Dash app file\n",
    "├── requirements.txt    # Python dependencies\n",
    "├── ESD.xlsx            # Your Excel data file\n",
    "└── Procfile            # Tells Render how to run it\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95995e3d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
