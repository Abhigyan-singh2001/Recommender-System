{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c95455eb-70be-435f-8593-2569d8a03e7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d982a05b-270a-49d3-81d2-c4f82f7eaeb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting faiss-cpu\n",
      "  Downloading faiss_cpu-1.8.0.post1-cp39-cp39-win_amd64.whl.metadata (3.8 kB)\n",
      "Requirement already satisfied: numpy<2.0,>=1.0 in c:\\users\\singh\\anaconda3\\envs\\test_env\\lib\\site-packages (from faiss-cpu) (1.26.4)\n",
      "Requirement already satisfied: packaging in c:\\users\\singh\\anaconda3\\envs\\test_env\\lib\\site-packages (from faiss-cpu) (23.2)\n",
      "Downloading faiss_cpu-1.8.0.post1-cp39-cp39-win_amd64.whl (14.6 MB)\n",
      "   ---------------------------------------- 0.0/14.6 MB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/14.6 MB 660.6 kB/s eta 0:00:23\n",
      "   ---------------------------------------- 0.1/14.6 MB 1.6 MB/s eta 0:00:09\n",
      "   - -------------------------------------- 0.5/14.6 MB 4.0 MB/s eta 0:00:04\n",
      "   ---- ----------------------------------- 1.8/14.6 MB 10.5 MB/s eta 0:00:02\n",
      "   ---------- ----------------------------- 3.7/14.6 MB 18.0 MB/s eta 0:00:01\n",
      "   --------------- ------------------------ 5.8/14.6 MB 23.1 MB/s eta 0:00:01\n",
      "   --------------------- ------------------ 7.9/14.6 MB 26.7 MB/s eta 0:00:01\n",
      "   ------------------------- -------------- 9.4/14.6 MB 27.3 MB/s eta 0:00:01\n",
      "   -------------------------- ------------- 9.8/14.6 MB 25.0 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 13.5/14.6 MB 43.5 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 14.6/14.6 MB 40.9 MB/s eta 0:00:00\n",
      "Installing collected packages: faiss-cpu\n",
      "Successfully installed faiss-cpu-1.8.0.post1\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install faiss-cpu\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f8f3e753-c6af-4730-a90b-a6fa4ebfb902",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in c:\\users\\singh\\anaconda3\\envs\\test_env\\lib\\site-packages (2.32.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\singh\\anaconda3\\envs\\test_env\\lib\\site-packages (from requests) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\singh\\anaconda3\\envs\\test_env\\lib\\site-packages (from requests) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\singh\\anaconda3\\envs\\test_env\\lib\\site-packages (from requests) (1.26.19)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\singh\\anaconda3\\envs\\test_env\\lib\\site-packages (from requests) (2024.7.4)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install requests\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4bc6a0a0-c039-4452-a93e-0aa90ae64b91",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_data = pd.read_csv(\"D:/Netflix dataset/netflix_titles.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ec5d4810-6306-4173-846b-fabd2c040ec5",
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
       "      <th>show_id</th>\n",
       "      <th>type</th>\n",
       "      <th>title</th>\n",
       "      <th>director</th>\n",
       "      <th>cast</th>\n",
       "      <th>country</th>\n",
       "      <th>date_added</th>\n",
       "      <th>release_year</th>\n",
       "      <th>rating</th>\n",
       "      <th>duration</th>\n",
       "      <th>listed_in</th>\n",
       "      <th>description</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>s1</td>\n",
       "      <td>Movie</td>\n",
       "      <td>Dick Johnson Is Dead</td>\n",
       "      <td>Kirsten Johnson</td>\n",
       "      <td>NaN</td>\n",
       "      <td>United States</td>\n",
       "      <td>September 25, 2021</td>\n",
       "      <td>2020</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>90 min</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>As her father nears the end of his life, filmm...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>s2</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Blood &amp; Water</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...</td>\n",
       "      <td>South Africa</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>2 Seasons</td>\n",
       "      <td>International TV Shows, TV Dramas, TV Mysteries</td>\n",
       "      <td>After crossing paths at a party, a Cape Town t...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>s3</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Ganglands</td>\n",
       "      <td>Julien Leclercq</td>\n",
       "      <td>Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>1 Season</td>\n",
       "      <td>Crime TV Shows, International TV Shows, TV Act...</td>\n",
       "      <td>To protect his family from a powerful drug lor...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>s4</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Jailbirds New Orleans</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>1 Season</td>\n",
       "      <td>Docuseries, Reality TV</td>\n",
       "      <td>Feuds, flirtations and toilet talk go down amo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>s5</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Kota Factory</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...</td>\n",
       "      <td>India</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>2 Seasons</td>\n",
       "      <td>International TV Shows, Romantic TV Shows, TV ...</td>\n",
       "      <td>In a city of coaching centers known to train I...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>s6</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Midnight Mass</td>\n",
       "      <td>Mike Flanagan</td>\n",
       "      <td>Kate Siegel, Zach Gilford, Hamish Linklater, H...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>1 Season</td>\n",
       "      <td>TV Dramas, TV Horror, TV Mysteries</td>\n",
       "      <td>The arrival of a charismatic young priest brin...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>s7</td>\n",
       "      <td>Movie</td>\n",
       "      <td>My Little Pony: A New Generation</td>\n",
       "      <td>Robert Cullen, José Luis Ucha</td>\n",
       "      <td>Vanessa Hudgens, Kimiko Glenn, James Marsden, ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>PG</td>\n",
       "      <td>91 min</td>\n",
       "      <td>Children &amp; Family Movies</td>\n",
       "      <td>Equestria's divided. But a bright-eyed hero be...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>s8</td>\n",
       "      <td>Movie</td>\n",
       "      <td>Sankofa</td>\n",
       "      <td>Haile Gerima</td>\n",
       "      <td>Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...</td>\n",
       "      <td>United States, Ghana, Burkina Faso, United Kin...</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>1993</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>125 min</td>\n",
       "      <td>Dramas, Independent Movies, International Movies</td>\n",
       "      <td>On a photo shoot in Ghana, an American model s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>s9</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>The Great British Baking Show</td>\n",
       "      <td>Andy Devonshire</td>\n",
       "      <td>Mel Giedroyc, Sue Perkins, Mary Berry, Paul Ho...</td>\n",
       "      <td>United Kingdom</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-14</td>\n",
       "      <td>9 Seasons</td>\n",
       "      <td>British TV Shows, Reality TV</td>\n",
       "      <td>A talented batch of amateur bakers face off in...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>s10</td>\n",
       "      <td>Movie</td>\n",
       "      <td>The Starling</td>\n",
       "      <td>Theodore Melfi</td>\n",
       "      <td>Melissa McCarthy, Chris O'Dowd, Kevin Kline, T...</td>\n",
       "      <td>United States</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>104 min</td>\n",
       "      <td>Comedies, Dramas</td>\n",
       "      <td>A woman adjusting to life after a loss contend...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  show_id     type                             title  \\\n",
       "0      s1    Movie              Dick Johnson Is Dead   \n",
       "1      s2  TV Show                     Blood & Water   \n",
       "2      s3  TV Show                         Ganglands   \n",
       "3      s4  TV Show             Jailbirds New Orleans   \n",
       "4      s5  TV Show                      Kota Factory   \n",
       "5      s6  TV Show                     Midnight Mass   \n",
       "6      s7    Movie  My Little Pony: A New Generation   \n",
       "7      s8    Movie                           Sankofa   \n",
       "8      s9  TV Show     The Great British Baking Show   \n",
       "9     s10    Movie                      The Starling   \n",
       "\n",
       "                        director  \\\n",
       "0                Kirsten Johnson   \n",
       "1                            NaN   \n",
       "2                Julien Leclercq   \n",
       "3                            NaN   \n",
       "4                            NaN   \n",
       "5                  Mike Flanagan   \n",
       "6  Robert Cullen, José Luis Ucha   \n",
       "7                   Haile Gerima   \n",
       "8                Andy Devonshire   \n",
       "9                 Theodore Melfi   \n",
       "\n",
       "                                                cast  \\\n",
       "0                                                NaN   \n",
       "1  Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...   \n",
       "2  Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...   \n",
       "3                                                NaN   \n",
       "4  Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...   \n",
       "5  Kate Siegel, Zach Gilford, Hamish Linklater, H...   \n",
       "6  Vanessa Hudgens, Kimiko Glenn, James Marsden, ...   \n",
       "7  Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...   \n",
       "8  Mel Giedroyc, Sue Perkins, Mary Berry, Paul Ho...   \n",
       "9  Melissa McCarthy, Chris O'Dowd, Kevin Kline, T...   \n",
       "\n",
       "                                             country          date_added  \\\n",
       "0                                      United States  September 25, 2021   \n",
       "1                                       South Africa  September 24, 2021   \n",
       "2                                                NaN  September 24, 2021   \n",
       "3                                                NaN  September 24, 2021   \n",
       "4                                              India  September 24, 2021   \n",
       "5                                                NaN  September 24, 2021   \n",
       "6                                                NaN  September 24, 2021   \n",
       "7  United States, Ghana, Burkina Faso, United Kin...  September 24, 2021   \n",
       "8                                     United Kingdom  September 24, 2021   \n",
       "9                                      United States  September 24, 2021   \n",
       "\n",
       "   release_year rating   duration  \\\n",
       "0          2020  PG-13     90 min   \n",
       "1          2021  TV-MA  2 Seasons   \n",
       "2          2021  TV-MA   1 Season   \n",
       "3          2021  TV-MA   1 Season   \n",
       "4          2021  TV-MA  2 Seasons   \n",
       "5          2021  TV-MA   1 Season   \n",
       "6          2021     PG     91 min   \n",
       "7          1993  TV-MA    125 min   \n",
       "8          2021  TV-14  9 Seasons   \n",
       "9          2021  PG-13    104 min   \n",
       "\n",
       "                                           listed_in  \\\n",
       "0                                      Documentaries   \n",
       "1    International TV Shows, TV Dramas, TV Mysteries   \n",
       "2  Crime TV Shows, International TV Shows, TV Act...   \n",
       "3                             Docuseries, Reality TV   \n",
       "4  International TV Shows, Romantic TV Shows, TV ...   \n",
       "5                 TV Dramas, TV Horror, TV Mysteries   \n",
       "6                           Children & Family Movies   \n",
       "7   Dramas, Independent Movies, International Movies   \n",
       "8                       British TV Shows, Reality TV   \n",
       "9                                   Comedies, Dramas   \n",
       "\n",
       "                                         description  \n",
       "0  As her father nears the end of his life, filmm...  \n",
       "1  After crossing paths at a party, a Cape Town t...  \n",
       "2  To protect his family from a powerful drug lor...  \n",
       "3  Feuds, flirtations and toilet talk go down amo...  \n",
       "4  In a city of coaching centers known to train I...  \n",
       "5  The arrival of a charismatic young priest brin...  \n",
       "6  Equestria's divided. But a bright-eyed hero be...  \n",
       "7  On a photo shoot in Ghana, an American model s...  \n",
       "8  A talented batch of amateur bakers face off in...  \n",
       "9  A woman adjusting to life after a loss contend...  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "362c905f-3278-4086-b568-7f45891ce68b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "show_id            0\n",
      "type               0\n",
      "title              0\n",
      "director        2634\n",
      "cast             825\n",
      "country          831\n",
      "date_added        10\n",
      "release_year       0\n",
      "rating             4\n",
      "duration           3\n",
      "listed_in          0\n",
      "description        0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(df_data.isna().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b4b44d0c-7cf3-4829-87d6-417324910a07",
   "metadata": {},
   "outputs": [],
   "source": [
    "cleaned_data = df_data.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "954f2052-9556-46c5-85fb-84cd40e99727",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "show_id         0\n",
      "type            0\n",
      "title           0\n",
      "director        0\n",
      "cast            0\n",
      "country         0\n",
      "date_added      0\n",
      "release_year    0\n",
      "rating          0\n",
      "duration        0\n",
      "listed_in       0\n",
      "description     0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(cleaned_data.isna().sum())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "db9b6916-faf1-4a27-971e-64659d49a6e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5332, 13)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cleaned_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "43efe3e1-33b2-45d1-a9a0-5dd947c16fbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_to_string(row):\n",
    "    string_format = f\"\"\"\n",
    "    Type:{row[\"type\"]} \n",
    "    Title:{row[\"title\"]},\n",
    "    Director:{row[\"director\"]},\n",
    "    Cast:{row[\"cast\"]},\n",
    "    Released:{row[\"release_year\"]},\n",
    "    Rating:{row[\"rating\"]},\n",
    "    Genere:{row[\"listed_in\"]},\n",
    "\n",
    "    Description:{row[\"description\"]}\n",
    "    \"\"\"\n",
    "    return string_format\n",
    "    \n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "822bf6a0-21dd-42d4-abed-3cf8e32d2a6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\singh\\AppData\\Local\\Temp\\ipykernel_27548\\2300188408.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  cleaned_data['String_data']= cleaned_data.apply(convert_to_string, axis=1)\n"
     ]
    }
   ],
   "source": [
    "cleaned_data['String_data']= cleaned_data.apply(convert_to_string, axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "214436be-fa3c-4127-b982-9e4af4ca9e4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "    Type:Movie \n",
      "    Title:Sankofa,\n",
      "    Director:Haile Gerima,\n",
      "    Cast:Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra Duah, Nick Medley, Mutabaruka, Afemo Omilami, Reggie Carter, Mzuri,\n",
      "    Released:1993,\n",
      "    Rating:TV-MA,\n",
      "    Genere:Dramas, Independent Movies, International Movies,\n",
      "\n",
      "    Description:On a photo shoot in Ghana, an American model slips back in time, becomes enslaved on a plantation and bears witness to the agony of her ancestral past.\n",
      "    \n"
     ]
    }
   ],
   "source": [
    "print(cleaned_data['String_data'].values[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e3d00f00-f48e-4603-abc1-d2399ef0355d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import faiss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5a845f34-d825-42e9-ba3b-d5e36ef22533",
   "metadata": {},
   "outputs": [],
   "source": [
    "dimension = 4096\n",
    "index = faiss.IndexFlatL2(dimension)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d38a42d3-c913-41ce-91c6-8e4494bb0817",
   "metadata": {},
   "outputs": [],
   "source": [
    "input = np.zeros((len(cleaned_data[\"String_data\"]), dimension), dtype = 'float32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a7a9a517-fbc3-45c6-a2be-8d8d988afad4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       ...,\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.]], dtype=float32)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ea091922-0d51-40fa-b56b-92960e5fcb3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "import faiss\n",
    "print(faiss.get_num_gpus())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "850b2a0f-967d-47c6-ba1f-9916691fcbdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Processing data for index 0\n",
      "Processing data for index 100\n",
      "Processing data for index 200\n",
      "Processing data for index 300\n",
      "Processing data for index 400\n",
      "Processing data for index 500\n",
      "Processing data for index 600\n",
      "Processing data for index 700\n",
      "Processing data for index 800\n",
      "Processing data for index 900\n",
      "Processing data for index 1000\n",
      "Processing data for index 1100\n",
      "Processing data for index 1200\n",
      "Processing data for index 1300\n",
      "Processing data for index 1400\n",
      "Processing data for index 1500\n",
      "Processing data for index 1600\n",
      "Processing data for index 1700\n",
      "Processing data for index 1800\n",
      "Processing data for index 1900\n",
      "Processing data for index 2000\n",
      "Processing data for index 2100\n",
      "Processing data for index 2200\n",
      "Processing data for index 2300\n",
      "Processing data for index 2400\n",
      "Processing data for index 2500\n",
      "Processing data for index 2600\n",
      "Processing data for index 2700\n",
      "Processing data for index 2800\n",
      "Processing data for index 2900\n",
      "Processing data for index 3000\n",
      "Processing data for index 3100\n",
      "Processing data for index 3200\n",
      "Processing data for index 3300\n",
      "Processing data for index 3400\n",
      "Processing data for index 3500\n",
      "Processing data for index 3600\n",
      "Processing data for index 3700\n",
      "Processing data for index 3800\n",
      "Processing data for index 3900\n",
      "Processing data for index 4000\n",
      "Processing data for index 4100\n",
      "Processing data for index 4200\n",
      "Processing data for index 4300\n",
      "Processing data for index 4400\n",
      "Processing data for index 4500\n",
      "Processing data for index 4600\n",
      "Processing data for index 4700\n",
      "Processing data for index 4800\n",
      "Processing data for index 4900\n",
      "Processing data for index 5000\n",
      "Processing data for index 5100\n",
      "Processing data for index 5200\n",
      "Processing data for index 5300\n",
      "FAISS index with GPU support is ready for use.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import numpy as np\n",
    "import faiss\n",
    "import time\n",
    "\n",
    "# Assuming `cleaned_data` is your DataFrame with 'String_data' column\n",
    "input_dim = 4096  # Adjust this to match the dimension of your embedding model\n",
    "input = np.zeros((len(cleaned_data), input_dim)).astype('float32')  # Ensure correct dtype for FAISS\n",
    "\n",
    "def get_embedding(representation, retries=5, delay=1):\n",
    "    for attempt in range(retries):\n",
    "        try:\n",
    "            res = requests.post('http://localhost:11434/api/embeddings',\n",
    "                                json={\n",
    "                                    'model': \"llama2\",\n",
    "                                    'prompt': representation\n",
    "                                })\n",
    "            if res.status_code == 200:\n",
    "                return res.json()[\"embedding\"]\n",
    "            else:\n",
    "                print(f\"Error for representation {representation[:20]}...: {res.status_code}, {res.text}\")\n",
    "                break\n",
    "        except requests.ConnectionError as e:\n",
    "            print(f\"ConnectionError on attempt {attempt + 1}/{retries}: {e}\")\n",
    "            if attempt < retries - 1:\n",
    "                time.sleep(delay)\n",
    "                delay *= 2  # Exponential backoff\n",
    "            else:\n",
    "                print(\"Max retries exceeded. Skipping this entry.\")\n",
    "    return None\n",
    "\n",
    "# Process each representation and get embeddings\n",
    "for i, representation in enumerate(cleaned_data['String_data']):\n",
    "    # To see the progress after every 100 steps\n",
    "    if i % 100 == 0:\n",
    "        print('Processing data for index ' + str(i))\n",
    "    \n",
    "    embedding = get_embedding(representation)\n",
    "    if embedding is not None:\n",
    "        input[i] = np.array(embedding)\n",
    "    else:\n",
    "        print(f\"Failed to retrieve embedding for index {i}\")\n",
    "\n",
    "# Initialize FAISS with GPU support\n",
    "res = faiss.StandardGpuResources()  # Initialize GPU resources\n",
    "index = faiss.GpuIndexFlatL2(res, input_dim)  # Use L2 distance for similarity and GPU resources\n",
    "\n",
    "# Add embeddings to the FAISS index\n",
    "index.add(input)\n",
    "\n",
    "print(\"FAISS index with GPU support is ready for use.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35910a0b-128a-447f-baf7-28ed6865397b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import torch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd7ab18f-06d0-4795-b601-60d331cabacd",
   "metadata": {},
   "outputs": [],
   "source": [
    "torch.cuda.is_available()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "f9f2d048-57fd-413f-a05b-5ab8f26a213b",
   "metadata": {},
   "outputs": [],
   "source": [
    "cpu_index = faiss.index_gpu_to_cpu(index)\n",
    "\n",
    "# Now save the CPU index\n",
    "faiss.write_index(cpu_index, \"faiss_index.bin\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "9def843a-b0b2-4601-81ac-e8132482e03a",
   "metadata": {},
   "outputs": [],
   "source": [
    "index = faiss.read_index(\"faiss_index.bin\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "8b2474af-94b0-4a26-8c75-1266cb0bf4d6",
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
       "      <th>show_id</th>\n",
       "      <th>type</th>\n",
       "      <th>title</th>\n",
       "      <th>director</th>\n",
       "      <th>cast</th>\n",
       "      <th>country</th>\n",
       "      <th>date_added</th>\n",
       "      <th>release_year</th>\n",
       "      <th>rating</th>\n",
       "      <th>duration</th>\n",
       "      <th>listed_in</th>\n",
       "      <th>description</th>\n",
       "      <th>String_data</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>s8</td>\n",
       "      <td>Movie</td>\n",
       "      <td>Sankofa</td>\n",
       "      <td>Haile Gerima</td>\n",
       "      <td>Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...</td>\n",
       "      <td>United States, Ghana, Burkina Faso, United Kin...</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>1993</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>125 min</td>\n",
       "      <td>Dramas, Independent Movies, International Movies</td>\n",
       "      <td>On a photo shoot in Ghana, an American model s...</td>\n",
       "      <td>\\n    Type:Movie \\n    Title:Sankofa,\\n    Dir...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  show_id   type    title      director  \\\n",
       "7      s8  Movie  Sankofa  Haile Gerima   \n",
       "\n",
       "                                                cast  \\\n",
       "7  Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...   \n",
       "\n",
       "                                             country          date_added  \\\n",
       "7  United States, Ghana, Burkina Faso, United Kin...  September 24, 2021   \n",
       "\n",
       "   release_year rating duration  \\\n",
       "7          1993  TV-MA  125 min   \n",
       "\n",
       "                                          listed_in  \\\n",
       "7  Dramas, Independent Movies, International Movies   \n",
       "\n",
       "                                         description  \\\n",
       "7  On a photo shoot in Ghana, an American model s...   \n",
       "\n",
       "                                         String_data  \n",
       "7  \\n    Type:Movie \\n    Title:Sankofa,\\n    Dir...  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cleaned_data[cleaned_data.title.str.contains(\"Sankofa\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "8f6752a1-8cfa-4757-87b2-e881b05dddce",
   "metadata": {},
   "outputs": [],
   "source": [
    "fav_movie = cleaned_data.iloc[7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "1d45c074-c7b3-4eb4-b189-4256f539e093",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "show_id                                                       s30\n",
       "type                                                        Movie\n",
       "title                                                    Paranoia\n",
       "director                                           Robert Luketic\n",
       "cast            Liam Hemsworth, Gary Oldman, Amber Heard, Harr...\n",
       "country                              United States, India, France\n",
       "date_added                                     September 19, 2021\n",
       "release_year                                                 2013\n",
       "rating                                                      PG-13\n",
       "duration                                                  106 min\n",
       "listed_in                                               Thrillers\n",
       "description     Blackmailed by his company's CEO, a low-level ...\n",
       "String_data     \\n    Type:Movie \\n    Title:Paranoia,\\n    Di...\n",
       "Name: 29, dtype: object"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fav_movie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "0dfb48f6-01ac-46ec-87f5-7f03208b59a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "res = requests.post('http://localhost:11434/api/embeddings',\n",
    "                                json={\n",
    "                                    'model': \"llama2\",\n",
    "                                    'prompt': fav_movie['String_data']\n",
    "                                })"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "d32bb517-e164-4cce-8dd7-c6adabfe94e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "embedding = np.array([res.json()['embedding']], dtype='float32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a1a8e231-b7aa-48f1-8be4-ce54ff57aea9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.81727016,  1.2920424 ,  3.3516822 , ..., -1.1654328 ,\n",
       "         0.86068374,  1.75916   ]], dtype=float32)"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "embedding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "bd91b201-4a1a-4706-9e81-9c85408dbaec",
   "metadata": {},
   "outputs": [],
   "source": [
    "D, I = index.search(embedding,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a2a332fa-3ed6-4f5b-8066-3b710aed48dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[   7,  550,  260, 1011, 1763]], dtype=int64)"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "I\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "85eb4704-3a6d-49ad-a656-d237b6f3e135",
   "metadata": {},
   "outputs": [],
   "source": [
    "best_matches = np.array(cleaned_data['String_data'])[I.flatten()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "490353bd-68e4-4314-8907-1b6d47633c4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([\"\\n    Type:Movie \\n    Title:Paranoia,\\n    Director:Robert Luketic,\\n    Cast:Liam Hemsworth, Gary Oldman, Amber Heard, Harrison Ford, Lucas Till, Embeth Davidtz, Julian McMahon, Josh Holloway, Richard Dreyfuss, Angela Sarafyan,\\n    Released:2013,\\n    Rating:PG-13,\\n    Genere:Thrillers,\\n\\n    Description:Blackmailed by his company's CEO, a low-level employee finds himself forced to spy on the boss's rival and former mentor.\\n    \",\n",
       "       '\\n    Type:Movie \\n    Title:Croupier,\\n    Director:Mike Hodges,\\n    Cast:Clive Owen, Kate Hardie, Alex Kingston, Gina McKee, Nicholas Ball, Nick Reding, Alexander Morton,\\n    Released:1998,\\n    Rating:TV-MA,\\n    Genere:Dramas, Independent Movies, Thrillers,\\n\\n    Description:A would-be writer lands a job as a croupier to make ends meet. But when he becomes involved with a gambler, he is lured into taking part in a heist.\\n    ',\n",
       "       \"\\n    Type:Movie \\n    Title:The Game,\\n    Director:David Fincher,\\n    Cast:Michael Douglas, Sean Penn, Deborah Kara Unger, James Rebhorn, Peter Donat, Carroll Baker, Anna Katarina, Armin Mueller-Stahl,\\n    Released:1997,\\n    Rating:R,\\n    Genere:Thrillers,\\n\\n    Description:An aloof investment banker's life spirals into peril and paranoia after his brother gives him an odd birthday gift: the chance to play a mysterious game.\\n    \",\n",
       "       \"\\n    Type:Movie \\n    Title:Manorama Six Feet Under,\\n    Director:Navdeep Singh,\\n    Cast:Abhay Deol, Gul Panag, Raima Sen, Sarika, Kulbhushan Kharbanda, Vinay Pathak, Yana Gupta, Jogi, Brijendra Kala, Nawazuddin Siddiqui,\\n    Released:2007,\\n    Rating:TV-14,\\n    Genere:Dramas, International Movies, Thrillers,\\n\\n    Description:A government employee and aspiring crime writer, who is under investigation for corruption, is asked by a politician's wife to spy on her husband.\\n    \",\n",
       "       '\\n    Type:Movie \\n    Title:Why Me?,\\n    Director:Tudor Giurgiu,\\n    Cast:Emilian Oprea, Mihai Constantin, Andreea Vasile, Dan Condurache, Liviu Pintileasa, Mihai Smarandache, Alin Florea, Lucretia Mandric,\\n    Released:2015,\\n    Rating:TV-MA,\\n    Genere:Dramas, International Movies, Thrillers,\\n\\n    Description:A young prosecutor is assigned a career-making case involving a colleague but soon starts to question the motivations behind the charges.\\n    '],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_matches"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "f02f954a-a36d-4b11-bc57-41502c1d47b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Next movie to watch\n",
      "\n",
      "    Type:Movie \n",
      "    Title:Paranoia,\n",
      "    Director:Robert Luketic,\n",
      "    Cast:Liam Hemsworth, Gary Oldman, Amber Heard, Harrison Ford, Lucas Till, Embeth Davidtz, Julian McMahon, Josh Holloway, Richard Dreyfuss, Angela Sarafyan,\n",
      "    Released:2013,\n",
      "    Rating:PG-13,\n",
      "    Genere:Thrillers,\n",
      "\n",
      "    Description:Blackmailed by his company's CEO, a low-level employee finds himself forced to spy on the boss's rival and former mentor.\n",
      "    \n",
      "\n",
      "Next movie to watch\n",
      "\n",
      "    Type:Movie \n",
      "    Title:Croupier,\n",
      "    Director:Mike Hodges,\n",
      "    Cast:Clive Owen, Kate Hardie, Alex Kingston, Gina McKee, Nicholas Ball, Nick Reding, Alexander Morton,\n",
      "    Released:1998,\n",
      "    Rating:TV-MA,\n",
      "    Genere:Dramas, Independent Movies, Thrillers,\n",
      "\n",
      "    Description:A would-be writer lands a job as a croupier to make ends meet. But when he becomes involved with a gambler, he is lured into taking part in a heist.\n",
      "    \n",
      "\n",
      "Next movie to watch\n",
      "\n",
      "    Type:Movie \n",
      "    Title:The Game,\n",
      "    Director:David Fincher,\n",
      "    Cast:Michael Douglas, Sean Penn, Deborah Kara Unger, James Rebhorn, Peter Donat, Carroll Baker, Anna Katarina, Armin Mueller-Stahl,\n",
      "    Released:1997,\n",
      "    Rating:R,\n",
      "    Genere:Thrillers,\n",
      "\n",
      "    Description:An aloof investment banker's life spirals into peril and paranoia after his brother gives him an odd birthday gift: the chance to play a mysterious game.\n",
      "    \n",
      "\n",
      "Next movie to watch\n",
      "\n",
      "    Type:Movie \n",
      "    Title:Manorama Six Feet Under,\n",
      "    Director:Navdeep Singh,\n",
      "    Cast:Abhay Deol, Gul Panag, Raima Sen, Sarika, Kulbhushan Kharbanda, Vinay Pathak, Yana Gupta, Jogi, Brijendra Kala, Nawazuddin Siddiqui,\n",
      "    Released:2007,\n",
      "    Rating:TV-14,\n",
      "    Genere:Dramas, International Movies, Thrillers,\n",
      "\n",
      "    Description:A government employee and aspiring crime writer, who is under investigation for corruption, is asked by a politician's wife to spy on her husband.\n",
      "    \n",
      "\n",
      "Next movie to watch\n",
      "\n",
      "    Type:Movie \n",
      "    Title:Why Me?,\n",
      "    Director:Tudor Giurgiu,\n",
      "    Cast:Emilian Oprea, Mihai Constantin, Andreea Vasile, Dan Condurache, Liviu Pintileasa, Mihai Smarandache, Alin Florea, Lucretia Mandric,\n",
      "    Released:2015,\n",
      "    Rating:TV-MA,\n",
      "    Genere:Dramas, International Movies, Thrillers,\n",
      "\n",
      "    Description:A young prosecutor is assigned a career-making case involving a colleague but soon starts to question the motivations behind the charges.\n",
      "    \n",
      "\n"
     ]
    }
   ],
   "source": [
    "for i in best_matches:\n",
    "    print(\"Next movie to watch\")\n",
    "    print(i)\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f52665a-514b-4896-87e5-b31d5f8dab17",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "8ee5bf52-fb12-40a5-bb02-7dfd82810414",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([\"\\n    Type:Movie \\n    Title:Paranoia,\\n    Director:Robert Luketic,\\n    Cast:Liam Hemsworth, Gary Oldman, Amber Heard, Harrison Ford, Lucas Till, Embeth Davidtz, Julian McMahon, Josh Holloway, Richard Dreyfuss, Angela Sarafyan,\\n    Released:2013,\\n    Rating:PG-13,\\n    Genere:Thrillers,\\n\\n    Description:Blackmailed by his company's CEO, a low-level employee finds himself forced to spy on the boss's rival and former mentor.\\n    \",\n",
       "       '\\n    Type:Movie \\n    Title:Croupier,\\n    Director:Mike Hodges,\\n    Cast:Clive Owen, Kate Hardie, Alex Kingston, Gina McKee, Nicholas Ball, Nick Reding, Alexander Morton,\\n    Released:1998,\\n    Rating:TV-MA,\\n    Genere:Dramas, Independent Movies, Thrillers,\\n\\n    Description:A would-be writer lands a job as a croupier to make ends meet. But when he becomes involved with a gambler, he is lured into taking part in a heist.\\n    ',\n",
       "       \"\\n    Type:Movie \\n    Title:The Game,\\n    Director:David Fincher,\\n    Cast:Michael Douglas, Sean Penn, Deborah Kara Unger, James Rebhorn, Peter Donat, Carroll Baker, Anna Katarina, Armin Mueller-Stahl,\\n    Released:1997,\\n    Rating:R,\\n    Genere:Thrillers,\\n\\n    Description:An aloof investment banker's life spirals into peril and paranoia after his brother gives him an odd birthday gift: the chance to play a mysterious game.\\n    \",\n",
       "       \"\\n    Type:Movie \\n    Title:Manorama Six Feet Under,\\n    Director:Navdeep Singh,\\n    Cast:Abhay Deol, Gul Panag, Raima Sen, Sarika, Kulbhushan Kharbanda, Vinay Pathak, Yana Gupta, Jogi, Brijendra Kala, Nawazuddin Siddiqui,\\n    Released:2007,\\n    Rating:TV-14,\\n    Genere:Dramas, International Movies, Thrillers,\\n\\n    Description:A government employee and aspiring crime writer, who is under investigation for corruption, is asked by a politician's wife to spy on her husband.\\n    \",\n",
       "       '\\n    Type:Movie \\n    Title:Why Me?,\\n    Director:Tudor Giurgiu,\\n    Cast:Emilian Oprea, Mihai Constantin, Andreea Vasile, Dan Condurache, Liviu Pintileasa, Mihai Smarandache, Alin Florea, Lucretia Mandric,\\n    Released:2015,\\n    Rating:TV-MA,\\n    Genere:Dramas, International Movies, Thrillers,\\n\\n    Description:A young prosecutor is assigned a career-making case involving a colleague but soon starts to question the motivations behind the charges.\\n    '],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_matches"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "7404ea52-afe2-48fc-bc35-60339c2dcd8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\n",
      "    {\n",
      "        \"Type\": \"Movie\",\n",
      "        \"Title\": \"Paranoia\",\n",
      "        \"Director\": \"Robert Luketic\",\n",
      "        \"Cast\": [\n",
      "            \"Liam Hemsworth\",\n",
      "            \"Gary Oldman\",\n",
      "            \"Amber Heard\",\n",
      "            \"Harrison Ford\",\n",
      "            \"Lucas Till\",\n",
      "            \"Embeth Davidtz\",\n",
      "            \"Julian McMahon\",\n",
      "            \"Josh Holloway\",\n",
      "            \"Richard Dreyfuss\",\n",
      "            \"Angela Sarafyan\"\n",
      "        ],\n",
      "        \"Released\": 2013,\n",
      "        \"Rating\": \"PG-13\",\n",
      "        \"Description\": \"Blackmailed by his company's CEO, a low-level employee finds himself forced to spy on the boss's rival and former mentor.\"\n",
      "    },\n",
      "    {\n",
      "        \"Type\": \"Movie\",\n",
      "        \"Title\": \"Croupier\",\n",
      "        \"Director\": \"Mike Hodges\",\n",
      "        \"Cast\": [\n",
      "            \"Clive Owen\",\n",
      "            \"Kate Hardie\",\n",
      "            \"Alex Kingston\",\n",
      "            \"Gina McKee\",\n",
      "            \"Nicholas Ball\",\n",
      "            \"Nick Reding\",\n",
      "            \"Alexander Morton\"\n",
      "        ],\n",
      "        \"Released\": 1998,\n",
      "        \"Rating\": \"TV-MA\",\n",
      "        \"Description\": \"A would-be writer lands a job as a croupier to make ends meet. But when he becomes involved with a gambler, he is lured into taking part in a heist.\"\n",
      "    },\n",
      "    {\n",
      "        \"Type\": \"Movie\",\n",
      "        \"Title\": \"The Game\",\n",
      "        \"Director\": \"David Fincher\",\n",
      "        \"Cast\": [\n",
      "            \"Michael Douglas\",\n",
      "            \"Sean Penn\",\n",
      "            \"Deborah Kara Unger\",\n",
      "            \"James Rebhorn\",\n",
      "            \"Peter Donat\",\n",
      "            \"Carroll Baker\",\n",
      "            \"Anna Katarina\",\n",
      "            \"Armin Mueller-Stahl\"\n",
      "        ],\n",
      "        \"Released\": 1997,\n",
      "        \"Rating\": \"R\",\n",
      "        \"Description\": \"An aloof investment banker's life spirals into peril and paranoia after his brother gives him an odd birthday gift: the chance to play a mysterious game.\"\n",
      "    },\n",
      "    {\n",
      "        \"Type\": \"Movie\",\n",
      "        \"Title\": \"Manorama Six Feet Under\",\n",
      "        \"Director\": \"Navdeep Singh\",\n",
      "        \"Cast\": [\n",
      "            \"Abhay Deol\",\n",
      "            \"Gul Panag\",\n",
      "            \"Raima Sen\",\n",
      "            \"Sarika\",\n",
      "            \"Kulbhushan Kharbanda\",\n",
      "            \"Vinay Pathak\",\n",
      "            \"Yana Gupta\",\n",
      "            \"Jogi\",\n",
      "            \"Brijendra Kala\",\n",
      "            \"Nawazuddin Siddiqui\"\n",
      "        ],\n",
      "        \"Released\": 2007,\n",
      "        \"Rating\": \"TV-14\",\n",
      "        \"Description\": \"A government employee and aspiring crime writer, who is under investigation for corruption, is asked by a politician's wife to spy on her husband.\"\n",
      "    },\n",
      "    {\n",
      "        \"Type\": \"Movie\",\n",
      "        \"Title\": \"Why Me?\",\n",
      "        \"Director\": \"Tudor Giurgiu\",\n",
      "        \"Cast\": [\n",
      "            \"Emilian Oprea\",\n",
      "            \"Mihai Constantin\",\n",
      "            \"Andreea Vasile\",\n",
      "            \"Dan Condurache\",\n",
      "            \"Liviu Pintileasa\",\n",
      "            \"Mihai Smarandache\",\n",
      "            \"Alin Florea\",\n",
      "            \"Lucretia Mandric\"\n",
      "        ],\n",
      "        \"Released\": 2015,\n",
      "        \"Rating\": \"TV-MA\",\n",
      "        \"Description\": \"A young prosecutor is assigned a career-making case involving a colleague but soon starts to question the motivations behind the charges.\"\n",
      "    }\n",
      "]\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "# Assuming `best_matches` contains the movie strings as shown\n",
    "recommendations = []\n",
    "for i in best_matches:\n",
    "    movie = {}\n",
    "    lines = i.split('\\n')\n",
    "    \n",
    "    for line in lines:\n",
    "        line = line.strip()  # Remove leading and trailing whitespace\n",
    "        if line.startswith(\"Type:\"):\n",
    "            movie[\"Type\"] = line.replace(\"Type:\", \"\").strip()\n",
    "        elif line.startswith(\"Title:\"):\n",
    "            movie[\"Title\"] = line.replace(\"Title:\", \"\").strip().rstrip(',')\n",
    "        elif line.startswith(\"Director:\"):\n",
    "            movie[\"Director\"] = line.replace(\"Director:\", \"\").strip().rstrip(',')\n",
    "        elif line.startswith(\"Cast:\"):\n",
    "            movie[\"Cast\"] = [actor.strip() for actor in line.replace(\"Cast:\", \"\").strip().rstrip(',').split(\",\")]\n",
    "        elif line.startswith(\"Released:\"):\n",
    "            movie[\"Released\"] = int(line.replace(\"Released:\", \"\").strip().rstrip(','))\n",
    "        elif line.startswith(\"Rating:\"):\n",
    "            movie[\"Rating\"] = line.replace(\"Rating:\", \"\").strip().rstrip(',')\n",
    "        elif line.startswith(\"Genre:\"):\n",
    "            movie[\"Genre\"] = [genre.strip() for genre in line.replace(\"Genre:\", \"\").strip().rstrip(',').split(\",\")]\n",
    "        elif line.startswith(\"Description:\"):\n",
    "            movie[\"Description\"] = line.replace(\"Description:\", \"\").strip()\n",
    "\n",
    "    recommendations.append(movie)\n",
    "\n",
    "# Convert to JSON\n",
    "json_output = json.dumps(recommendations, indent=4)\n",
    "\n",
    "# Save to file\n",
    "with open('recommendations.json', 'w') as file:\n",
    "    file.write(json_output)\n",
    "\n",
    "print(json_output)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dfc157fc-f092-4d91-803b-95f35f46c153",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
