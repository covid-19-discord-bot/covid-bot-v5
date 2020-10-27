# coding=utf-8
class AllWorldometers:
    def __init__(self):
        self.api_request_url = "https://disease.sh/v3/covid-19/all?allowNull=true"
        self.example_response = '''{
  "updated": 1603500523547,
  "cases": 42462925,
  "todayCases": 489630,
  "deaths": 1148698,
  "todayDeaths": 6526,
  "recovered": 31417499,
  "todayRecovered": 239545,
  "active": 9896728,
  "critical": 76321,
  "casesPerOneMillion": 5448,
  "deathsPerOneMillion": 147.4,
  "tests": 771052407,
  "testsPerOneMillion": 99075.47,
  "population": 7782475162,
  "oneCasePerPeople": null,
  "oneDeathPerPeople": null,
  "oneTestPerPeople": null,
  "activePerOneMillion": 1271.67,
  "recoveredPerOneMillion": 4036.95,
  "criticalPerOneMillion": 9.81,
  "affectedCountries": 217
}'''


class USStatesWorldometers:
    def __init__(self):
        self.request_url = "https://disease.sh/v3/covid-19/states?allowNull=true"
        self.example_response = '''[
  {
    "state": "Texas",
    "updated": 1603500517146,
    "cases": 903286,
    "todayCases": 6483,
    "deaths": 17954,
    "todayDeaths": 76,
    "recovered": 764138,
    "active": 121194,
    "casesPerOneMillion": 31152,
    "deathsPerOneMillion": 619,
    "tests": 8338444,
    "testsPerOneMillion": 287573,
    "population": 28995881
  },
  {
    "state": "California",
    "updated": 1603500517146,
    "cases": 900458,
    "todayCases": 5851,
    "deaths": 17317,
    "todayDeaths": 52,
    "recovered": 463817,
    "active": 419324,
    "casesPerOneMillion": 22789,
    "deathsPerOneMillion": 438,
    "tests": 17483293,
    "testsPerOneMillion": 442478,
    "population": 39512223
  },
  {
    "state": "Florida",
    "updated": 1603500517146,
    "cases": 771780,
    "todayCases": 3689,
    "deaths": 16349,
    "todayDeaths": 76,
    "recovered": 524920,
    "active": 230511,
    "casesPerOneMillion": 35934,
    "deathsPerOneMillion": 761,
    "tests": 5873041,
    "testsPerOneMillion": 273448,
    "population": 21477737
  },
  {
    "state": "New York",
    "updated": 1603500517146,
    "cases": 528037,
    "todayCases": 1756,
    "deaths": 33549,
    "todayDeaths": 13,
    "recovered": 413757,
    "active": 80731,
    "casesPerOneMillion": 27143,
    "deathsPerOneMillion": 1725,
    "tests": 13474353,
    "testsPerOneMillion": 692642,
    "population": 19453561
  },
  {
    "state": "Illinois",
    "updated": 1603500517146,
    "cases": 368746,
    "todayCases": 4035,
    "deaths": 9688,
    "todayDeaths": 41,
    "recovered": 266031,
    "active": 93027,
    "casesPerOneMillion": 29100,
    "deathsPerOneMillion": 765,
    "tests": 7113338,
    "testsPerOneMillion": 561351,
    "population": 12671821
  },
  {
    "state": "Georgia",
    "updated": 1603500517147,
    "cases": 347759,
    "todayCases": 2224,
    "deaths": 7766,
    "todayDeaths": 37,
    "recovered": 177382,
    "active": 162611,
    "casesPerOneMillion": 32754,
    "deathsPerOneMillion": 731,
    "tests": 3731541,
    "testsPerOneMillion": 351454,
    "population": 10617423
  },
  {
    "state": "North Carolina",
    "updated": 1603500517147,
    "cases": 255708,
    "todayCases": 2716,
    "deaths": 4114,
    "todayDeaths": 32,
    "recovered": 218541,
    "active": 33053,
    "casesPerOneMillion": 24381,
    "deathsPerOneMillion": 392,
    "tests": 3753953,
    "testsPerOneMillion": 357926,
    "population": 10488084
  },
  {
    "state": "Tennessee",
    "updated": 1603500517147,
    "cases": 241513,
    "todayCases": 3606,
    "deaths": 3076,
    "todayDeaths": 65,
    "recovered": 214634,
    "active": 23803,
    "casesPerOneMillion": 35365,
    "deathsPerOneMillion": 450,
    "tests": 3465912,
    "testsPerOneMillion": 507516,
    "population": 6829174
  },
  {
    "state": "Arizona",
    "updated": 1603500517147,
    "cases": 235882,
    "todayCases": 976,
    "deaths": 5865,
    "todayDeaths": 6,
    "recovered": 39306,
    "active": 190711,
    "casesPerOneMillion": 32407,
    "deathsPerOneMillion": 806,
    "tests": 1993389,
    "testsPerOneMillion": 273865,
    "population": 7278717
  },
  {
    "state": "New Jersey",
    "updated": 1603500517147,
    "cases": 229825,
    "todayCases": 1192,
    "deaths": 16398,
    "todayDeaths": 8,
    "recovered": 178800,
    "active": 34627,
    "casesPerOneMillion": 25875,
    "deathsPerOneMillion": 1846,
    "tests": 4337985,
    "testsPerOneMillion": 488391,
    "population": 8882190
  },
  {
    "state": "Pennsylvania",
    "updated": 1603500517147,
    "cases": 195659,
    "todayCases": 2258,
    "deaths": 8703,
    "todayDeaths": 34,
    "recovered": 148804,
    "active": 38152,
    "casesPerOneMillion": 15283,
    "deathsPerOneMillion": 680,
    "tests": 2530658,
    "testsPerOneMillion": 197677,
    "population": 12801989
  },
  {
    "state": "Ohio",
    "updated": 1603500517147,
    "cases": 193038,
    "todayCases": 2535,
    "deaths": 5218,
    "todayDeaths": 22,
    "recovered": 156421,
    "active": 31399,
    "casesPerOneMillion": 16514,
    "deathsPerOneMillion": 446,
    "tests": 4090314,
    "testsPerOneMillion": 349925,
    "population": 11689100
  },
  {
    "state": "Wisconsin",
    "updated": 1603500517147,
    "cases": 190478,
    "todayCases": 4378,
    "deaths": 1745,
    "todayDeaths": 42,
    "recovered": 149534,
    "active": 39199,
    "casesPerOneMillion": 32714,
    "deathsPerOneMillion": 300,
    "tests": 1934550,
    "testsPerOneMillion": 332258,
    "population": 5822434
  },
  {
    "state": "Alabama",
    "updated": 1603500517147,
    "cases": 180916,
    "todayCases": 1287,
    "deaths": 2859,
    "todayDeaths": 16,
    "recovered": 74439,
    "active": 103618,
    "casesPerOneMillion": 36898,
    "deathsPerOneMillion": 583,
    "tests": 1352271,
    "testsPerOneMillion": 275794,
    "population": 4903185
  },
  {
    "state": "Louisiana",
    "updated": 1603500517147,
    "cases": 178870,
    "todayCases": 699,
    "deaths": 5820,
    "todayDeaths": 21,
    "recovered": 165282,
    "active": 7768,
    "casesPerOneMillion": 38477,
    "deathsPerOneMillion": 1252,
    "tests": 2667505,
    "testsPerOneMillion": 573806,
    "population": 4648794
  },
  {
    "state": "Michigan",
    "updated": 1603500517147,
    "cases": 172122,
    "todayCases": 2046,
    "deaths": 7484,
    "todayDeaths": 20,
    "recovered": 109539,
    "active": 55099,
    "casesPerOneMillion": 17235,
    "deathsPerOneMillion": 749,
    "tests": 4883659,
    "testsPerOneMillion": 489009,
    "population": 9986857
  },
  {
    "state": "Virginia",
    "updated": 1603500517147,
    "cases": 171284,
    "todayCases": 1180,
    "deaths": 3539,
    "todayDeaths": 15,
    "recovered": 19406,
    "active": 148339,
    "casesPerOneMillion": 20067,
    "deathsPerOneMillion": 415,
    "tests": 2662896,
    "testsPerOneMillion": 311978,
    "population": 8535519
  },
  {
    "state": "Missouri",
    "updated": 1603500517147,
    "cases": 171085,
    "todayCases": 1892,
    "deaths": 2789,
    "todayDeaths": 26,
    "recovered": 40728,
    "active": 127568,
    "casesPerOneMillion": 27876,
    "deathsPerOneMillion": 454,
    "tests": 2477724,
    "testsPerOneMillion": 403707,
    "population": 6137428
  },
  {
    "state": "South Carolina",
    "updated": 1603500517147,
    "cases": 168549,
    "todayCases": 1064,
    "deaths": 3777,
    "todayDeaths": 22,
    "recovered": 85420,
    "active": 79352,
    "casesPerOneMillion": 32736,
    "deathsPerOneMillion": 734,
    "tests": 1838134,
    "testsPerOneMillion": 357008,
    "population": 5148714
  },
  {
    "state": "Indiana",
    "updated": 1603500517147,
    "cases": 157713,
    "todayCases": 2467,
    "deaths": 4092,
    "todayDeaths": 27,
    "recovered": 112914,
    "active": 40707,
    "casesPerOneMillion": 23427,
    "deathsPerOneMillion": 608,
    "tests": 2642522,
    "testsPerOneMillion": 392519,
    "population": 6732219
  },
  {
    "state": "Massachusetts",
    "updated": 1603500517147,
    "cases": 148285,
    "todayCases": 1070,
    "deaths": 9830,
    "todayDeaths": 20,
    "recovered": 122856,
    "active": 15599,
    "casesPerOneMillion": 21514,
    "deathsPerOneMillion": 1426,
    "tests": 2893276,
    "testsPerOneMillion": 419771,
    "population": 6892503
  },
  {
    "state": "Maryland",
    "updated": 1603500517147,
    "cases": 138691,
    "todayCases": 712,
    "deaths": 4078,
    "todayDeaths": 8,
    "recovered": 8030,
    "active": 126583,
    "casesPerOneMillion": 22941,
    "deathsPerOneMillion": 675,
    "tests": 3201774,
    "testsPerOneMillion": 529597,
    "population": 6045680
  },
  {
    "state": "Minnesota",
    "updated": 1603500517147,
    "cases": 129863,
    "todayCases": 1711,
    "deaths": 2367,
    "todayDeaths": 13,
    "recovered": 114679,
    "active": 12817,
    "casesPerOneMillion": 23027,
    "deathsPerOneMillion": 420,
    "tests": 2614124,
    "testsPerOneMillion": 463527,
    "population": 5639632
  },
  {
    "state": "Mississippi",
    "updated": 1603500517147,
    "cases": 113876,
    "todayCases": 795,
    "deaths": 3238,
    "todayDeaths": 7,
    "recovered": 97675,
    "active": 12963,
    "casesPerOneMillion": 38263,
    "deathsPerOneMillion": 1088,
    "tests": 941532,
    "testsPerOneMillion": 316359,
    "population": 2976149
  },
  {
    "state": "Oklahoma",
    "updated": 1603500517147,
    "cases": 113856,
    "todayCases": 1373,
    "deaths": 1234,
    "todayDeaths": 13,
    "recovered": 97490,
    "active": 15132,
    "casesPerOneMillion": 28774,
    "deathsPerOneMillion": 312,
    "tests": 1525561,
    "testsPerOneMillion": 385538,
    "population": 3956971
  },
  {
    "state": "Iowa",
    "updated": 1603500517147,
    "cases": 112928,
    "todayCases": 1111,
    "deaths": 1621,
    "todayDeaths": 20,
    "recovered": 86651,
    "active": 24656,
    "casesPerOneMillion": 35793,
    "deathsPerOneMillion": 514,
    "tests": 925926,
    "testsPerOneMillion": 293472,
    "population": 3155070
  },
  {
    "state": "Washington",
    "updated": 1603500517147,
    "cases": 104867,
    "todayCases": 806,
    "deaths": 2299,
    "todayDeaths": 8,
    "recovered": 49058,
    "active": 53510,
    "casesPerOneMillion": 13771,
    "deathsPerOneMillion": 302,
    "tests": 2318931,
    "testsPerOneMillion": 304526,
    "population": 7614893
  },
  {
    "state": "Arkansas",
    "updated": 1603500517147,
    "cases": 104135,
    "todayCases": 1337,
    "deaths": 1782,
    "todayDeaths": 10,
    "recovered": 93215,
    "active": 9138,
    "casesPerOneMillion": 34507,
    "deathsPerOneMillion": 590,
    "tests": 1312167,
    "testsPerOneMillion": 434809,
    "population": 3017804
  },
  {
    "state": "Utah",
    "updated": 1603500517147,
    "cases": 101509,
    "todayCases": 1960,
    "deaths": 567,
    "todayDeaths": 4,
    "recovered": 74688,
    "active": 26254,
    "casesPerOneMillion": 31663,
    "deathsPerOneMillion": 177,
    "tests": 1364473,
    "testsPerOneMillion": 425605,
    "population": 3205958
  },
  {
    "state": "Kentucky",
    "updated": 1603500517147,
    "cases": 93748,
    "todayCases": 1449,
    "deaths": 1396,
    "todayDeaths": 16,
    "recovered": 17722,
    "active": 74630,
    "casesPerOneMillion": 20984,
    "deathsPerOneMillion": 312,
    "tests": 1887520,
    "testsPerOneMillion": 422484,
    "population": 4467673
  },
  {
    "state": "Nevada",
    "updated": 1603500517147,
    "cases": 93666,
    "todayCases": 813,
    "deaths": 1738,
    "todayDeaths": 2,
    "recovered": 68699,
    "active": 23229,
    "casesPerOneMillion": 30409,
    "deathsPerOneMillion": 564,
    "tests": 1185069,
    "testsPerOneMillion": 384743,
    "population": 3080156
  },
  {
    "state": "Colorado",
    "updated": 1603500517147,
    "cases": 91572,
    "todayCases": 1350,
    "deaths": 2211,
    "todayDeaths": 13,
    "recovered": 41931,
    "active": 47430,
    "casesPerOneMillion": 15901,
    "deathsPerOneMillion": 384,
    "tests": 1124409,
    "testsPerOneMillion": 195253,
    "population": 5758736
  },
  {
    "state": "Kansas",
    "updated": 1603500517147,
    "cases": 76230,
    "todayCases": 363,
    "deaths": 975,
    "todayDeaths": 23,
    "recovered": 59660,
    "active": 15595,
    "casesPerOneMillion": 26166,
    "deathsPerOneMillion": 335,
    "tests": 616262,
    "testsPerOneMillion": 211533,
    "population": 2913314
  },
  {
    "state": "Connecticut",
    "updated": 1603500517147,
    "cases": 66052,
    "todayCases": 679,
    "deaths": 4577,
    "todayDeaths": 8,
    "recovered": 44002,
    "active": 17473,
    "casesPerOneMillion": 18526,
    "deathsPerOneMillion": 1284,
    "tests": 2113068,
    "testsPerOneMillion": 592678,
    "population": 3565287
  },
  {
    "state": "Nebraska",
    "updated": 1603500517147,
    "cases": 62510,
    "todayCases": 1225,
    "deaths": 591,
    "todayDeaths": 4,
    "recovered": 41008,
    "active": 20911,
    "casesPerOneMillion": 32315,
    "deathsPerOneMillion": 306,
    "tests": 564589,
    "testsPerOneMillion": 291867,
    "population": 1934408
  },
  {
    "state": "Idaho",
    "updated": 1603500517147,
    "cases": 57673,
    "todayCases": 1073,
    "deaths": 562,
    "todayDeaths": 9,
    "recovered": 27509,
    "active": 29602,
    "casesPerOneMillion": 32272,
    "deathsPerOneMillion": 314,
    "tests": 366047,
    "testsPerOneMillion": 204831,
    "population": 1787065
  },
  {
    "state": "Oregon",
    "updated": 1603500517147,
    "cases": 41348,
    "todayCases": 538,
    "deaths": 649,
    "todayDeaths": 3,
    "recovered": null,
    "active": null,
    "casesPerOneMillion": 9803,
    "deathsPerOneMillion": 154,
    "tests": 813114,
    "testsPerOneMillion": 192784,
    "population": 4217737
  },
  {
    "state": "New Mexico",
    "updated": 1603500517147,
    "cases": 40168,
    "todayCases": 791,
    "deaths": 960,
    "todayDeaths": 7,
    "recovered": 20655,
    "active": 18553,
    "casesPerOneMillion": 19157,
    "deathsPerOneMillion": 458,
    "tests": 1099484,
    "testsPerOneMillion": 524356,
    "population": 2096829
  },
  {
    "state": "South Dakota",
    "updated": 1603500517147,
    "cases": 37202,
    "todayCases": 1185,
    "deaths": 356,
    "todayDeaths": 9,
    "recovered": 26984,
    "active": 9862,
    "casesPerOneMillion": 42052,
    "deathsPerOneMillion": 402,
    "tests": 241002,
    "testsPerOneMillion": 272424,
    "population": 884659
  },
  {
    "state": "North Dakota",
    "updated": 1603500517147,
    "cases": 35939,
    "todayCases": 887,
    "deaths": 440,
    "todayDeaths": 9,
    "recovered": 29136,
    "active": 6363,
    "casesPerOneMillion": 47160,
    "deathsPerOneMillion": 577,
    "tests": 279702,
    "testsPerOneMillion": 367033,
    "population": 762062
  },
  {
    "state": "Rhode Island",
    "updated": 1603500517147,
    "cases": 30118,
    "todayCases": 524,
    "deaths": 1177,
    "todayDeaths": 4,
    "recovered": 2602,
    "active": 26339,
    "casesPerOneMillion": 28430,
    "deathsPerOneMillion": 1111,
    "tests": 1034572,
    "testsPerOneMillion": 976600,
    "population": 1059361
  },
  {
    "state": "Montana",
    "updated": 1603500517147,
    "cases": 26503,
    "todayCases": 863,
    "deaths": 282,
    "todayDeaths": 4,
    "recovered": 16611,
    "active": 9610,
    "casesPerOneMillion": 24797,
    "deathsPerOneMillion": 264,
    "tests": 461000,
    "testsPerOneMillion": 431334,
    "population": 1068778
  },
  {
    "state": "Delaware",
    "updated": 1603500517147,
    "cases": 23687,
    "todayCases": 159,
    "deaths": 678,
    "todayDeaths": 8,
    "recovered": 12493,
    "active": 10516,
    "casesPerOneMillion": 24325,
    "deathsPerOneMillion": 696,
    "tests": 333992,
    "testsPerOneMillion": 342991,
    "population": 973764
  },
  {
    "state": "West Virginia",
    "updated": 1603500517147,
    "cases": 21392,
    "todayCases": 335,
    "deaths": 422,
    "todayDeaths": 4,
    "recovered": 16368,
    "active": 4602,
    "casesPerOneMillion": 11937,
    "deathsPerOneMillion": 235,
    "tests": 709156,
    "testsPerOneMillion": 395702,
    "population": 1792147
  },
  {
    "state": "District Of Columbia",
    "updated": 1603500517147,
    "cases": 16609,
    "todayCases": 72,
    "deaths": 642,
    "todayDeaths": null,
    "recovered": 13028,
    "active": 2939,
    "casesPerOneMillion": 23534,
    "deathsPerOneMillion": 910,
    "tests": 485753,
    "testsPerOneMillion": 688280,
    "population": 705749
  },
  {
    "state": "Hawaii",
    "updated": 1603500517147,
    "cases": 14464,
    "todayCases": 129,
    "deaths": 209,
    "todayDeaths": 3,
    "recovered": 11292,
    "active": 2963,
    "casesPerOneMillion": 10216,
    "deathsPerOneMillion": 148,
    "tests": 491450,
    "testsPerOneMillion": 347101,
    "population": 1415872
  },
  {
    "state": "Alaska",
    "updated": 1603500517147,
    "cases": 12118,
    "todayCases": 281,
    "deaths": 68,
    "todayDeaths": null,
    "recovered": 6270,
    "active": 5780,
    "casesPerOneMillion": 16565,
    "deathsPerOneMillion": 93,
    "tests": 552746,
    "testsPerOneMillion": 755587,
    "population": 731545
  },
  {
    "state": "Wyoming",
    "updated": 1603500517147,
    "cases": 10545,
    "todayCases": 426,
    "deaths": 68,
    "todayDeaths": null,
    "recovered": 7357,
    "active": 3120,
    "casesPerOneMillion": 18220,
    "deathsPerOneMillion": 117,
    "tests": 230477,
    "testsPerOneMillion": 398226,
    "population": 578759
  },
  {
    "state": "New Hampshire",
    "updated": 1603500517147,
    "cases": 10112,
    "todayCases": 118,
    "deaths": 471,
    "todayDeaths": 1,
    "recovered": 8745,
    "active": 896,
    "casesPerOneMillion": 7437,
    "deathsPerOneMillion": 346,
    "tests": 358070,
    "testsPerOneMillion": 263343,
    "population": 1359711
  },
  {
    "state": "Maine",
    "updated": 1603500517147,
    "cases": 6095,
    "todayCases": 31,
    "deaths": 146,
    "todayDeaths": null,
    "recovered": 5307,
    "active": 642,
    "casesPerOneMillion": 4534,
    "deathsPerOneMillion": 109,
    "tests": 577139,
    "testsPerOneMillion": 429351,
    "population": 1344212
  },
  {
    "state": "Vermont",
    "updated": 1603500517147,
    "cases": 2016,
    "todayCases": 29,
    "deaths": 58,
    "todayDeaths": null,
    "recovered": 1723,
    "active": 235,
    "casesPerOneMillion": 3231,
    "deathsPerOneMillion": 93,
    "tests": 182943,
    "testsPerOneMillion": 293183,
    "population": 623989
  },
  {
    "state": "Puerto Rico",
    "updated": 1603500517147,
    "cases": 60984,
    "todayCases": 1947,
    "deaths": 791,
    "todayDeaths": 8,
    "recovered": null,
    "active": null,
    "casesPerOneMillion": 18006,
    "deathsPerOneMillion": 234,
    "tests": 464073,
    "testsPerOneMillion": 137018,
    "population": 3386941
  },
  {
    "state": "Guam",
    "updated": 1603500517147,
    "cases": 4141,
    "todayCases": 85,
    "deaths": 69,
    "todayDeaths": null,
    "recovered": 2471,
    "active": 1601,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": 62488,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "United States Virgin Islands",
    "updated": 1603500517147,
    "cases": 1346,
    "todayCases": 3,
    "deaths": 21,
    "todayDeaths": null,
    "recovered": 1305,
    "active": 20,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": 23463,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "Northern Mariana Islands",
    "updated": 1603500517147,
    "cases": 88,
    "todayCases": null,
    "deaths": 2,
    "todayDeaths": null,
    "recovered": 29,
    "active": 57,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": 22212,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "US Military",
    "updated": 1603500517147,
    "cases": 78227,
    "todayCases": 1743,
    "deaths": 103,
    "todayDeaths": 1,
    "recovered": 52738,
    "active": 25386,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": null,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "Veteran Affairs",
    "updated": 1603500517147,
    "cases": 71227,
    "todayCases": 636,
    "deaths": 3797,
    "todayDeaths": 12,
    "recovered": 62448,
    "active": 4982,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": 820709,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "Federal Prisons",
    "updated": 1603500517148,
    "cases": 19148,
    "todayCases": 142,
    "deaths": 130,
    "todayDeaths": 1,
    "recovered": 16277,
    "active": 2741,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": 67411,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "Navajo Nation",
    "updated": 1603500517148,
    "cases": 11101,
    "todayCases": 71,
    "deaths": 574,
    "todayDeaths": null,
    "recovered": 7429,
    "active": 3098,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": 119359,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "Grand Princess Ship",
    "updated": 1603500517148,
    "cases": 103,
    "todayCases": null,
    "deaths": 3,
    "todayDeaths": null,
    "recovered": null,
    "active": 100,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": null,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "Wuhan Repatriated",
    "updated": 1603500517148,
    "cases": 3,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": null,
    "active": 3,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": 3,
    "testsPerOneMillion": null,
    "population": null
  },
  {
    "state": "Diamond Princess Ship",
    "updated": 1603500517148,
    "cases": 46,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": null,
    "active": 46,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": 46,
    "testsPerOneMillion": null,
    "population": null
  }
]'''


class ContinentsWorldometers:
    def __init__(self):
        self.request_url = "https://disease.sh/v3/covid-19/continents?allowNull=true"
        self.example_response = '''[
  {
    "updated": 1603500524335,
    "cases": 10475661,
    "todayCases": 93913,
    "deaths": 341516,
    "todayDeaths": 1462,
    "recovered": 6978737,
    "todayRecovered": 52480,
    "active": 3155408,
    "critical": 19846,
    "casesPerOneMillion": 17738.89,
    "deathsPerOneMillion": 578.3,
    "tests": 146647805,
    "testsPerOneMillion": 248325.12,
    "population": 590547609,
    "continent": "North America",
    "activePerOneMillion": 5343.19,
    "recoveredPerOneMillion": 11817.4,
    "criticalPerOneMillion": 33.61,
    "continentInfo": {
      "lat": 31.6768272,
      "long": -146.4707474
    },
    "countries": [
      "Anguilla",
      "Antigua and Barbuda",
      "Aruba",
      "Bahamas",
      "Barbados",
      "Belize",
      "Bermuda",
      "British Virgin Islands",
      "Canada",
      "Caribbean Netherlands",
      "Cayman Islands",
      "Costa Rica",
      "Cuba",
      "Cura\u00e7ao",
      "Dominica",
      "Dominican Republic",
      "El Salvador",
      "Greenland",
      "Grenada",
      "Guadeloupe",
      "Guatemala",
      "Haiti",
      "Honduras",
      "Jamaica",
      "Martinique",
      "Mexico",
      "Montserrat",
      "Nicaragua",
      "Panama",
      "Saint Kitts and Nevis",
      "Saint Lucia",
      "Saint Martin",
      "Saint Pierre Miquelon",
      "Saint Vincent and the Grenadines",
      "Sint Maarten",
      "St. Barth",
      "Trinidad and Tobago",
      "Turks and Caicos Islands",
      "USA"
    ]
  },
  {
    "updated": 1603500524336,
    "cases": 12981587,
    "todayCases": 97753,
    "deaths": 231693,
    "todayDeaths": 1579,
    "recovered": 11401500,
    "todayRecovered": 96594,
    "active": 1348394,
    "critical": 21089,
    "casesPerOneMillion": 2809.78,
    "deathsPerOneMillion": 50.15,
    "tests": 354644000,
    "testsPerOneMillion": 76760.35,
    "population": 4620145977,
    "continent": "Asia",
    "activePerOneMillion": 291.85,
    "recoveredPerOneMillion": 2467.78,
    "criticalPerOneMillion": 4.56,
    "continentInfo": {
      "lat": 23.7027273,
      "long": 62.3750637
    },
    "countries": [
      "Afghanistan",
      "Armenia",
      "Azerbaijan",
      "Bahrain",
      "Bangladesh",
      "Bhutan",
      "Brunei",
      "Cambodia",
      "China",
      "Cyprus",
      "Georgia",
      "Hong Kong",
      "India",
      "Indonesia",
      "Iran",
      "Iraq",
      "Israel",
      "Japan",
      "Jordan",
      "Kazakhstan",
      "Kuwait",
      "Kyrgyzstan",
      "Lao People's Democratic Republic",
      "Lebanon",
      "Macao",
      "Malaysia",
      "Maldives",
      "Mongolia",
      "Myanmar",
      "Nepal",
      "Oman",
      "Pakistan",
      "Palestine",
      "Philippines",
      "Qatar",
      "S. Korea",
      "Saudi Arabia",
      "Singapore",
      "Sri Lanka",
      "Syrian Arab Republic",
      "Taiwan",
      "Tajikistan",
      "Thailand",
      "Timor-Leste",
      "Turkey",
      "UAE",
      "Uzbekistan",
      "Vietnam",
      "Yemen"
    ]
  },
  {
    "updated": 1603500524337,
    "cases": 9273610,
    "todayCases": 55341,
    "deaths": 286042,
    "todayDeaths": 1279,
    "recovered": 8220442,
    "todayRecovered": 42047,
    "active": 767126,
    "critical": 17856,
    "casesPerOneMillion": 21473.28,
    "deathsPerOneMillion": 662.34,
    "tests": 41344534,
    "testsPerOneMillion": 95734.32,
    "population": 431867433,
    "continent": "South America",
    "activePerOneMillion": 1776.3,
    "recoveredPerOneMillion": 19034.64,
    "criticalPerOneMillion": 41.35,
    "continentInfo": {
      "lat": -15.6551563,
      "long": -100.7484231
    },
    "countries": [
      "Argentina",
      "Bolivia",
      "Brazil",
      "Chile",
      "Colombia",
      "Ecuador",
      "Falkland Islands (Malvinas)",
      "French Guiana",
      "Guyana",
      "Paraguay",
      "Peru",
      "Suriname",
      "Uruguay",
      "Venezuela"
    ]
  },
  {
    "updated": 1603500524338,
    "cases": 7988512,
    "todayCases": 231396,
    "deaths": 247488,
    "todayDeaths": 1980,
    "recovered": 3386759,
    "todayRecovered": 40939,
    "active": 4354265,
    "critical": 15446,
    "casesPerOneMillion": 10683.07,
    "deathsPerOneMillion": 330.97,
    "tests": 202696725,
    "testsPerOneMillion": 271067.07,
    "population": 747773315,
    "continent": "Europe",
    "activePerOneMillion": 5822.97,
    "recoveredPerOneMillion": 4529.13,
    "criticalPerOneMillion": 20.66,
    "continentInfo": {
      "lat": 25.771324,
      "long": -35.6012256
    },
    "countries": [
      "Albania",
      "Andorra",
      "Austria",
      "Belarus",
      "Belgium",
      "Bosnia",
      "Bulgaria",
      "Channel Islands",
      "Croatia",
      "Czechia",
      "Denmark",
      "Estonia",
      "Faroe Islands",
      "Finland",
      "France",
      "Germany",
      "Gibraltar",
      "Greece",
      "Holy See (Vatican City State)",
      "Hungary",
      "Iceland",
      "Ireland",
      "Isle of Man",
      "Italy",
      "Latvia",
      "Liechtenstein",
      "Lithuania",
      "Luxembourg",
      "Macedonia",
      "Malta",
      "Moldova",
      "Monaco",
      "Montenegro",
      "Netherlands",
      "Norway",
      "Poland",
      "Portugal",
      "Romania",
      "Russia",
      "San Marino",
      "Serbia",
      "Slovakia",
      "Slovenia",
      "Spain",
      "Sweden",
      "Switzerland",
      "UK",
      "Ukraine"
    ]
  },
  {
    "updated": 1603500524339,
    "cases": 1706982,
    "todayCases": 10564,
    "deaths": 40985,
    "todayDeaths": 225,
    "recovered": 1398172,
    "todayRecovered": 7386,
    "active": 267825,
    "critical": 2063,
    "casesPerOneMillion": 1264.08,
    "deathsPerOneMillion": 30.35,
    "tests": 16117932,
    "testsPerOneMillion": 11935.87,
    "population": 1350378201,
    "continent": "Africa",
    "activePerOneMillion": 198.33,
    "recoveredPerOneMillion": 1035.39,
    "criticalPerOneMillion": 1.53,
    "continentInfo": {
      "lat": 1.7383867,
      "long": -16.3094636
    },
    "countries": [
      "Algeria",
      "Angola",
      "Benin",
      "Botswana",
      "Burkina Faso",
      "Burundi",
      "Cabo Verde",
      "Cameroon",
      "Central African Republic",
      "Chad",
      "Comoros",
      "Congo",
      "C\u00f4te d'Ivoire",
      "DRC",
      "Djibouti",
      "Egypt",
      "Equatorial Guinea",
      "Eritrea",
      "Ethiopia",
      "Gabon",
      "Gambia",
      "Ghana",
      "Guinea",
      "Guinea-Bissau",
      "Kenya",
      "Lesotho",
      "Liberia",
      "Libyan Arab Jamahiriya",
      "Madagascar",
      "Malawi",
      "Mali",
      "Mauritania",
      "Mauritius",
      "Mayotte",
      "Morocco",
      "Mozambique",
      "Namibia",
      "Niger",
      "Nigeria",
      "Rwanda",
      "R\u00e9union",
      "Sao Tome and Principe",
      "Senegal",
      "Seychelles",
      "Sierra Leone",
      "Somalia",
      "South Africa",
      "South Sudan",
      "Sudan",
      "Swaziland",
      "Tanzania",
      "Togo",
      "Tunisia",
      "Uganda",
      "Western Sahara",
      "Zambia",
      "Zimbabwe"
    ]
  },
  {
    "updated": 1603500524340,
    "cases": 35852,
    "todayCases": 663,
    "deaths": 959,
    "todayDeaths": 1,
    "recovered": 31230,
    "todayRecovered": 99,
    "active": 3663,
    "critical": 17,
    "casesPerOneMillion": 858.47,
    "deathsPerOneMillion": 22.96,
    "tests": 9601411,
    "testsPerOneMillion": 229904.38,
    "population": 41762627,
    "continent": "Australia/Oceania",
    "activePerOneMillion": 87.71,
    "recoveredPerOneMillion": 747.8,
    "criticalPerOneMillion": 0.41,
    "continentInfo": {
      "lat": -8.6599161,
      "long": 91.1469847
    },
    "countries": [
      "Australia",
      "Fiji",
      "French Polynesia",
      "New Caledonia",
      "New Zealand",
      "Papua New Guinea",
      "Solomon Islands",
      "Wallis and Futuna"
    ]
  }
]
'''


class CountriesWorldometers:
    def __init__(self):
        self.request_url = "https://disease.sh/v3/covid-19/countries?allowNull=true"
        self.example_response = '''[
  {
    "updated": 1603500523774,
    "country": "Afghanistan",
    "countryInfo": {
      "_id": 4,
      "iso2": "AF",
      "iso3": "AFG",
      "lat": 33,
      "long": 65,
      "flag": "https://disease.sh/assets/img/flags/af.png"
    },
    "cases": 40687,
    "todayCases": 61,
    "deaths": 1507,
    "todayDeaths": 2,
    "recovered": 34010,
    "todayRecovered": 179,
    "active": 5170,
    "critical": 93,
    "casesPerOneMillion": 1038,
    "deathsPerOneMillion": 38,
    "tests": 119323,
    "testsPerOneMillion": 3044,
    "population": 39196742,
    "continent": "Asia",
    "oneCasePerPeople": 963,
    "oneDeathPerPeople": 26010,
    "oneTestPerPeople": 328,
    "activePerOneMillion": 131.9,
    "recoveredPerOneMillion": 867.67,
    "criticalPerOneMillion": 2.37
  },
  {
    "updated": 1603500523855,
    "country": "Albania",
    "countryInfo": {
      "_id": 8,
      "iso2": "AL",
      "iso3": "ALB",
      "lat": 41,
      "long": 20,
      "flag": "https://disease.sh/assets/img/flags/al.png"
    },
    "cases": 18556,
    "todayCases": 306,
    "deaths": 469,
    "todayDeaths": 4,
    "recovered": 10466,
    "todayRecovered": 71,
    "active": 7621,
    "critical": 20,
    "casesPerOneMillion": 6450,
    "deathsPerOneMillion": 163,
    "tests": 111564,
    "testsPerOneMillion": 38781,
    "population": 2876803,
    "continent": "Europe",
    "oneCasePerPeople": 155,
    "oneDeathPerPeople": 6134,
    "oneTestPerPeople": 26,
    "activePerOneMillion": 2649.12,
    "recoveredPerOneMillion": 3638.07,
    "criticalPerOneMillion": 6.95
  },
  {
    "updated": 1603500523760,
    "country": "Algeria",
    "countryInfo": {
      "_id": 12,
      "iso2": "DZ",
      "iso3": "DZA",
      "lat": 28,
      "long": 3,
      "flag": "https://disease.sh/assets/img/flags/dz.png"
    },
    "cases": 55630,
    "todayCases": 273,
    "deaths": 1897,
    "todayDeaths": 9,
    "recovered": 38788,
    "todayRecovered": 170,
    "active": 14945,
    "critical": 33,
    "casesPerOneMillion": 1262,
    "deathsPerOneMillion": 43,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 44095051,
    "continent": "Africa",
    "oneCasePerPeople": 793,
    "oneDeathPerPeople": 23245,
    "oneTestPerPeople": null,
    "activePerOneMillion": 338.93,
    "recoveredPerOneMillion": 879.65,
    "criticalPerOneMillion": 0.75
  },
  {
    "updated": 1603500524138,
    "country": "Andorra",
    "countryInfo": {
      "_id": 20,
      "iso2": "AD",
      "iso3": "AND",
      "lat": 42.5,
      "long": 1.6,
      "flag": "https://disease.sh/assets/img/flags/ad.png"
    },
    "cases": 4038,
    "todayCases": 227,
    "deaths": 69,
    "todayDeaths": 6,
    "recovered": 2729,
    "todayRecovered": 259,
    "active": 1240,
    "critical": 22,
    "casesPerOneMillion": 52235,
    "deathsPerOneMillion": 893,
    "tests": 137457,
    "testsPerOneMillion": 1778136,
    "population": 77304,
    "continent": "Europe",
    "oneCasePerPeople": 19,
    "oneDeathPerPeople": 1120,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 16040.57,
    "recoveredPerOneMillion": 35302.18,
    "criticalPerOneMillion": 284.59
  },
  {
    "updated": 1603500524037,
    "country": "Angola",
    "countryInfo": {
      "_id": 24,
      "iso2": "AO",
      "iso3": "AGO",
      "lat": -12.5,
      "long": 18.5,
      "flag": "https://disease.sh/assets/img/flags/ao.png"
    },
    "cases": 8829,
    "todayCases": 247,
    "deaths": 265,
    "todayDeaths": 5,
    "recovered": 3384,
    "todayRecovered": 79,
    "active": 5180,
    "critical": 30,
    "casesPerOneMillion": 266,
    "deathsPerOneMillion": 8,
    "tests": 85213,
    "testsPerOneMillion": 2569,
    "population": 33175205,
    "continent": "Africa",
    "oneCasePerPeople": 3758,
    "oneDeathPerPeople": 125189,
    "oneTestPerPeople": 389,
    "activePerOneMillion": 156.14,
    "recoveredPerOneMillion": 102,
    "criticalPerOneMillion": 0.9
  },
  {
    "updated": 1603500524268,
    "country": "Anguilla",
    "countryInfo": {
      "_id": 660,
      "iso2": "AI",
      "iso3": "AIA",
      "lat": 18.25,
      "long": -63.1667,
      "flag": "https://disease.sh/assets/img/flags/ai.png"
    },
    "cases": 3,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 3,
    "todayRecovered": null,
    "active": 0,
    "critical": null,
    "casesPerOneMillion": 199,
    "deathsPerOneMillion": null,
    "tests": 1329,
    "testsPerOneMillion": 88335,
    "population": 15045,
    "continent": "North America",
    "oneCasePerPeople": 5015,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 11,
    "activePerOneMillion": 0,
    "recoveredPerOneMillion": 199.4,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524250,
    "country": "Antigua and Barbuda",
    "countryInfo": {
      "_id": 28,
      "iso2": "AG",
      "iso3": "ATG",
      "lat": 17.05,
      "long": -61.8,
      "flag": "https://disease.sh/assets/img/flags/ag.png"
    },
    "cases": 122,
    "todayCases": null,
    "deaths": 3,
    "todayDeaths": null,
    "recovered": 107,
    "todayRecovered": null,
    "active": 12,
    "critical": null,
    "casesPerOneMillion": 1243,
    "deathsPerOneMillion": 31,
    "tests": 3366,
    "testsPerOneMillion": 34283,
    "population": 98182,
    "continent": "North America",
    "oneCasePerPeople": 805,
    "oneDeathPerPeople": 32727,
    "oneTestPerPeople": 29,
    "activePerOneMillion": 122.22,
    "recoveredPerOneMillion": 1089.81,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523556,
    "country": "Argentina",
    "countryInfo": {
      "_id": 32,
      "iso2": "AR",
      "iso3": "ARG",
      "lat": -34,
      "long": -64,
      "flag": "https://disease.sh/assets/img/flags/ar.png"
    },
    "cases": 1069368,
    "todayCases": 15718,
    "deaths": 28338,
    "todayDeaths": 381,
    "recovered": 866695,
    "todayRecovered": 14841,
    "active": 174335,
    "critical": 4696,
    "casesPerOneMillion": 23593,
    "deathsPerOneMillion": 625,
    "tests": 2777087,
    "testsPerOneMillion": 61270,
    "population": 45325182,
    "continent": "South America",
    "oneCasePerPeople": 42,
    "oneDeathPerPeople": 1599,
    "oneTestPerPeople": 16,
    "activePerOneMillion": 3846.32,
    "recoveredPerOneMillion": 19121.71,
    "criticalPerOneMillion": 103.61
  },
  {
    "updated": 1603500523752,
    "country": "Armenia",
    "countryInfo": {
      "_id": 51,
      "iso2": "AM",
      "iso3": "ARM",
      "lat": 40,
      "long": 45,
      "flag": "https://disease.sh/assets/img/flags/am.png"
    },
    "cases": 73310,
    "todayCases": 2474,
    "deaths": 1145,
    "todayDeaths": 14,
    "recovered": 50276,
    "todayRecovered": 489,
    "active": 21889,
    "critical": null,
    "casesPerOneMillion": 24725,
    "deathsPerOneMillion": 386,
    "tests": 368053,
    "testsPerOneMillion": 124133,
    "population": 2964988,
    "continent": "Asia",
    "oneCasePerPeople": 40,
    "oneDeathPerPeople": 2590,
    "oneTestPerPeople": 8,
    "activePerOneMillion": 7382.49,
    "recoveredPerOneMillion": 16956.56,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524059,
    "country": "Aruba",
    "countryInfo": {
      "_id": 533,
      "iso2": "AW",
      "iso3": "ABW",
      "lat": 12.5,
      "long": -69.9667,
      "flag": "https://disease.sh/assets/img/flags/aw.png"
    },
    "cases": 4401,
    "todayCases": 12,
    "deaths": 36,
    "todayDeaths": null,
    "recovered": 4160,
    "todayRecovered": 40,
    "active": 205,
    "critical": 4,
    "casesPerOneMillion": 41166,
    "deathsPerOneMillion": 337,
    "tests": 37643,
    "testsPerOneMillion": 352106,
    "population": 106908,
    "continent": "North America",
    "oneCasePerPeople": 24,
    "oneDeathPerPeople": 2970,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 1917.54,
    "recoveredPerOneMillion": 38911.96,
    "criticalPerOneMillion": 37.42
  },
  {
    "updated": 1603500523846,
    "country": "Australia",
    "countryInfo": {
      "_id": 36,
      "iso2": "AU",
      "iso3": "AUS",
      "lat": -27,
      "long": 133,
      "flag": "https://disease.sh/assets/img/flags/au.png"
    },
    "cases": 27484,
    "todayCases": 18,
    "deaths": 905,
    "todayDeaths": null,
    "recovered": 25169,
    "todayRecovered": 10,
    "active": 1410,
    "critical": null,
    "casesPerOneMillion": 1074,
    "deathsPerOneMillion": 35,
    "tests": 8466557,
    "testsPerOneMillion": 330830,
    "population": 25591896,
    "continent": "Australia/Oceania",
    "oneCasePerPeople": 931,
    "oneDeathPerPeople": 28278,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 55.1,
    "recoveredPerOneMillion": 983.48,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523751,
    "country": "Austria",
    "countryInfo": {
      "_id": 40,
      "iso2": "AT",
      "iso3": "AUT",
      "lat": 47.3333,
      "long": 13.3333,
      "flag": "https://disease.sh/assets/img/flags/at.png"
    },
    "cases": 74415,
    "todayCases": 2571,
    "deaths": 954,
    "todayDeaths": 13,
    "recovered": 55195,
    "todayRecovered": 1225,
    "active": 18266,
    "critical": 158,
    "casesPerOneMillion": 8248,
    "deathsPerOneMillion": 106,
    "tests": 2046426,
    "testsPerOneMillion": 226813,
    "population": 9022508,
    "continent": "Europe",
    "oneCasePerPeople": 121,
    "oneDeathPerPeople": 9458,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 2024.49,
    "recoveredPerOneMillion": 6117.48,
    "criticalPerOneMillion": 17.51
  },
  {
    "updated": 1603500523769,
    "country": "Azerbaijan",
    "countryInfo": {
      "_id": 31,
      "iso2": "AZ",
      "iso3": "AZE",
      "lat": 40.5,
      "long": 47.5,
      "flag": "https://disease.sh/assets/img/flags/az.png"
    },
    "cases": 48221,
    "todayCases": 803,
    "deaths": 656,
    "todayDeaths": 8,
    "recovered": 40831,
    "todayRecovered": 212,
    "active": 6734,
    "critical": null,
    "casesPerOneMillion": 4743,
    "deathsPerOneMillion": 65,
    "tests": 1270144,
    "testsPerOneMillion": 124919,
    "population": 10167700,
    "continent": "Asia",
    "oneCasePerPeople": 211,
    "oneDeathPerPeople": 15500,
    "oneTestPerPeople": 8,
    "activePerOneMillion": 662.29,
    "recoveredPerOneMillion": 4015.76,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524045,
    "country": "Bahamas",
    "countryInfo": {
      "_id": 44,
      "iso2": "BS",
      "iso3": "BHS",
      "lat": 24.25,
      "long": -76,
      "flag": "https://disease.sh/assets/img/flags/bs.png"
    },
    "cases": 6268,
    "todayCases": 133,
    "deaths": 130,
    "todayDeaths": null,
    "recovered": 3795,
    "todayRecovered": 90,
    "active": 2343,
    "critical": 10,
    "casesPerOneMillion": 15892,
    "deathsPerOneMillion": 330,
    "tests": 33300,
    "testsPerOneMillion": 84429,
    "population": 394416,
    "continent": "North America",
    "oneCasePerPeople": 63,
    "oneDeathPerPeople": 3034,
    "oneTestPerPeople": 12,
    "activePerOneMillion": 5940.43,
    "recoveredPerOneMillion": 9621.82,
    "criticalPerOneMillion": 25.35
  },
  {
    "updated": 1603500523750,
    "country": "Bahrain",
    "countryInfo": {
      "_id": 48,
      "iso2": "BH",
      "iso3": "BHR",
      "lat": 26,
      "long": 50.55,
      "flag": "https://disease.sh/assets/img/flags/bh.png"
    },
    "cases": 79574,
    "todayCases": 363,
    "deaths": 311,
    "todayDeaths": 3,
    "recovered": 76143,
    "todayRecovered": 303,
    "active": 3120,
    "critical": 29,
    "casesPerOneMillion": 46282,
    "deathsPerOneMillion": 181,
    "tests": 1670411,
    "testsPerOneMillion": 971539,
    "population": 1719346,
    "continent": "Asia",
    "oneCasePerPeople": 22,
    "oneDeathPerPeople": 5528,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 1814.64,
    "recoveredPerOneMillion": 44286.03,
    "criticalPerOneMillion": 16.87
  },
  {
    "updated": 1603500523638,
    "country": "Bangladesh",
    "countryInfo": {
      "_id": 50,
      "iso2": "BD",
      "iso3": "BGD",
      "lat": 24,
      "long": 90,
      "flag": "https://disease.sh/assets/img/flags/bd.png"
    },
    "cases": 396413,
    "todayCases": 1586,
    "deaths": 5761,
    "todayDeaths": 14,
    "recovered": 312065,
    "todayRecovered": 1533,
    "active": 78587,
    "critical": null,
    "casesPerOneMillion": 2400,
    "deathsPerOneMillion": 35,
    "tests": 2235488,
    "testsPerOneMillion": 13532,
    "population": 165200803,
    "continent": "Asia",
    "oneCasePerPeople": 417,
    "oneDeathPerPeople": 28676,
    "oneTestPerPeople": 74,
    "activePerOneMillion": 475.71,
    "recoveredPerOneMillion": 1889,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524246,
    "country": "Barbados",
    "countryInfo": {
      "_id": 52,
      "iso2": "BB",
      "iso3": "BRB",
      "lat": 13.1667,
      "long": -59.5333,
      "flag": "https://disease.sh/assets/img/flags/bb.png"
    },
    "cases": 226,
    "todayCases": 2,
    "deaths": 7,
    "todayDeaths": null,
    "recovered": 207,
    "todayRecovered": null,
    "active": 12,
    "critical": null,
    "casesPerOneMillion": 786,
    "deathsPerOneMillion": 24,
    "tests": 32374,
    "testsPerOneMillion": 112611,
    "population": 287486,
    "continent": "North America",
    "oneCasePerPeople": 1272,
    "oneDeathPerPeople": 41069,
    "oneTestPerPeople": 9,
    "activePerOneMillion": 41.74,
    "recoveredPerOneMillion": 720.04,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523747,
    "country": "Belarus",
    "countryInfo": {
      "_id": 112,
      "iso2": "BY",
      "iso3": "BLR",
      "lat": 53,
      "long": 28,
      "flag": "https://disease.sh/assets/img/flags/by.png"
    },
    "cases": 91167,
    "todayCases": 787,
    "deaths": 945,
    "todayDeaths": null,
    "recovered": 82136,
    "todayRecovered": 635,
    "active": 8086,
    "critical": null,
    "casesPerOneMillion": 9649,
    "deathsPerOneMillion": 100,
    "tests": 2320856,
    "testsPerOneMillion": 245636,
    "population": 9448341,
    "continent": "Europe",
    "oneCasePerPeople": 104,
    "oneDeathPerPeople": 9998,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 855.81,
    "recoveredPerOneMillion": 8693.17,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523652,
    "country": "Belgium",
    "countryInfo": {
      "_id": 56,
      "iso2": "BE",
      "iso3": "BEL",
      "lat": 50.8333,
      "long": 4,
      "flag": "https://disease.sh/assets/img/flags/be.png"
    },
    "cases": 270132,
    "todayCases": 16746,
    "deaths": 10588,
    "todayDeaths": 49,
    "recovered": 22213,
    "todayRecovered": 496,
    "active": 237331,
    "critical": 573,
    "casesPerOneMillion": 23276,
    "deathsPerOneMillion": 912,
    "tests": 4375231,
    "testsPerOneMillion": 376998,
    "population": 11605464,
    "continent": "Europe",
    "oneCasePerPeople": 43,
    "oneDeathPerPeople": 1096,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 20449.94,
    "recoveredPerOneMillion": 1914.01,
    "criticalPerOneMillion": 49.37
  },
  {
    "updated": 1603500524143,
    "country": "Belize",
    "countryInfo": {
      "_id": 84,
      "iso2": "BZ",
      "iso3": "BLZ",
      "lat": 17.25,
      "long": -88.75,
      "flag": "https://disease.sh/assets/img/flags/bz.png"
    },
    "cases": 2995,
    "todayCases": 58,
    "deaths": 46,
    "todayDeaths": null,
    "recovered": 1826,
    "todayRecovered": 70,
    "active": 1123,
    "critical": 1,
    "casesPerOneMillion": 7490,
    "deathsPerOneMillion": 115,
    "tests": 20458,
    "testsPerOneMillion": 51164,
    "population": 399852,
    "continent": "North America",
    "oneCasePerPeople": 134,
    "oneDeathPerPeople": 8692,
    "oneTestPerPeople": 20,
    "activePerOneMillion": 2808.54,
    "recoveredPerOneMillion": 4566.69,
    "criticalPerOneMillion": 2.5
  },
  {
    "updated": 1603500524147,
    "country": "Benin",
    "countryInfo": {
      "_id": 204,
      "iso2": "BJ",
      "iso3": "BEN",
      "lat": 9.5,
      "long": 2.25,
      "flag": "https://disease.sh/assets/img/flags/bj.png"
    },
    "cases": 2557,
    "todayCases": null,
    "deaths": 41,
    "todayDeaths": null,
    "recovered": 2330,
    "todayRecovered": null,
    "active": 186,
    "critical": null,
    "casesPerOneMillion": 209,
    "deathsPerOneMillion": 3,
    "tests": 238105,
    "testsPerOneMillion": 19485,
    "population": 12219878,
    "continent": "Africa",
    "oneCasePerPeople": 4779,
    "oneDeathPerPeople": 298046,
    "oneTestPerPeople": 51,
    "activePerOneMillion": 15.22,
    "recoveredPerOneMillion": 190.67,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524247,
    "country": "Bermuda",
    "countryInfo": {
      "_id": 60,
      "iso2": "BM",
      "iso3": "BMU",
      "lat": 32.3333,
      "long": -64.75,
      "flag": "https://disease.sh/assets/img/flags/bm.png"
    },
    "cases": 190,
    "todayCases": 2,
    "deaths": 9,
    "todayDeaths": null,
    "recovered": 175,
    "todayRecovered": null,
    "active": 6,
    "critical": null,
    "casesPerOneMillion": 3054,
    "deathsPerOneMillion": 145,
    "tests": 79686,
    "testsPerOneMillion": 1281022,
    "population": 62205,
    "continent": "North America",
    "oneCasePerPeople": 327,
    "oneDeathPerPeople": 6912,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 96.46,
    "recoveredPerOneMillion": 2813.28,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524241,
    "country": "Bhutan",
    "countryInfo": {
      "_id": 64,
      "iso2": "BT",
      "iso3": "BTN",
      "lat": 27.5,
      "long": 90.5,
      "flag": "https://disease.sh/assets/img/flags/bt.png"
    },
    "cases": 336,
    "todayCases": 4,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 306,
    "todayRecovered": null,
    "active": 30,
    "critical": null,
    "casesPerOneMillion": 434,
    "deathsPerOneMillion": null,
    "tests": 163495,
    "testsPerOneMillion": 211165,
    "population": 774252,
    "continent": "Asia",
    "oneCasePerPeople": 2304,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 38.75,
    "recoveredPerOneMillion": 395.22,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523661,
    "country": "Bolivia",
    "countryInfo": {
      "_id": 68,
      "iso2": "BO",
      "iso3": "BOL",
      "lat": -17,
      "long": -65,
      "flag": "https://disease.sh/assets/img/flags/bo.png"
    },
    "cases": 140445,
    "todayCases": 217,
    "deaths": 8584,
    "todayDeaths": 26,
    "recovered": 106950,
    "todayRecovered": 620,
    "active": 24911,
    "critical": 71,
    "casesPerOneMillion": 11981,
    "deathsPerOneMillion": 732,
    "tests": 325340,
    "testsPerOneMillion": 27754,
    "population": 11722399,
    "continent": "South America",
    "oneCasePerPeople": 83,
    "oneDeathPerPeople": 1366,
    "oneTestPerPeople": 36,
    "activePerOneMillion": 2125.08,
    "recoveredPerOneMillion": 9123.56,
    "criticalPerOneMillion": 6.06
  },
  {
    "updated": 1603500523836,
    "country": "Bosnia",
    "countryInfo": {
      "_id": 70,
      "iso2": "BA",
      "iso3": "BIH",
      "lat": 44,
      "long": 18,
      "flag": "https://disease.sh/assets/img/flags/ba.png"
    },
    "cases": 38493,
    "todayCases": 1179,
    "deaths": 1065,
    "todayDeaths": 14,
    "recovered": 26260,
    "todayRecovered": 271,
    "active": 11168,
    "critical": null,
    "casesPerOneMillion": 11756,
    "deathsPerOneMillion": 325,
    "tests": 289301,
    "testsPerOneMillion": 88354,
    "population": 3274324,
    "continent": "Europe",
    "oneCasePerPeople": 85,
    "oneDeathPerPeople": 3074,
    "oneTestPerPeople": 11,
    "activePerOneMillion": 3410.78,
    "recoveredPerOneMillion": 8019.98,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524045,
    "country": "Botswana",
    "countryInfo": {
      "_id": 72,
      "iso2": "BW",
      "iso3": "BWA",
      "lat": -22,
      "long": 24,
      "flag": "https://disease.sh/assets/img/flags/bw.png"
    },
    "cases": 5923,
    "todayCases": null,
    "deaths": 21,
    "todayDeaths": null,
    "recovered": 927,
    "todayRecovered": null,
    "active": 4975,
    "critical": 1,
    "casesPerOneMillion": 2503,
    "deathsPerOneMillion": 9,
    "tests": 279070,
    "testsPerOneMillion": 117940,
    "population": 2366213,
    "continent": "Africa",
    "oneCasePerPeople": 399,
    "oneDeathPerPeople": 112677,
    "oneTestPerPeople": 8,
    "activePerOneMillion": 2102.52,
    "recoveredPerOneMillion": 391.77,
    "criticalPerOneMillion": 0.42
  },
  {
    "updated": 1603500523552,
    "country": "Brazil",
    "countryInfo": {
      "_id": 76,
      "iso2": "BR",
      "iso3": "BRA",
      "lat": -10,
      "long": -55,
      "flag": "https://disease.sh/assets/img/flags/br.png"
    },
    "cases": 5355650,
    "todayCases": 23016,
    "deaths": 156528,
    "todayDeaths": 566,
    "recovered": 4797872,
    "todayRecovered": 12575,
    "active": 401250,
    "critical": 8318,
    "casesPerOneMillion": 25140,
    "deathsPerOneMillion": 735,
    "tests": 21900000,
    "testsPerOneMillion": 102801,
    "population": 213032208,
    "continent": "South America",
    "oneCasePerPeople": 40,
    "oneDeathPerPeople": 1361,
    "oneTestPerPeople": 10,
    "activePerOneMillion": 1883.52,
    "recoveredPerOneMillion": 22521.82,
    "criticalPerOneMillion": 39.05
  },
  {
    "updated": 1603500524252,
    "country": "British Virgin Islands",
    "countryInfo": {
      "_id": 92,
      "iso2": "VG",
      "iso3": "VGB",
      "lat": 18.5,
      "long": -64.5,
      "flag": "https://disease.sh/assets/img/flags/vg.png"
    },
    "cases": 71,
    "todayCases": null,
    "deaths": 1,
    "todayDeaths": null,
    "recovered": 70,
    "todayRecovered": null,
    "active": 0,
    "critical": null,
    "casesPerOneMillion": 2344,
    "deathsPerOneMillion": 33,
    "tests": 5193,
    "testsPerOneMillion": 171420,
    "population": 30294,
    "continent": "North America",
    "oneCasePerPeople": 427,
    "oneDeathPerPeople": 30294,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 0,
    "recoveredPerOneMillion": 2310.69,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524249,
    "country": "Brunei",
    "countryInfo": {
      "_id": 96,
      "iso2": "BN",
      "iso3": "BRN",
      "lat": 4.5,
      "long": 114.6667,
      "flag": "https://disease.sh/assets/img/flags/bn.png"
    },
    "cases": 148,
    "todayCases": null,
    "deaths": 3,
    "todayDeaths": null,
    "recovered": 143,
    "todayRecovered": null,
    "active": 2,
    "critical": null,
    "casesPerOneMillion": 337,
    "deathsPerOneMillion": 7,
    "tests": 65663,
    "testsPerOneMillion": 149647,
    "population": 438785,
    "continent": "Asia",
    "oneCasePerPeople": 2965,
    "oneDeathPerPeople": 146262,
    "oneTestPerPeople": 7,
    "activePerOneMillion": 4.56,
    "recoveredPerOneMillion": 325.9,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523842,
    "country": "Bulgaria",
    "countryInfo": {
      "_id": 100,
      "iso2": "BG",
      "iso3": "BGR",
      "lat": 43,
      "long": 25,
      "flag": "https://disease.sh/assets/img/flags/bg.png"
    },
    "cases": 36519,
    "todayCases": 1589,
    "deaths": 1077,
    "todayDeaths": 13,
    "recovered": 18102,
    "todayRecovered": 269,
    "active": 17340,
    "critical": 127,
    "casesPerOneMillion": 5268,
    "deathsPerOneMillion": 155,
    "tests": 652508,
    "testsPerOneMillion": 94133,
    "population": 6931771,
    "continent": "Europe",
    "oneCasePerPeople": 190,
    "oneDeathPerPeople": 6436,
    "oneTestPerPeople": 11,
    "activePerOneMillion": 2501.53,
    "recoveredPerOneMillion": 2611.45,
    "criticalPerOneMillion": 18.32
  },
  {
    "updated": 1603500524148,
    "country": "Burkina Faso",
    "countryInfo": {
      "_id": 854,
      "iso2": "BF",
      "iso3": "BFA",
      "lat": 13,
      "long": -2,
      "flag": "https://disease.sh/assets/img/flags/bf.png"
    },
    "cases": 2433,
    "todayCases": 19,
    "deaths": 65,
    "todayDeaths": null,
    "recovered": 1996,
    "todayRecovered": 127,
    "active": 372,
    "critical": null,
    "casesPerOneMillion": 115,
    "deathsPerOneMillion": 3,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 21077460,
    "continent": "Africa",
    "oneCasePerPeople": 8663,
    "oneDeathPerPeople": 324269,
    "oneTestPerPeople": null,
    "activePerOneMillion": 17.65,
    "recoveredPerOneMillion": 94.7,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524169,
    "country": "Burundi",
    "countryInfo": {
      "_id": 108,
      "iso2": "BI",
      "iso3": "BDI",
      "lat": -3.5,
      "long": 30,
      "flag": "https://disease.sh/assets/img/flags/bi.png"
    },
    "cases": 553,
    "todayCases": 2,
    "deaths": 1,
    "todayDeaths": null,
    "recovered": 497,
    "todayRecovered": null,
    "active": 55,
    "critical": null,
    "casesPerOneMillion": 46,
    "deathsPerOneMillion": 0.08,
    "tests": 44526,
    "testsPerOneMillion": 3711,
    "population": 11998016,
    "continent": "Africa",
    "oneCasePerPeople": 21696,
    "oneDeathPerPeople": 11998016,
    "oneTestPerPeople": 269,
    "activePerOneMillion": 4.58,
    "recoveredPerOneMillion": 41.42,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524040,
    "country": "Cabo Verde",
    "countryInfo": {
      "_id": 132,
      "iso2": "CV",
      "iso3": "CPV",
      "lat": 16,
      "long": -24,
      "flag": "https://disease.sh/assets/img/flags/cv.png"
    },
    "cases": 8198,
    "todayCases": 76,
    "deaths": 94,
    "todayDeaths": 3,
    "recovered": 7034,
    "todayRecovered": 94,
    "active": 1070,
    "critical": 23,
    "casesPerOneMillion": 14695,
    "deathsPerOneMillion": 168,
    "tests": 87480,
    "testsPerOneMillion": 156812,
    "population": 557867,
    "continent": "Africa",
    "oneCasePerPeople": 68,
    "oneDeathPerPeople": 5935,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 1918.02,
    "recoveredPerOneMillion": 12608.74,
    "criticalPerOneMillion": 41.23
  },
  {
    "updated": 1603500524245,
    "country": "Cambodia",
    "countryInfo": {
      "_id": 116,
      "iso2": "KH",
      "iso3": "KHM",
      "lat": 13,
      "long": 105,
      "flag": "https://disease.sh/assets/img/flags/kh.png"
    },
    "cases": 286,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 280,
    "todayRecovered": null,
    "active": 6,
    "critical": null,
    "casesPerOneMillion": 17,
    "deathsPerOneMillion": null,
    "tests": 170495,
    "testsPerOneMillion": 10154,
    "population": 16790698,
    "continent": "Asia",
    "oneCasePerPeople": 58709,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 98,
    "activePerOneMillion": 0.36,
    "recoveredPerOneMillion": 16.68,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523851,
    "country": "Cameroon",
    "countryInfo": {
      "_id": 120,
      "iso2": "CM",
      "iso3": "CMR",
      "lat": 6,
      "long": 12,
      "flag": "https://disease.sh/assets/img/flags/cm.png"
    },
    "cases": 21570,
    "todayCases": null,
    "deaths": 425,
    "todayDeaths": null,
    "recovered": 20117,
    "todayRecovered": null,
    "active": 1028,
    "critical": 61,
    "casesPerOneMillion": 806,
    "deathsPerOneMillion": 16,
    "tests": 149000,
    "testsPerOneMillion": 5571,
    "population": 26747441,
    "continent": "Africa",
    "oneCasePerPeople": 1240,
    "oneDeathPerPeople": 62935,
    "oneTestPerPeople": 180,
    "activePerOneMillion": 38.43,
    "recoveredPerOneMillion": 752.11,
    "criticalPerOneMillion": 2.28
  },
  {
    "updated": 1603500523655,
    "country": "Canada",
    "countryInfo": {
      "_id": 124,
      "iso2": "CA",
      "iso3": "CAN",
      "lat": 60,
      "long": -95,
      "flag": "https://disease.sh/assets/img/flags/ca.png"
    },
    "cases": 211732,
    "todayCases": 2584,
    "deaths": 9888,
    "todayDeaths": 26,
    "recovered": 177879,
    "todayRecovered": 2074,
    "active": 23965,
    "critical": 215,
    "casesPerOneMillion": 5595,
    "deathsPerOneMillion": 261,
    "tests": 9476989,
    "testsPerOneMillion": 250413,
    "population": 37845468,
    "continent": "North America",
    "oneCasePerPeople": 179,
    "oneDeathPerPeople": 3827,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 633.23,
    "recoveredPerOneMillion": 4700.14,
    "criticalPerOneMillion": 5.68
  },
  {
    "updated": 1603500524248,
    "country": "Caribbean Netherlands",
    "countryInfo": {
      "_id": 535,
      "iso2": "BQ",
      "iso3": "BES",
      "lat": 12.2,
      "long": -68.26,
      "flag": "https://disease.sh/assets/img/flags/bq.png"
    },
    "cases": 150,
    "todayCases": null,
    "deaths": 3,
    "todayDeaths": null,
    "recovered": 121,
    "todayRecovered": null,
    "active": 26,
    "critical": null,
    "casesPerOneMillion": 5704,
    "deathsPerOneMillion": 114,
    "tests": 2890,
    "testsPerOneMillion": 109890,
    "population": 26299,
    "continent": "North America",
    "oneCasePerPeople": 175,
    "oneDeathPerPeople": 8766,
    "oneTestPerPeople": 9,
    "activePerOneMillion": 988.63,
    "recoveredPerOneMillion": 4600.94,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524245,
    "country": "Cayman Islands",
    "countryInfo": {
      "_id": 136,
      "iso2": "KY",
      "iso3": "CYM",
      "lat": 19.5,
      "long": -80.5,
      "flag": "https://disease.sh/assets/img/flags/ky.png"
    },
    "cases": 239,
    "todayCases": 3,
    "deaths": 1,
    "todayDeaths": null,
    "recovered": 215,
    "todayRecovered": null,
    "active": 23,
    "critical": 1,
    "casesPerOneMillion": 3623,
    "deathsPerOneMillion": 15,
    "tests": 45365,
    "testsPerOneMillion": 687744,
    "population": 65962,
    "continent": "North America",
    "oneCasePerPeople": 276,
    "oneDeathPerPeople": 65962,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 348.69,
    "recoveredPerOneMillion": 3259.45,
    "criticalPerOneMillion": 15.16
  },
  {
    "updated": 1603500524058,
    "country": "Central African Republic",
    "countryInfo": {
      "_id": 140,
      "iso2": "CF",
      "iso3": "CAF",
      "lat": 7,
      "long": 21,
      "flag": "https://disease.sh/assets/img/flags/cf.png"
    },
    "cases": 4862,
    "todayCases": null,
    "deaths": 62,
    "todayDeaths": null,
    "recovered": 1924,
    "todayRecovered": null,
    "active": 2876,
    "critical": 2,
    "casesPerOneMillion": 1001,
    "deathsPerOneMillion": 13,
    "tests": 32711,
    "testsPerOneMillion": 6737,
    "population": 4855669,
    "continent": "Africa",
    "oneCasePerPeople": 999,
    "oneDeathPerPeople": 78317,
    "oneTestPerPeople": 148,
    "activePerOneMillion": 592.3,
    "recoveredPerOneMillion": 396.24,
    "criticalPerOneMillion": 0.41
  },
  {
    "updated": 1603500524155,
    "country": "Chad",
    "countryInfo": {
      "_id": 148,
      "iso2": "TD",
      "iso3": "TCD",
      "lat": 15,
      "long": 19,
      "flag": "https://disease.sh/assets/img/flags/td.png"
    },
    "cases": 1423,
    "todayCases": 13,
    "deaths": 96,
    "todayDeaths": null,
    "recovered": 1234,
    "todayRecovered": 11,
    "active": 93,
    "critical": null,
    "casesPerOneMillion": 86,
    "deathsPerOneMillion": 6,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 16568821,
    "continent": "Africa",
    "oneCasePerPeople": 11644,
    "oneDeathPerPeople": 172592,
    "oneTestPerPeople": null,
    "activePerOneMillion": 5.61,
    "recoveredPerOneMillion": 74.48,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524162,
    "country": "Channel Islands",
    "countryInfo": {
      "_id": 832,
      "iso2": "JE",
      "iso3": "JEY",
      "lat": 49.21,
      "long": -2.13,
      "flag": "https://disease.sh/assets/img/flags/je.png"
    },
    "cases": 795,
    "todayCases": 11,
    "deaths": 48,
    "todayDeaths": null,
    "recovered": 659,
    "todayRecovered": null,
    "active": 88,
    "critical": 2,
    "casesPerOneMillion": 4559,
    "deathsPerOneMillion": 275,
    "tests": 141888,
    "testsPerOneMillion": 813751,
    "population": 174363,
    "continent": "Europe",
    "oneCasePerPeople": 219,
    "oneDeathPerPeople": 3633,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 504.69,
    "recoveredPerOneMillion": 3779.47,
    "criticalPerOneMillion": 11.47
  },
  {
    "updated": 1603500523566,
    "country": "Chile",
    "countryInfo": {
      "_id": 152,
      "iso2": "CL",
      "iso3": "CHL",
      "lat": -30,
      "long": -71,
      "flag": "https://disease.sh/assets/img/flags/cl.png"
    },
    "cases": 498906,
    "todayCases": 1775,
    "deaths": 13844,
    "todayDeaths": 52,
    "recovered": 471343,
    "todayRecovered": 1578,
    "active": 13719,
    "critical": 759,
    "casesPerOneMillion": 26029,
    "deathsPerOneMillion": 722,
    "tests": 4043282,
    "testsPerOneMillion": 210945,
    "population": 19167444,
    "continent": "South America",
    "oneCasePerPeople": 38,
    "oneDeathPerPeople": 1385,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 715.74,
    "recoveredPerOneMillion": 24590.81,
    "criticalPerOneMillion": 39.6
  },
  {
    "updated": 1603500524270,
    "country": "China",
    "countryInfo": {
      "_id": 156,
      "iso2": "CN",
      "iso3": "CHN",
      "lat": 35,
      "long": 105,
      "flag": "https://disease.sh/assets/img/flags/cn.png"
    },
    "cases": 85747,
    "todayCases": 18,
    "deaths": 4634,
    "todayDeaths": null,
    "recovered": 80865,
    "todayRecovered": 15,
    "active": 248,
    "critical": 3,
    "casesPerOneMillion": 60,
    "deathsPerOneMillion": 3,
    "tests": 160000000,
    "testsPerOneMillion": 111163,
    "population": 1439323776,
    "continent": "Asia",
    "oneCasePerPeople": 16786,
    "oneDeathPerPeople": 310601,
    "oneTestPerPeople": 9,
    "activePerOneMillion": 0.17,
    "recoveredPerOneMillion": 56.18,
    "criticalPerOneMillion": 0
  },
  {
    "updated": 1603500523559,
    "country": "Colombia",
    "countryInfo": {
      "_id": 170,
      "iso2": "CO",
      "iso3": "COL",
      "lat": 4,
      "long": -72,
      "flag": "https://disease.sh/assets/img/flags/co.png"
    },
    "cases": 998942,
    "todayCases": 8672,
    "deaths": 29802,
    "todayDeaths": 166,
    "recovered": 901652,
    "todayRecovered": 7940,
    "active": 67488,
    "critical": 2291,
    "casesPerOneMillion": 19567,
    "deathsPerOneMillion": 584,
    "tests": 4668341,
    "testsPerOneMillion": 91443,
    "population": 51051776,
    "continent": "South America",
    "oneCasePerPeople": 51,
    "oneDeathPerPeople": 1713,
    "oneTestPerPeople": 11,
    "activePerOneMillion": 1321.95,
    "recoveredPerOneMillion": 17661.52,
    "criticalPerOneMillion": 44.88
  },
  {
    "updated": 1603500524235,
    "country": "Comoros",
    "countryInfo": {
      "_id": 174,
      "iso2": "KM",
      "iso3": "COM",
      "lat": -12.1667,
      "long": 44.25,
      "flag": "https://disease.sh/assets/img/flags/km.png"
    },
    "cases": 517,
    "todayCases": null,
    "deaths": 7,
    "todayDeaths": null,
    "recovered": 494,
    "todayRecovered": null,
    "active": 16,
    "critical": null,
    "casesPerOneMillion": 591,
    "deathsPerOneMillion": 8,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 875282,
    "continent": "Africa",
    "oneCasePerPeople": 1693,
    "oneDeathPerPeople": 125040,
    "oneTestPerPeople": null,
    "activePerOneMillion": 18.28,
    "recoveredPerOneMillion": 564.39,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524054,
    "country": "Congo",
    "countryInfo": {
      "_id": 178,
      "iso2": "CG",
      "iso3": "COG",
      "lat": -1,
      "long": 15,
      "flag": "https://disease.sh/assets/img/flags/cg.png"
    },
    "cases": 5156,
    "todayCases": null,
    "deaths": 92,
    "todayDeaths": null,
    "recovered": 3887,
    "todayRecovered": null,
    "active": 1177,
    "critical": null,
    "casesPerOneMillion": 927,
    "deathsPerOneMillion": 17,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 5559538,
    "continent": "Africa",
    "oneCasePerPeople": 1078,
    "oneDeathPerPeople": 60430,
    "oneTestPerPeople": null,
    "activePerOneMillion": 211.71,
    "recoveredPerOneMillion": 699.16,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523738,
    "country": "Costa Rica",
    "countryInfo": {
      "_id": 188,
      "iso2": "CR",
      "iso3": "CRI",
      "lat": 10,
      "long": -84,
      "flag": "https://disease.sh/assets/img/flags/cr.png"
    },
    "cases": 101826,
    "todayCases": 1210,
    "deaths": 1265,
    "todayDeaths": 14,
    "recovered": 61662,
    "todayRecovered": 500,
    "active": 38899,
    "critical": 201,
    "casesPerOneMillion": 19932,
    "deathsPerOneMillion": 248,
    "tests": 271394,
    "testsPerOneMillion": 53125,
    "population": 5108634,
    "continent": "North America",
    "oneCasePerPeople": 50,
    "oneDeathPerPeople": 4038,
    "oneTestPerPeople": 19,
    "activePerOneMillion": 7614.36,
    "recoveredPerOneMillion": 12070.15,
    "criticalPerOneMillion": 39.35
  },
  {
    "updated": 1603500523844,
    "country": "Croatia",
    "countryInfo": {
      "_id": 191,
      "iso2": "HR",
      "iso3": "HRV",
      "lat": 45.1667,
      "long": 15.5,
      "flag": "https://disease.sh/assets/img/flags/hr.png"
    },
    "cases": 31717,
    "todayCases": 1867,
    "deaths": 413,
    "todayDeaths": 7,
    "recovered": 22910,
    "todayRecovered": 846,
    "active": 8394,
    "critical": 49,
    "casesPerOneMillion": 7741,
    "deathsPerOneMillion": 101,
    "tests": 428961,
    "testsPerOneMillion": 104696,
    "population": 4097210,
    "continent": "Europe",
    "oneCasePerPeople": 129,
    "oneDeathPerPeople": 9921,
    "oneTestPerPeople": 10,
    "activePerOneMillion": 2048.71,
    "recoveredPerOneMillion": 5591.61,
    "criticalPerOneMillion": 11.96
  },
  {
    "updated": 1603500524043,
    "country": "Cuba",
    "countryInfo": {
      "_id": 192,
      "iso2": "CU",
      "iso3": "CUB",
      "lat": 21.5,
      "long": -80,
      "flag": "https://disease.sh/assets/img/flags/cu.png"
    },
    "cases": 6479,
    "todayCases": 58,
    "deaths": 128,
    "todayDeaths": null,
    "recovered": 5899,
    "todayRecovered": 28,
    "active": 452,
    "critical": 5,
    "casesPerOneMillion": 572,
    "deathsPerOneMillion": 11,
    "tests": 777247,
    "testsPerOneMillion": 68635,
    "population": 11324431,
    "continent": "North America",
    "oneCasePerPeople": 1748,
    "oneDeathPerPeople": 88472,
    "oneTestPerPeople": 15,
    "activePerOneMillion": 39.91,
    "recoveredPerOneMillion": 520.91,
    "criticalPerOneMillion": 0.44
  },
  {
    "updated": 1603500524162,
    "country": "Cura\u00e7ao",
    "countryInfo": {
      "_id": 531,
      "iso2": "CW",
      "iso3": "CUW",
      "lat": 12.15,
      "long": -68.97,
      "flag": "https://disease.sh/assets/img/flags/cw.png"
    },
    "cases": 818,
    "todayCases": 14,
    "deaths": 1,
    "todayDeaths": null,
    "recovered": 534,
    "todayRecovered": 25,
    "active": 283,
    "critical": 5,
    "casesPerOneMillion": 4979,
    "deathsPerOneMillion": 6,
    "tests": 11276,
    "testsPerOneMillion": 68629,
    "population": 164304,
    "continent": "North America",
    "oneCasePerPeople": 201,
    "oneDeathPerPeople": 164304,
    "oneTestPerPeople": 15,
    "activePerOneMillion": 1722.42,
    "recoveredPerOneMillion": 3250.07,
    "criticalPerOneMillion": 30.43
  },
  {
    "updated": 1603500524143,
    "country": "Cyprus",
    "countryInfo": {
      "_id": 196,
      "iso2": "CY",
      "iso3": "CYP",
      "lat": 35,
      "long": 33,
      "flag": "https://disease.sh/assets/img/flags/cy.png"
    },
    "cases": 3314,
    "todayCases": 160,
    "deaths": 25,
    "todayDeaths": null,
    "recovered": 1444,
    "todayRecovered": null,
    "active": 1845,
    "critical": 5,
    "casesPerOneMillion": 2739,
    "deathsPerOneMillion": 21,
    "tests": 446224,
    "testsPerOneMillion": 368747,
    "population": 1210109,
    "continent": "Asia",
    "oneCasePerPeople": 365,
    "oneDeathPerPeople": 48404,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 1524.66,
    "recoveredPerOneMillion": 1193.28,
    "criticalPerOneMillion": 4.13
  },
  {
    "updated": 1603500523653,
    "country": "Czechia",
    "countryInfo": {
      "_id": 203,
      "iso2": "CZ",
      "iso3": "CZE",
      "lat": 49.75,
      "long": 15.5,
      "flag": "https://disease.sh/assets/img/flags/cz.png"
    },
    "cases": 238323,
    "todayCases": 15258,
    "deaths": 1971,
    "todayDeaths": 126,
    "recovered": 91651,
    "todayRecovered": 4426,
    "active": 144701,
    "critical": 735,
    "casesPerOneMillion": 22241,
    "deathsPerOneMillion": 184,
    "tests": 1976869,
    "testsPerOneMillion": 184491,
    "population": 10715241,
    "continent": "Europe",
    "oneCasePerPeople": 45,
    "oneDeathPerPeople": 5436,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 13504.22,
    "recoveredPerOneMillion": 8553.33,
    "criticalPerOneMillion": 68.59
  },
  {
    "updated": 1603500523851,
    "country": "C\u00f4te d'Ivoire",
    "countryInfo": {
      "_id": 384,
      "iso2": "CI",
      "iso3": "CIV",
      "lat": 8,
      "long": -5,
      "flag": "https://disease.sh/assets/img/flags/ci.png"
    },
    "cases": 20405,
    "todayCases": 15,
    "deaths": 121,
    "todayDeaths": null,
    "recovered": 20100,
    "todayRecovered": 12,
    "active": 184,
    "critical": null,
    "casesPerOneMillion": 768,
    "deathsPerOneMillion": 5,
    "tests": 184796,
    "testsPerOneMillion": 6953,
    "population": 26577577,
    "continent": "Africa",
    "oneCasePerPeople": 1303,
    "oneDeathPerPeople": 219649,
    "oneTestPerPeople": 144,
    "activePerOneMillion": 6.92,
    "recoveredPerOneMillion": 756.28,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523952,
    "country": "DRC",
    "countryInfo": {
      "_id": 180,
      "iso2": "CD",
      "iso3": "COD",
      "lat": 0,
      "long": 25,
      "flag": "https://disease.sh/assets/img/flags/cd.png"
    },
    "cases": 11122,
    "todayCases": 25,
    "deaths": 304,
    "todayDeaths": null,
    "recovered": 10379,
    "todayRecovered": null,
    "active": 439,
    "critical": null,
    "casesPerOneMillion": 123,
    "deathsPerOneMillion": 3,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 90385077,
    "continent": "Africa",
    "oneCasePerPeople": 8127,
    "oneDeathPerPeople": 297319,
    "oneTestPerPeople": null,
    "activePerOneMillion": 4.86,
    "recoveredPerOneMillion": 114.83,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523835,
    "country": "Denmark",
    "countryInfo": {
      "_id": 208,
      "iso2": "DK",
      "iso3": "DNK",
      "lat": 56,
      "long": 10,
      "flag": "https://disease.sh/assets/img/flags/dk.png"
    },
    "cases": 38622,
    "todayCases": 859,
    "deaths": 697,
    "todayDeaths": 3,
    "recovered": 31295,
    "todayRecovered": 418,
    "active": 6630,
    "critical": 18,
    "casesPerOneMillion": 6661,
    "deathsPerOneMillion": 120,
    "tests": 4801009,
    "testsPerOneMillion": 827958,
    "population": 5798615,
    "continent": "Europe",
    "oneCasePerPeople": 150,
    "oneDeathPerPeople": 8319,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 1143.38,
    "recoveredPerOneMillion": 5396.98,
    "criticalPerOneMillion": 3.1
  },
  {
    "updated": 1603500524164,
    "country": "Diamond Princess",
    "countryInfo": {
      "_id": null,
      "iso2": null,
      "iso3": null,
      "lat": 0,
      "long": 0,
      "flag": "https://disease.sh/assets/img/flags/unknown.png"
    },
    "cases": 712,
    "todayCases": null,
    "deaths": 13,
    "todayDeaths": null,
    "recovered": 659,
    "todayRecovered": null,
    "active": 40,
    "critical": 4,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": null,
    "testsPerOneMillion": null,
    "population": null,
    "continent": "",
    "oneCasePerPeople": null,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": null,
    "activePerOneMillion": null,
    "recoveredPerOneMillion": null,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524049,
    "country": "Djibouti",
    "countryInfo": {
      "_id": 262,
      "iso2": "DJ",
      "iso3": "DJI",
      "lat": 11.5,
      "long": 43,
      "flag": "https://disease.sh/assets/img/flags/dj.png"
    },
    "cases": 5528,
    "todayCases": 6,
    "deaths": 61,
    "todayDeaths": null,
    "recovered": 5393,
    "todayRecovered": 4,
    "active": 74,
    "critical": null,
    "casesPerOneMillion": 5570,
    "deathsPerOneMillion": 61,
    "tests": 83626,
    "testsPerOneMillion": 84262,
    "population": 992450,
    "continent": "Africa",
    "oneCasePerPeople": 180,
    "oneDeathPerPeople": 16270,
    "oneTestPerPeople": 12,
    "activePerOneMillion": 74.56,
    "recoveredPerOneMillion": 5434.03,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524255,
    "country": "Dominica",
    "countryInfo": {
      "_id": 212,
      "iso2": "DM",
      "iso3": "DMA",
      "lat": 15.4167,
      "long": -61.3333,
      "flag": "https://disease.sh/assets/img/flags/dm.png"
    },
    "cases": 37,
    "todayCases": 4,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 29,
    "todayRecovered": null,
    "active": 8,
    "critical": null,
    "casesPerOneMillion": 514,
    "deathsPerOneMillion": null,
    "tests": 4268,
    "testsPerOneMillion": 59243,
    "population": 72042,
    "continent": "North America",
    "oneCasePerPeople": 1947,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 17,
    "activePerOneMillion": 111.05,
    "recoveredPerOneMillion": 402.54,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523664,
    "country": "Dominican Republic",
    "countryInfo": {
      "_id": 214,
      "iso2": "DO",
      "iso3": "DOM",
      "lat": 19,
      "long": -70.6667,
      "flag": "https://disease.sh/assets/img/flags/do.png"
    },
    "cases": 122873,
    "todayCases": null,
    "deaths": 2212,
    "todayDeaths": null,
    "recovered": 100920,
    "todayRecovered": null,
    "active": 19741,
    "critical": 158,
    "casesPerOneMillion": 11292,
    "deathsPerOneMillion": 203,
    "tests": 554736,
    "testsPerOneMillion": 50978,
    "population": 10881814,
    "continent": "North America",
    "oneCasePerPeople": 89,
    "oneDeathPerPeople": 4919,
    "oneTestPerPeople": 20,
    "activePerOneMillion": 1814.13,
    "recoveredPerOneMillion": 9274.19,
    "criticalPerOneMillion": 14.52
  },
  {
    "updated": 1603500523659,
    "country": "Ecuador",
    "countryInfo": {
      "_id": 218,
      "iso2": "EC",
      "iso3": "ECU",
      "lat": -2,
      "long": -77.5,
      "flag": "https://disease.sh/assets/img/flags/ec.png"
    },
    "cases": 158270,
    "todayCases": 1819,
    "deaths": 12528,
    "todayDeaths": 28,
    "recovered": 134187,
    "todayRecovered": null,
    "active": 11555,
    "critical": 360,
    "casesPerOneMillion": 8929,
    "deathsPerOneMillion": 707,
    "tests": 514857,
    "testsPerOneMillion": 29045,
    "population": 17725952,
    "continent": "South America",
    "oneCasePerPeople": 112,
    "oneDeathPerPeople": 1415,
    "oneTestPerPeople": 34,
    "activePerOneMillion": 651.87,
    "recoveredPerOneMillion": 7570.09,
    "criticalPerOneMillion": 20.31
  },
  {
    "updated": 1603500523735,
    "country": "Egypt",
    "countryInfo": {
      "_id": 818,
      "iso2": "EG",
      "iso3": "EGY",
      "lat": 27,
      "long": 30,
      "flag": "https://disease.sh/assets/img/flags/eg.png"
    },
    "cases": 106230,
    "todayCases": 170,
    "deaths": 6176,
    "todayDeaths": 10,
    "recovered": 98713,
    "todayRecovered": 89,
    "active": 1341,
    "critical": 41,
    "casesPerOneMillion": 1032,
    "deathsPerOneMillion": 60,
    "tests": 135000,
    "testsPerOneMillion": 1312,
    "population": 102928483,
    "continent": "Africa",
    "oneCasePerPeople": 969,
    "oneDeathPerPeople": 16666,
    "oneTestPerPeople": 762,
    "activePerOneMillion": 13.03,
    "recoveredPerOneMillion": 959.04,
    "criticalPerOneMillion": 0.4
  },
  {
    "updated": 1603500523843,
    "country": "El Salvador",
    "countryInfo": {
      "_id": 222,
      "iso2": "SV",
      "iso3": "SLV",
      "lat": 13.8333,
      "long": -88.9167,
      "flag": "https://disease.sh/assets/img/flags/sv.png"
    },
    "cases": 32421,
    "todayCases": 159,
    "deaths": 940,
    "todayDeaths": 4,
    "recovered": 28127,
    "todayRecovered": 223,
    "active": 3354,
    "critical": 51,
    "casesPerOneMillion": 4991,
    "deathsPerOneMillion": 145,
    "tests": 456202,
    "testsPerOneMillion": 70223,
    "population": 6496474,
    "continent": "North America",
    "oneCasePerPeople": 200,
    "oneDeathPerPeople": 6911,
    "oneTestPerPeople": 14,
    "activePerOneMillion": 516.28,
    "recoveredPerOneMillion": 4329.58,
    "criticalPerOneMillion": 7.85
  },
  {
    "updated": 1603500524057,
    "country": "Equatorial Guinea",
    "countryInfo": {
      "_id": 226,
      "iso2": "GQ",
      "iso3": "GNQ",
      "lat": 2,
      "long": 10,
      "flag": "https://disease.sh/assets/img/flags/gq.png"
    },
    "cases": 5074,
    "todayCases": null,
    "deaths": 83,
    "todayDeaths": null,
    "recovered": 4961,
    "todayRecovered": null,
    "active": 30,
    "critical": 1,
    "casesPerOneMillion": 3581,
    "deathsPerOneMillion": 59,
    "tests": 64485,
    "testsPerOneMillion": 45512,
    "population": 1416875,
    "continent": "Africa",
    "oneCasePerPeople": 279,
    "oneDeathPerPeople": 17071,
    "oneTestPerPeople": 22,
    "activePerOneMillion": 21.17,
    "recoveredPerOneMillion": 3501.37,
    "criticalPerOneMillion": 0.71
  },
  {
    "updated": 1603500524238,
    "country": "Eritrea",
    "countryInfo": {
      "_id": 232,
      "iso2": "ER",
      "iso3": "ERI",
      "lat": 15,
      "long": 39,
      "flag": "https://disease.sh/assets/img/flags/er.png"
    },
    "cases": 461,
    "todayCases": 4,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 405,
    "todayRecovered": 14,
    "active": 56,
    "critical": null,
    "casesPerOneMillion": 129,
    "deathsPerOneMillion": null,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 3561638,
    "continent": "Africa",
    "oneCasePerPeople": 7726,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": null,
    "activePerOneMillion": 15.72,
    "recoveredPerOneMillion": 113.71,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524061,
    "country": "Estonia",
    "countryInfo": {
      "_id": 233,
      "iso2": "EE",
      "iso3": "EST",
      "lat": 59,
      "long": 26,
      "flag": "https://disease.sh/assets/img/flags/ee.png"
    },
    "cases": 4300,
    "todayCases": 53,
    "deaths": 73,
    "todayDeaths": 2,
    "recovered": 3418,
    "todayRecovered": 52,
    "active": 809,
    "critical": 1,
    "casesPerOneMillion": 3241,
    "deathsPerOneMillion": 55,
    "tests": 249726,
    "testsPerOneMillion": 188214,
    "population": 1326817,
    "continent": "Europe",
    "oneCasePerPeople": 309,
    "oneDeathPerPeople": 18176,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 609.73,
    "recoveredPerOneMillion": 2576.09,
    "criticalPerOneMillion": 0.75
  },
  {
    "updated": 1603500523744,
    "country": "Ethiopia",
    "countryInfo": {
      "_id": 231,
      "iso2": "ET",
      "iso3": "ETH",
      "lat": 8,
      "long": 38,
      "flag": "https://disease.sh/assets/img/flags/et.png"
    },
    "cases": 92229,
    "todayCases": 536,
    "deaths": 1400,
    "todayDeaths": 4,
    "recovered": 46118,
    "todayRecovered": 858,
    "active": 44711,
    "critical": 315,
    "casesPerOneMillion": 796,
    "deathsPerOneMillion": 12,
    "tests": 1430043,
    "testsPerOneMillion": 12346,
    "population": 115832447,
    "continent": "Africa",
    "oneCasePerPeople": 1256,
    "oneDeathPerPeople": 82737,
    "oneTestPerPeople": 81,
    "activePerOneMillion": 386,
    "recoveredPerOneMillion": 398.14,
    "criticalPerOneMillion": 2.72
  },
  {
    "updated": 1603500524265,
    "country": "Falkland Islands (Malvinas)",
    "countryInfo": {
      "_id": 238,
      "iso2": "FK",
      "iso3": "FLK",
      "lat": -51.75,
      "long": -59,
      "flag": "https://disease.sh/assets/img/flags/fk.png"
    },
    "cases": 13,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 13,
    "todayRecovered": null,
    "active": 0,
    "critical": null,
    "casesPerOneMillion": 3703,
    "deathsPerOneMillion": null,
    "tests": 2682,
    "testsPerOneMillion": 763885,
    "population": 3511,
    "continent": "South America",
    "oneCasePerPeople": 270,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 0,
    "recoveredPerOneMillion": 3702.65,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524237,
    "country": "Faroe Islands",
    "countryInfo": {
      "_id": 234,
      "iso2": "FO",
      "iso3": "FRO",
      "lat": 62,
      "long": -7,
      "flag": "https://disease.sh/assets/img/flags/fo.png"
    },
    "cases": 490,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 473,
    "todayRecovered": null,
    "active": 17,
    "critical": null,
    "casesPerOneMillion": 10016,
    "deathsPerOneMillion": null,
    "tests": 148854,
    "testsPerOneMillion": 3042742,
    "population": 48921,
    "continent": "Europe",
    "oneCasePerPeople": 100,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": null,
    "activePerOneMillion": 347.5,
    "recoveredPerOneMillion": 9668.65,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524255,
    "country": "Fiji",
    "countryInfo": {
      "_id": 242,
      "iso2": "FJ",
      "iso3": "FJI",
      "lat": -18,
      "long": 175,
      "flag": "https://disease.sh/assets/img/flags/fj.png"
    },
    "cases": 33,
    "todayCases": null,
    "deaths": 2,
    "todayDeaths": null,
    "recovered": 30,
    "todayRecovered": null,
    "active": 1,
    "critical": null,
    "casesPerOneMillion": 37,
    "deathsPerOneMillion": 2,
    "tests": 12125,
    "testsPerOneMillion": 13495,
    "population": 898477,
    "continent": "Australia/Oceania",
    "oneCasePerPeople": 27227,
    "oneDeathPerPeople": 449239,
    "oneTestPerPeople": 74,
    "activePerOneMillion": 1.11,
    "recoveredPerOneMillion": 33.39,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523941,
    "country": "Finland",
    "countryInfo": {
      "_id": 246,
      "iso2": "FI",
      "iso3": "FIN",
      "lat": 64,
      "long": 26,
      "flag": "https://disease.sh/assets/img/flags/fi.png"
    },
    "cases": 14474,
    "todayCases": 219,
    "deaths": 353,
    "todayDeaths": null,
    "recovered": 9800,
    "todayRecovered": null,
    "active": 4321,
    "critical": 11,
    "casesPerOneMillion": 2611,
    "deathsPerOneMillion": 64,
    "tests": 1362069,
    "testsPerOneMillion": 245709,
    "population": 5543433,
    "continent": "Europe",
    "oneCasePerPeople": 383,
    "oneDeathPerPeople": 15704,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 779.48,
    "recoveredPerOneMillion": 1767.86,
    "criticalPerOneMillion": 1.98
  },
  {
    "updated": 1603500523557,
    "country": "France",
    "countryInfo": {
      "_id": 250,
      "iso2": "FR",
      "iso3": "FRA",
      "lat": 46,
      "long": 2,
      "flag": "https://disease.sh/assets/img/flags/fr.png"
    },
    "cases": 1041075,
    "todayCases": 42032,
    "deaths": 34508,
    "todayDeaths": 298,
    "recovered": 109486,
    "todayRecovered": 887,
    "active": 897081,
    "critical": 2441,
    "casesPerOneMillion": 15938,
    "deathsPerOneMillion": 528,
    "tests": 14406499,
    "testsPerOneMillion": 220556,
    "population": 65318998,
    "continent": "Europe",
    "oneCasePerPeople": 63,
    "oneDeathPerPeople": 1893,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 13733.85,
    "recoveredPerOneMillion": 1676.17,
    "criticalPerOneMillion": 37.37
  },
  {
    "updated": 1603500523955,
    "country": "French Guiana",
    "countryInfo": {
      "_id": 254,
      "iso2": "GF",
      "iso3": "GUF",
      "lat": 4,
      "long": -53,
      "flag": "https://disease.sh/assets/img/flags/gf.png"
    },
    "cases": 10351,
    "todayCases": 9,
    "deaths": 69,
    "todayDeaths": null,
    "recovered": 9995,
    "todayRecovered": null,
    "active": 287,
    "critical": 2,
    "casesPerOneMillion": 34384,
    "deathsPerOneMillion": 229,
    "tests": 72900,
    "testsPerOneMillion": 242161,
    "population": 301040,
    "continent": "South America",
    "oneCasePerPeople": 29,
    "oneDeathPerPeople": 4363,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 953.36,
    "recoveredPerOneMillion": 33201.57,
    "criticalPerOneMillion": 6.64
  },
  {
    "updated": 1603500524048,
    "country": "French Polynesia",
    "countryInfo": {
      "_id": 258,
      "iso2": "PF",
      "iso3": "PYF",
      "lat": -15,
      "long": -140,
      "flag": "https://disease.sh/assets/img/flags/pf.png"
    },
    "cases": 5797,
    "todayCases": 636,
    "deaths": 20,
    "todayDeaths": 1,
    "recovered": 3623,
    "todayRecovered": 87,
    "active": 2154,
    "critical": 17,
    "casesPerOneMillion": 20599,
    "deathsPerOneMillion": 71,
    "tests": 26355,
    "testsPerOneMillion": 93651,
    "population": 281417,
    "continent": "Australia/Oceania",
    "oneCasePerPeople": 49,
    "oneDeathPerPeople": 14071,
    "oneTestPerPeople": 11,
    "activePerOneMillion": 7654.12,
    "recoveredPerOneMillion": 12874.13,
    "criticalPerOneMillion": 60.41
  },
  {
    "updated": 1603500524036,
    "country": "Gabon",
    "countryInfo": {
      "_id": 266,
      "iso2": "GA",
      "iso3": "GAB",
      "lat": -1,
      "long": 11.75,
      "flag": "https://disease.sh/assets/img/flags/ga.png"
    },
    "cases": 8919,
    "todayCases": 18,
    "deaths": 54,
    "todayDeaths": null,
    "recovered": 8512,
    "todayRecovered": 33,
    "active": 353,
    "critical": 3,
    "casesPerOneMillion": 3979,
    "deathsPerOneMillion": 24,
    "tests": 225105,
    "testsPerOneMillion": 100413,
    "population": 2241786,
    "continent": "Africa",
    "oneCasePerPeople": 251,
    "oneDeathPerPeople": 41515,
    "oneTestPerPeople": 10,
    "activePerOneMillion": 157.46,
    "recoveredPerOneMillion": 3796.97,
    "criticalPerOneMillion": 1.34
  },
  {
    "updated": 1603500524141,
    "country": "Gambia",
    "countryInfo": {
      "_id": 270,
      "iso2": "GM",
      "iso3": "GMB",
      "lat": 13.4667,
      "long": -16.5667,
      "flag": "https://disease.sh/assets/img/flags/gm.png"
    },
    "cases": 3659,
    "todayCases": null,
    "deaths": 119,
    "todayDeaths": null,
    "recovered": 2660,
    "todayRecovered": null,
    "active": 880,
    "critical": null,
    "casesPerOneMillion": 1501,
    "deathsPerOneMillion": 49,
    "tests": 18657,
    "testsPerOneMillion": 7655,
    "population": 2437279,
    "continent": "Africa",
    "oneCasePerPeople": 666,
    "oneDeathPerPeople": 20481,
    "oneTestPerPeople": 131,
    "activePerOneMillion": 361.06,
    "recoveredPerOneMillion": 1091.38,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523849,
    "country": "Georgia",
    "countryInfo": {
      "_id": 268,
      "iso2": "GE",
      "iso3": "GEO",
      "lat": 42,
      "long": 43.5,
      "flag": "https://disease.sh/assets/img/flags/ge.png"
    },
    "cases": 24562,
    "todayCases": 1759,
    "deaths": 183,
    "todayDeaths": 5,
    "recovered": 9751,
    "todayRecovered": 350,
    "active": 14628,
    "critical": null,
    "casesPerOneMillion": 6161,
    "deathsPerOneMillion": 46,
    "tests": 800789,
    "testsPerOneMillion": 200863,
    "population": 3986743,
    "continent": "Asia",
    "oneCasePerPeople": 162,
    "oneDeathPerPeople": 21785,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 3669.16,
    "recoveredPerOneMillion": 2445.86,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523569,
    "country": "Germany",
    "countryInfo": {
      "_id": 276,
      "iso2": "DE",
      "iso3": "DEU",
      "lat": 51,
      "long": 9,
      "flag": "https://disease.sh/assets/img/flags/de.png"
    },
    "cases": 417350,
    "todayCases": 13476,
    "deaths": 10090,
    "todayDeaths": 46,
    "recovered": 310200,
    "todayRecovered": 4100,
    "active": 97060,
    "critical": 1121,
    "casesPerOneMillion": 4976,
    "deathsPerOneMillion": 120,
    "tests": 20380376,
    "testsPerOneMillion": 243005,
    "population": 83868205,
    "continent": "Europe",
    "oneCasePerPeople": 201,
    "oneDeathPerPeople": 8312,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 1157.29,
    "recoveredPerOneMillion": 3698.66,
    "criticalPerOneMillion": 13.37
  },
  {
    "updated": 1603500523771,
    "country": "Ghana",
    "countryInfo": {
      "_id": 288,
      "iso2": "GH",
      "iso3": "GHA",
      "lat": 8,
      "long": -2,
      "flag": "https://disease.sh/assets/img/flags/gh.png"
    },
    "cases": 47601,
    "todayCases": 63,
    "deaths": 314,
    "todayDeaths": 2,
    "recovered": 46824,
    "todayRecovered": 35,
    "active": 463,
    "critical": 9,
    "casesPerOneMillion": 1522,
    "deathsPerOneMillion": 10,
    "tests": 515890,
    "testsPerOneMillion": 16497,
    "population": 31271992,
    "continent": "Africa",
    "oneCasePerPeople": 657,
    "oneDeathPerPeople": 99592,
    "oneTestPerPeople": 61,
    "activePerOneMillion": 14.81,
    "recoveredPerOneMillion": 1497.31,
    "criticalPerOneMillion": 0.29
  },
  {
    "updated": 1603500524167,
    "country": "Gibraltar",
    "countryInfo": {
      "_id": 292,
      "iso2": "GI",
      "iso3": "GIB",
      "lat": 36.1833,
      "long": -5.3667,
      "flag": "https://disease.sh/assets/img/flags/gi.png"
    },
    "cases": 641,
    "todayCases": 11,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 500,
    "todayRecovered": 5,
    "active": 141,
    "critical": 13,
    "casesPerOneMillion": 19028,
    "deathsPerOneMillion": null,
    "tests": 60887,
    "testsPerOneMillion": 1807379,
    "population": 33688,
    "continent": "Europe",
    "oneCasePerPeople": 53,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 4185.47,
    "recoveredPerOneMillion": 14842.08,
    "criticalPerOneMillion": 385.89
  },
  {
    "updated": 1603500523845,
    "country": "Greece",
    "countryInfo": {
      "_id": 300,
      "iso2": "GR",
      "iso3": "GRC",
      "lat": 39,
      "long": 22,
      "flag": "https://disease.sh/assets/img/flags/gr.png"
    },
    "cases": 29057,
    "todayCases": 841,
    "deaths": 559,
    "todayDeaths": 10,
    "recovered": 9989,
    "todayRecovered": null,
    "active": 18509,
    "critical": 89,
    "casesPerOneMillion": 2792,
    "deathsPerOneMillion": 54,
    "tests": 1629489,
    "testsPerOneMillion": 156578,
    "population": 10406876,
    "continent": "Europe",
    "oneCasePerPeople": 358,
    "oneDeathPerPeople": 18617,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 1778.54,
    "recoveredPerOneMillion": 959.85,
    "criticalPerOneMillion": 8.55
  },
  {
    "updated": 1603500524262,
    "country": "Greenland",
    "countryInfo": {
      "_id": 304,
      "iso2": "GL",
      "iso3": "GRL",
      "lat": 72,
      "long": -40,
      "flag": "https://disease.sh/assets/img/flags/gl.png"
    },
    "cases": 17,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 16,
    "todayRecovered": null,
    "active": 1,
    "critical": null,
    "casesPerOneMillion": 299,
    "deathsPerOneMillion": null,
    "tests": 10273,
    "testsPerOneMillion": 180859,
    "population": 56801,
    "continent": "North America",
    "oneCasePerPeople": 3341,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 17.61,
    "recoveredPerOneMillion": 281.69,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524257,
    "country": "Grenada",
    "countryInfo": {
      "_id": 308,
      "iso2": "GD",
      "iso3": "GRD",
      "lat": 12.1167,
      "long": -61.6667,
      "flag": "https://disease.sh/assets/img/flags/gd.png"
    },
    "cases": 27,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 24,
    "todayRecovered": null,
    "active": 3,
    "critical": null,
    "casesPerOneMillion": 240,
    "deathsPerOneMillion": null,
    "tests": 6252,
    "testsPerOneMillion": 55481,
    "population": 112687,
    "continent": "North America",
    "oneCasePerPeople": 4174,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 18,
    "activePerOneMillion": 26.62,
    "recoveredPerOneMillion": 212.98,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524041,
    "country": "Guadeloupe",
    "countryInfo": {
      "_id": 312,
      "iso2": "GP",
      "iso3": "GLP",
      "lat": 16.25,
      "long": -61.5833,
      "flag": "https://disease.sh/assets/img/flags/gp.png"
    },
    "cases": 7329,
    "todayCases": null,
    "deaths": 115,
    "todayDeaths": null,
    "recovered": 2199,
    "todayRecovered": null,
    "active": 5015,
    "critical": 35,
    "casesPerOneMillion": 18316,
    "deathsPerOneMillion": 287,
    "tests": 65030,
    "testsPerOneMillion": 162516,
    "population": 400146,
    "continent": "North America",
    "oneCasePerPeople": 55,
    "oneDeathPerPeople": 3480,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 12532.93,
    "recoveredPerOneMillion": 5495.49,
    "criticalPerOneMillion": 87.47
  },
  {
    "updated": 1603500523736,
    "country": "Guatemala",
    "countryInfo": {
      "_id": 320,
      "iso2": "GT",
      "iso3": "GTM",
      "lat": 15.5,
      "long": -90.25,
      "flag": "https://disease.sh/assets/img/flags/gt.png"
    },
    "cases": 103902,
    "todayCases": 730,
    "deaths": 3594,
    "todayDeaths": 14,
    "recovered": 93341,
    "todayRecovered": 676,
    "active": 6967,
    "critical": 5,
    "casesPerOneMillion": 5767,
    "deathsPerOneMillion": 199,
    "tests": 404460,
    "testsPerOneMillion": 22448,
    "population": 18017627,
    "continent": "North America",
    "oneCasePerPeople": 173,
    "oneDeathPerPeople": 5013,
    "oneTestPerPeople": 45,
    "activePerOneMillion": 386.68,
    "recoveredPerOneMillion": 5180.54,
    "criticalPerOneMillion": 0.28
  },
  {
    "updated": 1603500523946,
    "country": "Guinea",
    "countryInfo": {
      "_id": 324,
      "iso2": "GN",
      "iso3": "GIN",
      "lat": 11,
      "long": -10,
      "flag": "https://disease.sh/assets/img/flags/gn.png"
    },
    "cases": 11635,
    "todayCases": null,
    "deaths": 71,
    "todayDeaths": null,
    "recovered": 10474,
    "todayRecovered": null,
    "active": 1090,
    "critical": 24,
    "casesPerOneMillion": 879,
    "deathsPerOneMillion": 5,
    "tests": 40998,
    "testsPerOneMillion": 3096,
    "population": 13241097,
    "continent": "Africa",
    "oneCasePerPeople": 1138,
    "oneDeathPerPeople": 186494,
    "oneTestPerPeople": 323,
    "activePerOneMillion": 82.32,
    "recoveredPerOneMillion": 791.02,
    "criticalPerOneMillion": 1.81
  },
  {
    "updated": 1603500524149,
    "country": "Guinea-Bissau",
    "countryInfo": {
      "_id": 624,
      "iso2": "GW",
      "iso3": "GNB",
      "lat": 12,
      "long": -15,
      "flag": "https://disease.sh/assets/img/flags/gw.png"
    },
    "cases": 2403,
    "todayCases": null,
    "deaths": 41,
    "todayDeaths": null,
    "recovered": 1818,
    "todayRecovered": null,
    "active": 544,
    "critical": 5,
    "casesPerOneMillion": 1212,
    "deathsPerOneMillion": 21,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 1982217,
    "continent": "Africa",
    "oneCasePerPeople": 825,
    "oneDeathPerPeople": 48347,
    "oneTestPerPeople": null,
    "activePerOneMillion": 274.44,
    "recoveredPerOneMillion": 917.15,
    "criticalPerOneMillion": 2.52
  },
  {
    "updated": 1603500524138,
    "country": "Guyana",
    "countryInfo": {
      "_id": 328,
      "iso2": "GY",
      "iso3": "GUY",
      "lat": 5,
      "long": -59,
      "flag": "https://disease.sh/assets/img/flags/gy.png"
    },
    "cases": 3960,
    "todayCases": 83,
    "deaths": 117,
    "todayDeaths": null,
    "recovered": 2923,
    "todayRecovered": 70,
    "active": 920,
    "critical": 13,
    "casesPerOneMillion": 5027,
    "deathsPerOneMillion": 149,
    "tests": 17841,
    "testsPerOneMillion": 22648,
    "population": 787743,
    "continent": "South America",
    "oneCasePerPeople": 199,
    "oneDeathPerPeople": 6733,
    "oneTestPerPeople": 44,
    "activePerOneMillion": 1167.89,
    "recoveredPerOneMillion": 3710.6,
    "criticalPerOneMillion": 16.5
  },
  {
    "updated": 1603500523958,
    "country": "Haiti",
    "countryInfo": {
      "_id": 332,
      "iso2": "HT",
      "iso3": "HTI",
      "lat": 19,
      "long": -72.4167,
      "flag": "https://disease.sh/assets/img/flags/ht.png"
    },
    "cases": 9015,
    "todayCases": 8,
    "deaths": 231,
    "todayDeaths": null,
    "recovered": 7361,
    "todayRecovered": 50,
    "active": 1423,
    "critical": null,
    "casesPerOneMillion": 788,
    "deathsPerOneMillion": 20,
    "tests": 31783,
    "testsPerOneMillion": 2777,
    "population": 11445721,
    "continent": "North America",
    "oneCasePerPeople": 1270,
    "oneDeathPerPeople": 49549,
    "oneTestPerPeople": 360,
    "activePerOneMillion": 124.33,
    "recoveredPerOneMillion": 643.12,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524259,
    "country": "Holy See (Vatican City State)",
    "countryInfo": {
      "_id": 336,
      "iso2": "VA",
      "iso3": "VAT",
      "lat": 41.9,
      "long": 12.45,
      "flag": "https://disease.sh/assets/img/flags/va.png"
    },
    "cases": 27,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 15,
    "todayRecovered": null,
    "active": 12,
    "critical": null,
    "casesPerOneMillion": 33666,
    "deathsPerOneMillion": null,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 802,
    "continent": "Europe",
    "oneCasePerPeople": 30,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": null,
    "activePerOneMillion": 14962.59,
    "recoveredPerOneMillion": 18703.24,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523745,
    "country": "Honduras",
    "countryInfo": {
      "_id": 340,
      "iso2": "HN",
      "iso3": "HND",
      "lat": 15,
      "long": -86.5,
      "flag": "https://disease.sh/assets/img/flags/hn.png"
    },
    "cases": 91509,
    "todayCases": 431,
    "deaths": 2604,
    "todayDeaths": 8,
    "recovered": 37132,
    "todayRecovered": 791,
    "active": 51773,
    "critical": 27,
    "casesPerOneMillion": 9194,
    "deathsPerOneMillion": 262,
    "tests": 214418,
    "testsPerOneMillion": 21542,
    "population": 9953301,
    "continent": "North America",
    "oneCasePerPeople": 109,
    "oneDeathPerPeople": 3822,
    "oneTestPerPeople": 46,
    "activePerOneMillion": 5201.59,
    "recoveredPerOneMillion": 3730.62,
    "criticalPerOneMillion": 2.71
  },
  {
    "updated": 1603500524053,
    "country": "Hong Kong",
    "countryInfo": {
      "_id": 344,
      "iso2": "HK",
      "iso3": "HKG",
      "lat": 22.25,
      "long": 114.1667,
      "flag": "https://disease.sh/assets/img/flags/hk.png"
    },
    "cases": 5285,
    "todayCases": 4,
    "deaths": 105,
    "todayDeaths": null,
    "recovered": 5029,
    "todayRecovered": 10,
    "active": 151,
    "critical": 13,
    "casesPerOneMillion": 703,
    "deathsPerOneMillion": 14,
    "tests": 3587019,
    "testsPerOneMillion": 477252,
    "population": 7515987,
    "continent": "Asia",
    "oneCasePerPeople": 1422,
    "oneDeathPerPeople": 71581,
    "oneTestPerPeople": 2,
    "activePerOneMillion": 20.09,
    "recoveredPerOneMillion": 669.11,
    "criticalPerOneMillion": 1.73
  },
  {
    "updated": 1603500523764,
    "country": "Hungary",
    "countryInfo": {
      "_id": 348,
      "iso2": "HU",
      "iso3": "HUN",
      "lat": 47,
      "long": 20,
      "flag": "https://disease.sh/assets/img/flags/hu.png"
    },
    "cases": 54278,
    "todayCases": 2066,
    "deaths": 1352,
    "todayDeaths": 47,
    "recovered": 15655,
    "todayRecovered": 401,
    "active": 37271,
    "critical": 200,
    "casesPerOneMillion": 5623,
    "deathsPerOneMillion": 140,
    "tests": 949470,
    "testsPerOneMillion": 98364,
    "population": 9652579,
    "continent": "Europe",
    "oneCasePerPeople": 178,
    "oneDeathPerPeople": 7139,
    "oneTestPerPeople": 10,
    "activePerOneMillion": 3861.25,
    "recoveredPerOneMillion": 1621.85,
    "criticalPerOneMillion": 20.72
  },
  {
    "updated": 1603500524060,
    "country": "Iceland",
    "countryInfo": {
      "_id": 352,
      "iso2": "IS",
      "iso3": "ISL",
      "lat": 65,
      "long": -18,
      "flag": "https://disease.sh/assets/img/flags/is.png"
    },
    "cases": 4308,
    "todayCases": 40,
    "deaths": 11,
    "todayDeaths": null,
    "recovered": 3187,
    "todayRecovered": 89,
    "active": 1110,
    "critical": 3,
    "casesPerOneMillion": 12599,
    "deathsPerOneMillion": 32,
    "tests": 335426,
    "testsPerOneMillion": 980958,
    "population": 341937,
    "continent": "Europe",
    "oneCasePerPeople": 79,
    "oneDeathPerPeople": 31085,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 3246.21,
    "recoveredPerOneMillion": 9320.43,
    "criticalPerOneMillion": 8.77
  },
  {
    "updated": 1603500523551,
    "country": "India",
    "countryInfo": {
      "_id": 356,
      "iso2": "IN",
      "iso3": "IND",
      "lat": 20,
      "long": 77,
      "flag": "https://disease.sh/assets/img/flags/in.png"
    },
    "cases": 7813668,
    "todayCases": 54028,
    "deaths": 117992,
    "todayDeaths": 656,
    "recovered": 7013569,
    "todayRecovered": 67244,
    "active": 682107,
    "critical": 8944,
    "casesPerOneMillion": 5645,
    "deathsPerOneMillion": 85,
    "tests": 100113085,
    "testsPerOneMillion": 72324,
    "population": 1384234140,
    "continent": "Asia",
    "oneCasePerPeople": 177,
    "oneDeathPerPeople": 11732,
    "oneTestPerPeople": 14,
    "activePerOneMillion": 492.77,
    "recoveredPerOneMillion": 5066.75,
    "criticalPerOneMillion": 6.46
  },
  {
    "updated": 1603500523639,
    "country": "Indonesia",
    "countryInfo": {
      "_id": 360,
      "iso2": "ID",
      "iso3": "IDN",
      "lat": -5,
      "long": 120,
      "flag": "https://disease.sh/assets/img/flags/id.png"
    },
    "cases": 381910,
    "todayCases": 4369,
    "deaths": 13077,
    "todayDeaths": 118,
    "recovered": 305100,
    "todayRecovered": 4094,
    "active": 63733,
    "critical": null,
    "casesPerOneMillion": 1392,
    "deathsPerOneMillion": 48,
    "tests": 4253425,
    "testsPerOneMillion": 15499,
    "population": 274424390,
    "continent": "Asia",
    "oneCasePerPeople": 719,
    "oneDeathPerPeople": 20985,
    "oneTestPerPeople": 65,
    "activePerOneMillion": 232.24,
    "recoveredPerOneMillion": 1111.78,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523565,
    "country": "Iran",
    "countryInfo": {
      "_id": 364,
      "iso2": "IR",
      "iso3": "IRN",
      "lat": 32,
      "long": 53,
      "flag": "https://disease.sh/assets/img/flags/ir.png"
    },
    "cases": 556891,
    "todayCases": 6134,
    "deaths": 31985,
    "todayDeaths": 335,
    "recovered": 446685,
    "todayRecovered": 4011,
    "active": 78221,
    "critical": 4933,
    "casesPerOneMillion": 6604,
    "deathsPerOneMillion": 379,
    "tests": 4658727,
    "testsPerOneMillion": 55246,
    "population": 84326729,
    "continent": "Asia",
    "oneCasePerPeople": 151,
    "oneDeathPerPeople": 2636,
    "oneTestPerPeople": 18,
    "activePerOneMillion": 927.59,
    "recoveredPerOneMillion": 5297.07,
    "criticalPerOneMillion": 58.5
  },
  {
    "updated": 1603500523568,
    "country": "Iraq",
    "countryInfo": {
      "_id": 368,
      "iso2": "IQ",
      "iso3": "IRQ",
      "lat": 33,
      "long": 44,
      "flag": "https://disease.sh/assets/img/flags/iq.png"
    },
    "cases": 445949,
    "todayCases": 3785,
    "deaths": 10513,
    "todayDeaths": 48,
    "recovered": 375188,
    "todayRecovered": 3362,
    "active": 60248,
    "critical": 434,
    "casesPerOneMillion": 11011,
    "deathsPerOneMillion": 260,
    "tests": 2724328,
    "testsPerOneMillion": 67269,
    "population": 40498846,
    "continent": "Asia",
    "oneCasePerPeople": 91,
    "oneDeathPerPeople": 3852,
    "oneTestPerPeople": 15,
    "activePerOneMillion": 1487.65,
    "recoveredPerOneMillion": 9264.17,
    "criticalPerOneMillion": 10.72
  },
  {
    "updated": 1603500523761,
    "country": "Ireland",
    "countryInfo": {
      "_id": 372,
      "iso2": "IE",
      "iso3": "IRL",
      "lat": 53,
      "long": -8,
      "flag": "https://disease.sh/assets/img/flags/ie.png"
    },
    "cases": 55261,
    "todayCases": 785,
    "deaths": 1878,
    "todayDeaths": 7,
    "recovered": 23364,
    "todayRecovered": null,
    "active": 30019,
    "critical": 37,
    "casesPerOneMillion": 11153,
    "deathsPerOneMillion": 379,
    "tests": 1520643,
    "testsPerOneMillion": 306894,
    "population": 4954950,
    "continent": "Europe",
    "oneCasePerPeople": 90,
    "oneDeathPerPeople": 2638,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 6058.39,
    "recoveredPerOneMillion": 4715.28,
    "criticalPerOneMillion": 7.47
  },
  {
    "updated": 1603500524240,
    "country": "Isle of Man",
    "countryInfo": {
      "_id": 833,
      "iso2": "IM",
      "iso3": "IMN",
      "lat": 54.23,
      "long": -4.55,
      "flag": "https://disease.sh/assets/img/flags/im.png"
    },
    "cases": 348,
    "todayCases": null,
    "deaths": 24,
    "todayDeaths": null,
    "recovered": 321,
    "todayRecovered": null,
    "active": 3,
    "critical": null,
    "casesPerOneMillion": 4086,
    "deathsPerOneMillion": 282,
    "tests": 15569,
    "testsPerOneMillion": 182791,
    "population": 85174,
    "continent": "Europe",
    "oneCasePerPeople": 245,
    "oneDeathPerPeople": 3549,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 35.22,
    "recoveredPerOneMillion": 3768.76,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523650,
    "country": "Israel",
    "countryInfo": {
      "_id": 376,
      "iso2": "IL",
      "iso3": "ISR",
      "lat": 31.5,
      "long": 34.75,
      "flag": "https://disease.sh/assets/img/flags/il.png"
    },
    "cases": 308840,
    "todayCases": 593,
    "deaths": 2329,
    "todayDeaths": 10,
    "recovered": 290130,
    "todayRecovered": 1793,
    "active": 16381,
    "critical": 573,
    "casesPerOneMillion": 33578,
    "deathsPerOneMillion": 253,
    "tests": 4377294,
    "testsPerOneMillion": 475917,
    "population": 9197590,
    "continent": "Asia",
    "oneCasePerPeople": 30,
    "oneDeathPerPeople": 3949,
    "oneTestPerPeople": 2,
    "activePerOneMillion": 1781.01,
    "recoveredPerOneMillion": 31544.13,
    "criticalPerOneMillion": 62.3
  },
  {
    "updated": 1603500523567,
    "country": "Italy",
    "countryInfo": {
      "_id": 380,
      "iso2": "IT",
      "iso3": "ITA",
      "lat": 42.8333,
      "long": 12.8333,
      "flag": "https://disease.sh/assets/img/flags/it.png"
    },
    "cases": 484869,
    "todayCases": 19143,
    "deaths": 37059,
    "todayDeaths": 91,
    "recovered": 261808,
    "todayRecovered": 2352,
    "active": 186002,
    "critical": 1049,
    "casesPerOneMillion": 8023,
    "deathsPerOneMillion": 613,
    "tests": 14314453,
    "testsPerOneMillion": 236862,
    "population": 60433695,
    "continent": "Europe",
    "oneCasePerPeople": 125,
    "oneDeathPerPeople": 1631,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 3077.79,
    "recoveredPerOneMillion": 4332.15,
    "criticalPerOneMillion": 17.36
  },
  {
    "updated": 1603500524038,
    "country": "Jamaica",
    "countryInfo": {
      "_id": 388,
      "iso2": "JM",
      "iso3": "JAM",
      "lat": 18.25,
      "long": -77.5,
      "flag": "https://disease.sh/assets/img/flags/jm.png"
    },
    "cases": 8638,
    "todayCases": 38,
    "deaths": 182,
    "todayDeaths": 3,
    "recovered": 4156,
    "todayRecovered": 61,
    "active": 4300,
    "critical": 8,
    "casesPerOneMillion": 2913,
    "deathsPerOneMillion": 61,
    "tests": 91495,
    "testsPerOneMillion": 30856,
    "population": 2965226,
    "continent": "North America",
    "oneCasePerPeople": 343,
    "oneDeathPerPeople": 16292,
    "oneTestPerPeople": 32,
    "activePerOneMillion": 1450.14,
    "recoveredPerOneMillion": 1401.58,
    "criticalPerOneMillion": 2.7
  },
  {
    "updated": 1603500523741,
    "country": "Japan",
    "countryInfo": {
      "_id": 392,
      "iso2": "JP",
      "iso3": "JPN",
      "lat": 36,
      "long": 138,
      "flag": "https://disease.sh/assets/img/flags/jp.png"
    },
    "cases": 95138,
    "todayCases": 614,
    "deaths": 1694,
    "todayDeaths": 9,
    "recovered": 88245,
    "todayRecovered": 579,
    "active": 5199,
    "critical": 151,
    "casesPerOneMillion": 753,
    "deathsPerOneMillion": 13,
    "tests": 2531971,
    "testsPerOneMillion": 20039,
    "population": 126353709,
    "continent": "Asia",
    "oneCasePerPeople": 1328,
    "oneDeathPerPeople": 74589,
    "oneTestPerPeople": 50,
    "activePerOneMillion": 41.15,
    "recoveredPerOneMillion": 698.4,
    "criticalPerOneMillion": 1.2
  },
  {
    "updated": 1603500523767,
    "country": "Jordan",
    "countryInfo": {
      "_id": 400,
      "iso2": "JO",
      "iso3": "JOR",
      "lat": 31,
      "long": 36,
      "flag": "https://disease.sh/assets/img/flags/jo.png"
    },
    "cases": 48930,
    "todayCases": 2489,
    "deaths": 508,
    "todayDeaths": 27,
    "recovered": 7449,
    "todayRecovered": 109,
    "active": 40973,
    "critical": 55,
    "casesPerOneMillion": 4781,
    "deathsPerOneMillion": 50,
    "tests": 1683236,
    "testsPerOneMillion": 164464,
    "population": 10234708,
    "continent": "Asia",
    "oneCasePerPeople": 209,
    "oneDeathPerPeople": 20147,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 4003.34,
    "recoveredPerOneMillion": 727.82,
    "criticalPerOneMillion": 5.37
  },
  {
    "updated": 1603500523674,
    "country": "Kazakhstan",
    "countryInfo": {
      "_id": 398,
      "iso2": "KZ",
      "iso3": "KAZ",
      "lat": 48,
      "long": 68,
      "flag": "https://disease.sh/assets/img/flags/kz.png"
    },
    "cases": 110086,
    "todayCases": 179,
    "deaths": 1796,
    "todayDeaths": null,
    "recovered": 105493,
    "todayRecovered": 108,
    "active": 2797,
    "critical": 221,
    "casesPerOneMillion": 5841,
    "deathsPerOneMillion": 95,
    "tests": 3309626,
    "testsPerOneMillion": 175609,
    "population": 18846520,
    "continent": "Asia",
    "oneCasePerPeople": 171,
    "oneDeathPerPeople": 10494,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 148.41,
    "recoveredPerOneMillion": 5597.48,
    "criticalPerOneMillion": 11.73
  },
  {
    "updated": 1603500523770,
    "country": "Kenya",
    "countryInfo": {
      "_id": 404,
      "iso2": "KE",
      "iso3": "KEN",
      "lat": 1,
      "long": 38,
      "flag": "https://disease.sh/assets/img/flags/ke.png"
    },
    "cases": 47843,
    "todayCases": 631,
    "deaths": 884,
    "todayDeaths": 14,
    "recovered": 33421,
    "todayRecovered": 371,
    "active": 13538,
    "critical": 20,
    "casesPerOneMillion": 884,
    "deathsPerOneMillion": 16,
    "tests": 646367,
    "testsPerOneMillion": 11940,
    "population": 54134164,
    "continent": "Africa",
    "oneCasePerPeople": 1131,
    "oneDeathPerPeople": 61238,
    "oneTestPerPeople": 84,
    "activePerOneMillion": 250.08,
    "recoveredPerOneMillion": 617.37,
    "criticalPerOneMillion": 0.37
  },
  {
    "updated": 1603500523668,
    "country": "Kuwait",
    "countryInfo": {
      "_id": 414,
      "iso2": "KW",
      "iso3": "KWT",
      "lat": 29.3375,
      "long": 47.6581,
      "flag": "https://disease.sh/assets/img/flags/kw.png"
    },
    "cases": 120232,
    "todayCases": 812,
    "deaths": 740,
    "todayDeaths": 10,
    "recovered": 111440,
    "todayRecovered": 726,
    "active": 8052,
    "critical": 122,
    "casesPerOneMillion": 28025,
    "deathsPerOneMillion": 172,
    "tests": 865560,
    "testsPerOneMillion": 201756,
    "population": 4290125,
    "continent": "Asia",
    "oneCasePerPeople": 36,
    "oneDeathPerPeople": 5797,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 1876.87,
    "recoveredPerOneMillion": 25975.93,
    "criticalPerOneMillion": 28.44
  },
  {
    "updated": 1603500523763,
    "country": "Kyrgyzstan",
    "countryInfo": {
      "_id": 417,
      "iso2": "KG",
      "iso3": "KGZ",
      "lat": 41,
      "long": 75,
      "flag": "https://disease.sh/assets/img/flags/kg.png"
    },
    "cases": 54588,
    "todayCases": 582,
    "deaths": 1126,
    "todayDeaths": 4,
    "recovered": 47050,
    "todayRecovered": 324,
    "active": 6412,
    "critical": 24,
    "casesPerOneMillion": 8325,
    "deathsPerOneMillion": 172,
    "tests": 392223,
    "testsPerOneMillion": 59813,
    "population": 6557439,
    "continent": "Asia",
    "oneCasePerPeople": 120,
    "oneDeathPerPeople": 5824,
    "oneTestPerPeople": 17,
    "activePerOneMillion": 977.82,
    "recoveredPerOneMillion": 7175.06,
    "criticalPerOneMillion": 3.66
  },
  {
    "updated": 1603500524261,
    "country": "Lao People's Democratic Republic",
    "countryInfo": {
      "_id": 418,
      "iso2": "LA",
      "iso3": "LAO",
      "lat": 18,
      "long": 105,
      "flag": "https://disease.sh/assets/img/flags/la.png"
    },
    "cases": 24,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 22,
    "todayRecovered": null,
    "active": 2,
    "critical": null,
    "casesPerOneMillion": 3,
    "deathsPerOneMillion": null,
    "tests": 62474,
    "testsPerOneMillion": 8548,
    "population": 7308259,
    "continent": "Asia",
    "oneCasePerPeople": 304511,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 117,
    "activePerOneMillion": 0.27,
    "recoveredPerOneMillion": 3.01,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524061,
    "country": "Latvia",
    "countryInfo": {
      "_id": 428,
      "iso2": "LV",
      "iso3": "LVA",
      "lat": 57,
      "long": 25,
      "flag": "https://disease.sh/assets/img/flags/lv.png"
    },
    "cases": 4208,
    "todayCases": 250,
    "deaths": 50,
    "todayDeaths": 1,
    "recovered": 1357,
    "todayRecovered": null,
    "active": 2801,
    "critical": 10,
    "casesPerOneMillion": 2239,
    "deathsPerOneMillion": 27,
    "tests": 413905,
    "testsPerOneMillion": 220218,
    "population": 1879522,
    "continent": "Europe",
    "oneCasePerPeople": 447,
    "oneDeathPerPeople": 37590,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 1490.27,
    "recoveredPerOneMillion": 721.99,
    "criticalPerOneMillion": 5.32
  },
  {
    "updated": 1603500523754,
    "country": "Lebanon",
    "countryInfo": {
      "_id": 422,
      "iso2": "LB",
      "iso3": "LBN",
      "lat": 33.8333,
      "long": 35.8333,
      "flag": "https://disease.sh/assets/img/flags/lb.png"
    },
    "cases": 68479,
    "todayCases": 1452,
    "deaths": 559,
    "todayDeaths": 7,
    "recovered": 32412,
    "todayRecovered": 1003,
    "active": 35508,
    "critical": 242,
    "casesPerOneMillion": 10047,
    "deathsPerOneMillion": 82,
    "tests": 1126289,
    "testsPerOneMillion": 165248,
    "population": 6815738,
    "continent": "Asia",
    "oneCasePerPeople": 100,
    "oneDeathPerPeople": 12193,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 5209.71,
    "recoveredPerOneMillion": 4755.46,
    "criticalPerOneMillion": 35.51
  },
  {
    "updated": 1603500524153,
    "country": "Lesotho",
    "countryInfo": {
      "_id": 426,
      "iso2": "LS",
      "iso3": "LSO",
      "lat": -29.5,
      "long": 28.5,
      "flag": "https://disease.sh/assets/img/flags/ls.png"
    },
    "cases": 1934,
    "todayCases": 11,
    "deaths": 43,
    "todayDeaths": null,
    "recovered": 961,
    "todayRecovered": null,
    "active": 930,
    "critical": null,
    "casesPerOneMillion": 901,
    "deathsPerOneMillion": 20,
    "tests": 22200,
    "testsPerOneMillion": 10337,
    "population": 2147557,
    "continent": "Africa",
    "oneCasePerPeople": 1110,
    "oneDeathPerPeople": 49943,
    "oneTestPerPeople": 97,
    "activePerOneMillion": 433.05,
    "recoveredPerOneMillion": 447.49,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524156,
    "country": "Liberia",
    "countryInfo": {
      "_id": 430,
      "iso2": "LR",
      "iso3": "LBR",
      "lat": 6.5,
      "long": -9.5,
      "flag": "https://disease.sh/assets/img/flags/lr.png"
    },
    "cases": 1393,
    "todayCases": 8,
    "deaths": 82,
    "todayDeaths": null,
    "recovered": 1278,
    "todayRecovered": null,
    "active": 33,
    "critical": 2,
    "casesPerOneMillion": 273,
    "deathsPerOneMillion": 16,
    "tests": 30332,
    "testsPerOneMillion": 5954,
    "population": 5094020,
    "continent": "Africa",
    "oneCasePerPeople": 3657,
    "oneDeathPerPeople": 62122,
    "oneTestPerPeople": 168,
    "activePerOneMillion": 6.48,
    "recoveredPerOneMillion": 250.88,
    "criticalPerOneMillion": 0.39
  },
  {
    "updated": 1603500523765,
    "country": "Libyan Arab Jamahiriya",
    "countryInfo": {
      "_id": 434,
      "iso2": "LY",
      "iso3": "LBY",
      "lat": 25,
      "long": 17,
      "flag": "https://disease.sh/assets/img/flags/ly.png"
    },
    "cases": 53384,
    "todayCases": 764,
    "deaths": 774,
    "todayDeaths": 6,
    "recovered": 29619,
    "todayRecovered": 562,
    "active": 22991,
    "critical": null,
    "casesPerOneMillion": 7737,
    "deathsPerOneMillion": 112,
    "tests": 289850,
    "testsPerOneMillion": 42006,
    "population": 6900269,
    "continent": "Africa",
    "oneCasePerPeople": 129,
    "oneDeathPerPeople": 8915,
    "oneTestPerPeople": 24,
    "activePerOneMillion": 3331.9,
    "recoveredPerOneMillion": 4292.44,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524242,
    "country": "Liechtenstein",
    "countryInfo": {
      "_id": 438,
      "iso2": "LI",
      "iso3": "LIE",
      "lat": 47.1667,
      "long": 9.5333,
      "flag": "https://disease.sh/assets/img/flags/li.png"
    },
    "cases": 324,
    "todayCases": 42,
    "deaths": 1,
    "todayDeaths": null,
    "recovered": 170,
    "todayRecovered": 12,
    "active": 153,
    "critical": 8,
    "casesPerOneMillion": 8490,
    "deathsPerOneMillion": 26,
    "tests": 2200,
    "testsPerOneMillion": 57649,
    "population": 38162,
    "continent": "Europe",
    "oneCasePerPeople": 118,
    "oneDeathPerPeople": 38162,
    "oneTestPerPeople": 17,
    "activePerOneMillion": 4009.22,
    "recoveredPerOneMillion": 4454.69,
    "criticalPerOneMillion": 209.63
  },
  {
    "updated": 1603500523957,
    "country": "Lithuania",
    "countryInfo": {
      "_id": 440,
      "iso2": "LT",
      "iso3": "LTU",
      "lat": 56,
      "long": 24,
      "flag": "https://disease.sh/assets/img/flags/lt.png"
    },
    "cases": 9104,
    "todayCases": 442,
    "deaths": 126,
    "todayDeaths": 1,
    "recovered": 3978,
    "todayRecovered": 205,
    "active": 5000,
    "critical": 26,
    "casesPerOneMillion": 3359,
    "deathsPerOneMillion": 46,
    "tests": 935997,
    "testsPerOneMillion": 345375,
    "population": 2710088,
    "continent": "Europe",
    "oneCasePerPeople": 298,
    "oneDeathPerPeople": 21509,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 1844.96,
    "recoveredPerOneMillion": 1467.85,
    "criticalPerOneMillion": 9.59
  },
  {
    "updated": 1603500523943,
    "country": "Luxembourg",
    "countryInfo": {
      "_id": 442,
      "iso2": "LU",
      "iso3": "LUX",
      "lat": 49.75,
      "long": 6.1667,
      "flag": "https://disease.sh/assets/img/flags/lu.png"
    },
    "cases": 12851,
    "todayCases": 518,
    "deaths": 141,
    "todayDeaths": 1,
    "recovered": 9085,
    "todayRecovered": 611,
    "active": 3625,
    "critical": 8,
    "casesPerOneMillion": 20427,
    "deathsPerOneMillion": 224,
    "tests": 983307,
    "testsPerOneMillion": 1562978,
    "population": 629124,
    "continent": "Europe",
    "oneCasePerPeople": 49,
    "oneDeathPerPeople": 4462,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 5761.98,
    "recoveredPerOneMillion": 14440.71,
    "criticalPerOneMillion": 12.72
  },
  {
    "updated": 1603500524267,
    "country": "MS Zaandam",
    "countryInfo": {
      "_id": null,
      "iso2": null,
      "iso3": null,
      "lat": 0,
      "long": 0,
      "flag": "https://disease.sh/assets/img/flags/unknown.png"
    },
    "cases": 9,
    "todayCases": null,
    "deaths": 2,
    "todayDeaths": null,
    "recovered": null,
    "todayRecovered": null,
    "active": 7,
    "critical": null,
    "casesPerOneMillion": null,
    "deathsPerOneMillion": null,
    "tests": null,
    "testsPerOneMillion": null,
    "population": null,
    "continent": "",
    "oneCasePerPeople": null,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": null,
    "activePerOneMillion": null,
    "recoveredPerOneMillion": null,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524254,
    "country": "Macao",
    "countryInfo": {
      "_id": 446,
      "iso2": "MO",
      "iso3": "MAC",
      "lat": 22.1667,
      "long": 113.55,
      "flag": "https://disease.sh/assets/img/flags/mo.png"
    },
    "cases": 46,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 46,
    "todayRecovered": null,
    "active": 0,
    "critical": null,
    "casesPerOneMillion": 71,
    "deathsPerOneMillion": null,
    "tests": 4238,
    "testsPerOneMillion": 6499,
    "population": 652080,
    "continent": "Asia",
    "oneCasePerPeople": 14176,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 154,
    "activePerOneMillion": 0,
    "recoveredPerOneMillion": 70.54,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523847,
    "country": "Macedonia",
    "countryInfo": {
      "_id": 807,
      "iso2": "MK",
      "iso3": "MKD",
      "lat": 41.8333,
      "long": 22,
      "flag": "https://disease.sh/assets/img/flags/mk.png"
    },
    "cases": 25991,
    "todayCases": 518,
    "deaths": 883,
    "todayDeaths": 9,
    "recovered": 18247,
    "todayRecovered": 200,
    "active": 6861,
    "critical": 25,
    "casesPerOneMillion": 12476,
    "deathsPerOneMillion": 424,
    "tests": 231613,
    "testsPerOneMillion": 111174,
    "population": 2083347,
    "continent": "Europe",
    "oneCasePerPeople": 80,
    "oneDeathPerPeople": 2359,
    "oneTestPerPeople": 9,
    "activePerOneMillion": 3293.26,
    "recoveredPerOneMillion": 8758.5,
    "criticalPerOneMillion": 12
  },
  {
    "updated": 1603500523858,
    "country": "Madagascar",
    "countryInfo": {
      "_id": 450,
      "iso2": "MG",
      "iso3": "MDG",
      "lat": -20,
      "long": 47,
      "flag": "https://disease.sh/assets/img/flags/mg.png"
    },
    "cases": 16810,
    "todayCases": null,
    "deaths": 238,
    "todayDeaths": null,
    "recovered": 16215,
    "todayRecovered": null,
    "active": 357,
    "critical": 16,
    "casesPerOneMillion": 602,
    "deathsPerOneMillion": 9,
    "tests": 85407,
    "testsPerOneMillion": 3060,
    "population": 27907915,
    "continent": "Africa",
    "oneCasePerPeople": 1660,
    "oneDeathPerPeople": 117260,
    "oneTestPerPeople": 327,
    "activePerOneMillion": 12.79,
    "recoveredPerOneMillion": 581.02,
    "criticalPerOneMillion": 0.57
  },
  {
    "updated": 1603500524046,
    "country": "Malawi",
    "countryInfo": {
      "_id": 454,
      "iso2": "MW",
      "iso3": "MWI",
      "lat": -13.5,
      "long": 34,
      "flag": "https://disease.sh/assets/img/flags/mw.png"
    },
    "cases": 5885,
    "todayCases": 11,
    "deaths": 183,
    "todayDeaths": null,
    "recovered": 5287,
    "todayRecovered": 523,
    "active": 415,
    "critical": 4,
    "casesPerOneMillion": 305,
    "deathsPerOneMillion": 9,
    "tests": 59402,
    "testsPerOneMillion": 3081,
    "population": 19280534,
    "continent": "Africa",
    "oneCasePerPeople": 3276,
    "oneDeathPerPeople": 105358,
    "oneTestPerPeople": 325,
    "activePerOneMillion": 21.52,
    "recoveredPerOneMillion": 274.21,
    "criticalPerOneMillion": 0.21
  },
  {
    "updated": 1603500523850,
    "country": "Malaysia",
    "countryInfo": {
      "_id": 458,
      "iso2": "MY",
      "iso3": "MYS",
      "lat": 2.5,
      "long": 112.5,
      "flag": "https://disease.sh/assets/img/flags/my.png"
    },
    "cases": 24514,
    "todayCases": 710,
    "deaths": 214,
    "todayDeaths": 10,
    "recovered": 15884,
    "todayRecovered": 467,
    "active": 8416,
    "critical": 90,
    "casesPerOneMillion": 754,
    "deathsPerOneMillion": 7,
    "tests": 1973780,
    "testsPerOneMillion": 60742,
    "population": 32494745,
    "continent": "Asia",
    "oneCasePerPeople": 1326,
    "oneDeathPerPeople": 151845,
    "oneTestPerPeople": 16,
    "activePerOneMillion": 259,
    "recoveredPerOneMillion": 488.82,
    "criticalPerOneMillion": 2.77
  },
  {
    "updated": 1603500523947,
    "country": "Maldives",
    "countryInfo": {
      "_id": 462,
      "iso2": "MV",
      "iso3": "MDV",
      "lat": 3.25,
      "long": 73,
      "flag": "https://disease.sh/assets/img/flags/mv.png"
    },
    "cases": 11391,
    "todayCases": 33,
    "deaths": 37,
    "todayDeaths": null,
    "recovered": 10428,
    "todayRecovered": 45,
    "active": 926,
    "critical": 12,
    "casesPerOneMillion": 20959,
    "deathsPerOneMillion": 68,
    "tests": 150743,
    "testsPerOneMillion": 277366,
    "population": 543480,
    "continent": "Asia",
    "oneCasePerPeople": 48,
    "oneDeathPerPeople": 14689,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 1703.83,
    "recoveredPerOneMillion": 19187.46,
    "criticalPerOneMillion": 22.08
  },
  {
    "updated": 1603500524142,
    "country": "Mali",
    "countryInfo": {
      "_id": 466,
      "iso2": "ML",
      "iso3": "MLI",
      "lat": 17,
      "long": -4,
      "flag": "https://disease.sh/assets/img/flags/ml.png"
    },
    "cases": 3444,
    "todayCases": 4,
    "deaths": 132,
    "todayDeaths": null,
    "recovered": 2620,
    "todayRecovered": 12,
    "active": 692,
    "critical": null,
    "casesPerOneMillion": 169,
    "deathsPerOneMillion": 6,
    "tests": 69342,
    "testsPerOneMillion": 3395,
    "population": 20427714,
    "continent": "Africa",
    "oneCasePerPeople": 5931,
    "oneDeathPerPeople": 154755,
    "oneTestPerPeople": 295,
    "activePerOneMillion": 33.88,
    "recoveredPerOneMillion": 128.26,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524053,
    "country": "Malta",
    "countryInfo": {
      "_id": 470,
      "iso2": "MT",
      "iso3": "MLT",
      "lat": 35.8333,
      "long": 14.5833,
      "flag": "https://disease.sh/assets/img/flags/mt.png"
    },
    "cases": 5258,
    "todayCases": 121,
    "deaths": 49,
    "todayDeaths": null,
    "recovered": 3439,
    "todayRecovered": 55,
    "active": 1770,
    "critical": 6,
    "casesPerOneMillion": 11898,
    "deathsPerOneMillion": 111,
    "tests": 311475,
    "testsPerOneMillion": 704833,
    "population": 441913,
    "continent": "Europe",
    "oneCasePerPeople": 84,
    "oneDeathPerPeople": 9019,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 4005.31,
    "recoveredPerOneMillion": 7782.07,
    "criticalPerOneMillion": 13.58
  },
  {
    "updated": 1603500524150,
    "country": "Martinique",
    "countryInfo": {
      "_id": 474,
      "iso2": "MQ",
      "iso3": "MTQ",
      "lat": 14.6667,
      "long": -61,
      "flag": "https://disease.sh/assets/img/flags/mq.png"
    },
    "cases": 2257,
    "todayCases": null,
    "deaths": 24,
    "todayDeaths": null,
    "recovered": 98,
    "todayRecovered": null,
    "active": 2135,
    "critical": 19,
    "casesPerOneMillion": 6016,
    "deathsPerOneMillion": 64,
    "tests": 42504,
    "testsPerOneMillion": 113292,
    "population": 375173,
    "continent": "North America",
    "oneCasePerPeople": 166,
    "oneDeathPerPeople": 15632,
    "oneTestPerPeople": 9,
    "activePerOneMillion": 5690.71,
    "recoveredPerOneMillion": 261.21,
    "criticalPerOneMillion": 50.64
  },
  {
    "updated": 1603500524040,
    "country": "Mauritania",
    "countryInfo": {
      "_id": 478,
      "iso2": "MR",
      "iso3": "MRT",
      "lat": 20,
      "long": -12,
      "flag": "https://disease.sh/assets/img/flags/mr.png"
    },
    "cases": 7662,
    "todayCases": 12,
    "deaths": 163,
    "todayDeaths": null,
    "recovered": 7374,
    "todayRecovered": 5,
    "active": 125,
    "critical": 3,
    "casesPerOneMillion": 1635,
    "deathsPerOneMillion": 35,
    "tests": 85629,
    "testsPerOneMillion": 18270,
    "population": 4686863,
    "continent": "Africa",
    "oneCasePerPeople": 612,
    "oneDeathPerPeople": 28754,
    "oneTestPerPeople": 55,
    "activePerOneMillion": 26.67,
    "recoveredPerOneMillion": 1573.33,
    "criticalPerOneMillion": 0.64
  },
  {
    "updated": 1603500524239,
    "country": "Mauritius",
    "countryInfo": {
      "_id": 480,
      "iso2": "MU",
      "iso3": "MUS",
      "lat": -20.2833,
      "long": 57.55,
      "flag": "https://disease.sh/assets/img/flags/mu.png"
    },
    "cases": 435,
    "todayCases": 10,
    "deaths": 10,
    "todayDeaths": null,
    "recovered": 386,
    "todayRecovered": null,
    "active": 39,
    "critical": null,
    "casesPerOneMillion": 342,
    "deathsPerOneMillion": 8,
    "tests": 260973,
    "testsPerOneMillion": 205098,
    "population": 1272433,
    "continent": "Africa",
    "oneCasePerPeople": 2925,
    "oneDeathPerPeople": 127243,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 30.65,
    "recoveredPerOneMillion": 303.36,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524063,
    "country": "Mayotte",
    "countryInfo": {
      "_id": 175,
      "iso2": "YT",
      "iso3": "MYT",
      "lat": -12.8333,
      "long": 45.1667,
      "flag": "https://disease.sh/assets/img/flags/yt.png"
    },
    "cases": 4203,
    "todayCases": null,
    "deaths": 44,
    "todayDeaths": null,
    "recovered": 2964,
    "todayRecovered": null,
    "active": 1195,
    "critical": 3,
    "casesPerOneMillion": 15293,
    "deathsPerOneMillion": 160,
    "tests": 13000,
    "testsPerOneMillion": 47303,
    "population": 274825,
    "continent": "Africa",
    "oneCasePerPeople": 65,
    "oneDeathPerPeople": 6246,
    "oneTestPerPeople": 21,
    "activePerOneMillion": 4348.22,
    "recoveredPerOneMillion": 10785.05,
    "criticalPerOneMillion": 10.92
  },
  {
    "updated": 1603500523561,
    "country": "Mexico",
    "countryInfo": {
      "_id": 484,
      "iso2": "MX",
      "iso3": "MEX",
      "lat": 23,
      "long": -102,
      "flag": "https://disease.sh/assets/img/flags/mx.png"
    },
    "cases": 874171,
    "todayCases": 6612,
    "deaths": 87894,
    "todayDeaths": 479,
    "recovered": 636391,
    "todayRecovered": 4354,
    "active": 149886,
    "critical": 2617,
    "casesPerOneMillion": 6758,
    "deathsPerOneMillion": 679,
    "tests": 2249619,
    "testsPerOneMillion": 17391,
    "population": 129354669,
    "continent": "North America",
    "oneCasePerPeople": 148,
    "oneDeathPerPeople": 1472,
    "oneTestPerPeople": 58,
    "activePerOneMillion": 1158.72,
    "recoveredPerOneMillion": 4919.74,
    "criticalPerOneMillion": 20.23
  },
  {
    "updated": 1603500523753,
    "country": "Moldova",
    "countryInfo": {
      "_id": 498,
      "iso2": "MD",
      "iso3": "MDA",
      "lat": 47,
      "long": 29,
      "flag": "https://disease.sh/assets/img/flags/md.png"
    },
    "cases": 70256,
    "todayCases": 688,
    "deaths": 1654,
    "todayDeaths": 13,
    "recovered": 51102,
    "todayRecovered": 680,
    "active": 17500,
    "critical": 813,
    "casesPerOneMillion": 17429,
    "deathsPerOneMillion": 410,
    "tests": 341838,
    "testsPerOneMillion": 84802,
    "population": 4030993,
    "continent": "Europe",
    "oneCasePerPeople": 57,
    "oneDeathPerPeople": 2437,
    "oneTestPerPeople": 12,
    "activePerOneMillion": 4341.36,
    "recoveredPerOneMillion": 12677.27,
    "criticalPerOneMillion": 201.69
  },
  {
    "updated": 1603500524243,
    "country": "Monaco",
    "countryInfo": {
      "_id": 492,
      "iso2": "MC",
      "iso3": "MCO",
      "lat": 43.7333,
      "long": 7.4,
      "flag": "https://disease.sh/assets/img/flags/mc.png"
    },
    "cases": 295,
    "todayCases": 14,
    "deaths": 2,
    "todayDeaths": null,
    "recovered": 241,
    "todayRecovered": 8,
    "active": 52,
    "critical": 5,
    "casesPerOneMillion": 7501,
    "deathsPerOneMillion": 51,
    "tests": 51953,
    "testsPerOneMillion": 1320985,
    "population": 39329,
    "continent": "Europe",
    "oneCasePerPeople": 133,
    "oneDeathPerPeople": 19665,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 1322.18,
    "recoveredPerOneMillion": 6127.79,
    "criticalPerOneMillion": 127.13
  },
  {
    "updated": 1603500524241,
    "country": "Mongolia",
    "countryInfo": {
      "_id": 496,
      "iso2": "MN",
      "iso3": "MNG",
      "lat": 46,
      "long": 105,
      "flag": "https://disease.sh/assets/img/flags/mn.png"
    },
    "cases": 328,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 312,
    "todayRecovered": null,
    "active": 16,
    "critical": 1,
    "casesPerOneMillion": 100,
    "deathsPerOneMillion": null,
    "tests": 84564,
    "testsPerOneMillion": 25667,
    "population": 3294604,
    "continent": "Asia",
    "oneCasePerPeople": 10045,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 39,
    "activePerOneMillion": 4.86,
    "recoveredPerOneMillion": 94.7,
    "criticalPerOneMillion": 0.3
  },
  {
    "updated": 1603500523936,
    "country": "Montenegro",
    "countryInfo": {
      "_id": 499,
      "iso2": "ME",
      "iso3": "MNE",
      "lat": 42,
      "long": 19,
      "flag": "https://disease.sh/assets/img/flags/me.png"
    },
    "cases": 16436,
    "todayCases": 177,
    "deaths": 255,
    "todayDeaths": 2,
    "recovered": 12378,
    "todayRecovered": 285,
    "active": 3803,
    "critical": 26,
    "casesPerOneMillion": 26168,
    "deathsPerOneMillion": 406,
    "tests": 84074,
    "testsPerOneMillion": 133856,
    "population": 628091,
    "continent": "Europe",
    "oneCasePerPeople": 38,
    "oneDeathPerPeople": 2463,
    "oneTestPerPeople": 7,
    "activePerOneMillion": 6054.86,
    "recoveredPerOneMillion": 19707.34,
    "criticalPerOneMillion": 41.4
  },
  {
    "updated": 1603500524264,
    "country": "Montserrat",
    "countryInfo": {
      "_id": 500,
      "iso2": "MS",
      "iso3": "MSR",
      "lat": 16.75,
      "long": -62.2,
      "flag": "https://disease.sh/assets/img/flags/ms.png"
    },
    "cases": 13,
    "todayCases": null,
    "deaths": 1,
    "todayDeaths": null,
    "recovered": 12,
    "todayRecovered": null,
    "active": 0,
    "critical": null,
    "casesPerOneMillion": 2604,
    "deathsPerOneMillion": 200,
    "tests": 483,
    "testsPerOneMillion": 96735,
    "population": 4993,
    "continent": "North America",
    "oneCasePerPeople": 384,
    "oneDeathPerPeople": 4993,
    "oneTestPerPeople": 10,
    "activePerOneMillion": 0,
    "recoveredPerOneMillion": 2403.36,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523658,
    "country": "Morocco",
    "countryInfo": {
      "_id": 504,
      "iso2": "MA",
      "iso3": "MAR",
      "lat": 32,
      "long": -5,
      "flag": "https://disease.sh/assets/img/flags/ma.png"
    },
    "cases": 190416,
    "todayCases": 3685,
    "deaths": 3205,
    "todayDeaths": 73,
    "recovered": 157175,
    "todayRecovered": 2694,
    "active": 30036,
    "critical": 699,
    "casesPerOneMillion": 5140,
    "deathsPerOneMillion": 87,
    "tests": 3153471,
    "testsPerOneMillion": 85122,
    "population": 37046570,
    "continent": "Africa",
    "oneCasePerPeople": 195,
    "oneDeathPerPeople": 11559,
    "oneTestPerPeople": 12,
    "activePerOneMillion": 810.76,
    "recoveredPerOneMillion": 4242.63,
    "criticalPerOneMillion": 18.87
  },
  {
    "updated": 1603500523945,
    "country": "Mozambique",
    "countryInfo": {
      "_id": 508,
      "iso2": "MZ",
      "iso3": "MOZ",
      "lat": -18.25,
      "long": 35,
      "flag": "https://disease.sh/assets/img/flags/mz.png"
    },
    "cases": 11748,
    "todayCases": 189,
    "deaths": 82,
    "todayDeaths": 1,
    "recovered": 9234,
    "todayRecovered": 8,
    "active": 2432,
    "critical": null,
    "casesPerOneMillion": 373,
    "deathsPerOneMillion": 3,
    "tests": 177287,
    "testsPerOneMillion": 5624,
    "population": 31521303,
    "continent": "Africa",
    "oneCasePerPeople": 2683,
    "oneDeathPerPeople": 384406,
    "oneTestPerPeople": 178,
    "activePerOneMillion": 77.15,
    "recoveredPerOneMillion": 292.94,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523773,
    "country": "Myanmar",
    "countryInfo": {
      "_id": 104,
      "iso2": "MM",
      "iso3": "MMR",
      "lat": 22,
      "long": 98,
      "flag": "https://disease.sh/assets/img/flags/mm.png"
    },
    "cases": 42365,
    "todayCases": 1357,
    "deaths": 1038,
    "todayDeaths": 33,
    "recovered": 22445,
    "todayRecovered": 1301,
    "active": 18882,
    "critical": null,
    "casesPerOneMillion": 777,
    "deathsPerOneMillion": 19,
    "tests": 579921,
    "testsPerOneMillion": 10636,
    "population": 54523996,
    "continent": "Asia",
    "oneCasePerPeople": 1287,
    "oneDeathPerPeople": 52528,
    "oneTestPerPeople": 94,
    "activePerOneMillion": 346.31,
    "recoveredPerOneMillion": 411.65,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523944,
    "country": "Namibia",
    "countryInfo": {
      "_id": 516,
      "iso2": "NA",
      "iso3": "NAM",
      "lat": -22,
      "long": 17,
      "flag": "https://disease.sh/assets/img/flags/na.png"
    },
    "cases": 12501,
    "todayCases": 41,
    "deaths": 133,
    "todayDeaths": null,
    "recovered": 10748,
    "todayRecovered": 139,
    "active": 1620,
    "critical": 3,
    "casesPerOneMillion": 4893,
    "deathsPerOneMillion": 52,
    "tests": 120558,
    "testsPerOneMillion": 47184,
    "population": 2555084,
    "continent": "Africa",
    "oneCasePerPeople": 204,
    "oneDeathPerPeople": 19211,
    "oneTestPerPeople": 21,
    "activePerOneMillion": 634.03,
    "recoveredPerOneMillion": 4206.52,
    "criticalPerOneMillion": 1.17
  },
  {
    "updated": 1603500523660,
    "country": "Nepal",
    "countryInfo": {
      "_id": 524,
      "iso2": "NP",
      "iso3": "NPL",
      "lat": 28,
      "long": 84,
      "flag": "https://disease.sh/assets/img/flags/np.png"
    },
    "cases": 153008,
    "todayCases": 4499,
    "deaths": 829,
    "todayDeaths": 17,
    "recovered": 105488,
    "todayRecovered": 2668,
    "active": 46691,
    "critical": null,
    "casesPerOneMillion": 5222,
    "deathsPerOneMillion": 28,
    "tests": 1367016,
    "testsPerOneMillion": 46659,
    "population": 29298314,
    "continent": "Asia",
    "oneCasePerPeople": 191,
    "oneDeathPerPeople": 35342,
    "oneTestPerPeople": 21,
    "activePerOneMillion": 1593.64,
    "recoveredPerOneMillion": 3600.48,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523651,
    "country": "Netherlands",
    "countryInfo": {
      "_id": 528,
      "iso2": "NL",
      "iso3": "NLD",
      "lat": 52.5,
      "long": 5.75,
      "flag": "https://disease.sh/assets/img/flags/nl.png"
    },
    "cases": 272401,
    "todayCases": 9996,
    "deaths": 6964,
    "todayDeaths": 45,
    "recovered": null,
    "todayRecovered": null,
    "active": 265437,
    "critical": 488,
    "casesPerOneMillion": 15886,
    "deathsPerOneMillion": 406,
    "tests": 2872319,
    "testsPerOneMillion": 167513,
    "population": 17146812,
    "continent": "Europe",
    "oneCasePerPeople": 63,
    "oneDeathPerPeople": 2462,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 15480.25,
    "recoveredPerOneMillion": null,
    "criticalPerOneMillion": 28.46
  },
  {
    "updated": 1603500524260,
    "country": "New Caledonia",
    "countryInfo": {
      "_id": 540,
      "iso2": "NC",
      "iso3": "NCL",
      "lat": -21.5,
      "long": 165.5,
      "flag": "https://disease.sh/assets/img/flags/nc.png"
    },
    "cases": 27,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 27,
    "todayRecovered": null,
    "active": 0,
    "critical": null,
    "casesPerOneMillion": 94,
    "deathsPerOneMillion": null,
    "tests": 15180,
    "testsPerOneMillion": 53011,
    "population": 286354,
    "continent": "Australia/Oceania",
    "oneCasePerPeople": 10606,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 19,
    "activePerOneMillion": 0,
    "recoveredPerOneMillion": 94.29,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524154,
    "country": "New Zealand",
    "countryInfo": {
      "_id": 554,
      "iso2": "NZ",
      "iso3": "NZL",
      "lat": -41,
      "long": 174,
      "flag": "https://disease.sh/assets/img/flags/nz.png"
    },
    "cases": 1923,
    "todayCases": 9,
    "deaths": 25,
    "todayDeaths": null,
    "recovered": 1832,
    "todayRecovered": 1,
    "active": 66,
    "critical": null,
    "casesPerOneMillion": 384,
    "deathsPerOneMillion": 5,
    "tests": 1054047,
    "testsPerOneMillion": 210721,
    "population": 5002100,
    "continent": "Australia/Oceania",
    "oneCasePerPeople": 2601,
    "oneDeathPerPeople": 200084,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 13.19,
    "recoveredPerOneMillion": 366.25,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524051,
    "country": "Nicaragua",
    "countryInfo": {
      "_id": 558,
      "iso2": "NI",
      "iso3": "NIC",
      "lat": 13,
      "long": -85,
      "flag": "https://disease.sh/assets/img/flags/ni.png"
    },
    "cases": 5434,
    "todayCases": null,
    "deaths": 155,
    "todayDeaths": null,
    "recovered": 4225,
    "todayRecovered": null,
    "active": 1054,
    "critical": null,
    "casesPerOneMillion": 817,
    "deathsPerOneMillion": 23,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 6649055,
    "continent": "North America",
    "oneCasePerPeople": 1224,
    "oneDeathPerPeople": 42897,
    "oneTestPerPeople": null,
    "activePerOneMillion": 158.52,
    "recoveredPerOneMillion": 635.43,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524157,
    "country": "Niger",
    "countryInfo": {
      "_id": 562,
      "iso2": "NE",
      "iso3": "NER",
      "lat": 16,
      "long": 8,
      "flag": "https://disease.sh/assets/img/flags/ne.png"
    },
    "cases": 1215,
    "todayCases": null,
    "deaths": 69,
    "todayDeaths": null,
    "recovered": 1128,
    "todayRecovered": null,
    "active": 18,
    "critical": 9,
    "casesPerOneMillion": 50,
    "deathsPerOneMillion": 3,
    "tests": 34823,
    "testsPerOneMillion": 1423,
    "population": 24469314,
    "continent": "Africa",
    "oneCasePerPeople": 20139,
    "oneDeathPerPeople": 354628,
    "oneTestPerPeople": 703,
    "activePerOneMillion": 0.74,
    "recoveredPerOneMillion": 46.1,
    "criticalPerOneMillion": 0.37
  },
  {
    "updated": 1603500523756,
    "country": "Nigeria",
    "countryInfo": {
      "_id": 566,
      "iso2": "NG",
      "iso3": "NGA",
      "lat": 10,
      "long": 8,
      "flag": "https://disease.sh/assets/img/flags/ng.png"
    },
    "cases": 61882,
    "todayCases": 77,
    "deaths": 1129,
    "todayDeaths": 2,
    "recovered": 57190,
    "todayRecovered": 205,
    "active": 3563,
    "critical": 7,
    "casesPerOneMillion": 298,
    "deathsPerOneMillion": 5,
    "tests": 602239,
    "testsPerOneMillion": 2900,
    "population": 207698436,
    "continent": "Africa",
    "oneCasePerPeople": 3356,
    "oneDeathPerPeople": 183967,
    "oneTestPerPeople": 345,
    "activePerOneMillion": 17.15,
    "recoveredPerOneMillion": 275.35,
    "criticalPerOneMillion": 0.03
  },
  {
    "updated": 1603500523856,
    "country": "Norway",
    "countryInfo": {
      "_id": 578,
      "iso2": "NO",
      "iso3": "NOR",
      "lat": 62,
      "long": 10,
      "flag": "https://disease.sh/assets/img/flags/no.png"
    },
    "cases": 17532,
    "todayCases": 300,
    "deaths": 279,
    "todayDeaths": null,
    "recovered": 11863,
    "todayRecovered": null,
    "active": 5390,
    "critical": 6,
    "casesPerOneMillion": 3226,
    "deathsPerOneMillion": 51,
    "tests": 1528498,
    "testsPerOneMillion": 281259,
    "population": 5434493,
    "continent": "Europe",
    "oneCasePerPeople": 310,
    "oneDeathPerPeople": 19478,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 991.81,
    "recoveredPerOneMillion": 2182.91,
    "criticalPerOneMillion": 1.1
  },
  {
    "updated": 1603500523671,
    "country": "Oman",
    "countryInfo": {
      "_id": 512,
      "iso2": "OM",
      "iso3": "OMN",
      "lat": 21,
      "long": 57,
      "flag": "https://disease.sh/assets/img/flags/om.png"
    },
    "cases": 111837,
    "todayCases": null,
    "deaths": 1147,
    "todayDeaths": null,
    "recovered": 97949,
    "todayRecovered": null,
    "active": 12741,
    "critical": 202,
    "casesPerOneMillion": 21732,
    "deathsPerOneMillion": 223,
    "tests": 376700,
    "testsPerOneMillion": 73199,
    "population": 5146213,
    "continent": "Asia",
    "oneCasePerPeople": 46,
    "oneDeathPerPeople": 4487,
    "oneTestPerPeople": 14,
    "activePerOneMillion": 2475.8,
    "recoveredPerOneMillion": 19033.22,
    "criticalPerOneMillion": 39.25
  },
  {
    "updated": 1603500523649,
    "country": "Pakistan",
    "countryInfo": {
      "_id": 586,
      "iso2": "PK",
      "iso3": "PAK",
      "lat": 30,
      "long": 70,
      "flag": "https://disease.sh/assets/img/flags/pk.png"
    },
    "cases": 326216,
    "todayCases": 736,
    "deaths": 6715,
    "todayDeaths": 13,
    "recovered": 309646,
    "todayRecovered": 510,
    "active": 9855,
    "critical": 586,
    "casesPerOneMillion": 1468,
    "deathsPerOneMillion": 30,
    "tests": 4204320,
    "testsPerOneMillion": 18920,
    "population": 222211438,
    "continent": "Asia",
    "oneCasePerPeople": 681,
    "oneDeathPerPeople": 33092,
    "oneTestPerPeople": 53,
    "activePerOneMillion": 44.35,
    "recoveredPerOneMillion": 1393.47,
    "criticalPerOneMillion": 2.64
  },
  {
    "updated": 1603500523766,
    "country": "Palestine",
    "countryInfo": {
      "_id": 275,
      "iso2": "PS",
      "iso3": "PSE",
      "lat": 32,
      "long": 35.25,
      "flag": "https://disease.sh/assets/img/flags/ps.png"
    },
    "cases": 49579,
    "todayCases": 445,
    "deaths": 439,
    "todayDeaths": 4,
    "recovered": 42850,
    "todayRecovered": 306,
    "active": 6290,
    "critical": null,
    "casesPerOneMillion": 9650,
    "deathsPerOneMillion": 85,
    "tests": 489417,
    "testsPerOneMillion": 95260,
    "population": 5137680,
    "continent": "Asia",
    "oneCasePerPeople": 104,
    "oneDeathPerPeople": 11703,
    "oneTestPerPeople": 10,
    "activePerOneMillion": 1224.29,
    "recoveredPerOneMillion": 8340.34,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523663,
    "country": "Panama",
    "countryInfo": {
      "_id": 591,
      "iso2": "PA",
      "iso3": "PAN",
      "lat": 9,
      "long": -80,
      "flag": "https://disease.sh/assets/img/flags/pa.png"
    },
    "cases": 127866,
    "todayCases": 639,
    "deaths": 2622,
    "todayDeaths": 10,
    "recovered": 103985,
    "todayRecovered": 587,
    "active": 21259,
    "critical": 122,
    "casesPerOneMillion": 29491,
    "deathsPerOneMillion": 605,
    "tests": 614675,
    "testsPerOneMillion": 141768,
    "population": 4335767,
    "continent": "North America",
    "oneCasePerPeople": 34,
    "oneDeathPerPeople": 1654,
    "oneTestPerPeople": 7,
    "activePerOneMillion": 4903.17,
    "recoveredPerOneMillion": 23983.07,
    "criticalPerOneMillion": 28.14
  },
  {
    "updated": 1603500524168,
    "country": "Papua New Guinea",
    "countryInfo": {
      "_id": 598,
      "iso2": "PG",
      "iso3": "PNG",
      "lat": -6,
      "long": 147,
      "flag": "https://disease.sh/assets/img/flags/pg.png"
    },
    "cases": 583,
    "todayCases": null,
    "deaths": 7,
    "todayDeaths": null,
    "recovered": 545,
    "todayRecovered": null,
    "active": 31,
    "critical": null,
    "casesPerOneMillion": 65,
    "deathsPerOneMillion": 0.8,
    "tests": 27003,
    "testsPerOneMillion": 3001,
    "population": 8999183,
    "continent": "Australia/Oceania",
    "oneCasePerPeople": 15436,
    "oneDeathPerPeople": 1285598,
    "oneTestPerPeople": 333,
    "activePerOneMillion": 3.44,
    "recoveredPerOneMillion": 60.56,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523757,
    "country": "Paraguay",
    "countryInfo": {
      "_id": 600,
      "iso2": "PY",
      "iso3": "PRY",
      "lat": -23,
      "long": -58,
      "flag": "https://disease.sh/assets/img/flags/py.png"
    },
    "cases": 58259,
    "todayCases": 733,
    "deaths": 1278,
    "todayDeaths": 11,
    "recovered": 38797,
    "todayRecovered": 610,
    "active": 18184,
    "critical": 135,
    "casesPerOneMillion": 8137,
    "deathsPerOneMillion": 178,
    "tests": 342331,
    "testsPerOneMillion": 47813,
    "population": 7159759,
    "continent": "South America",
    "oneCasePerPeople": 123,
    "oneDeathPerPeople": 5602,
    "oneTestPerPeople": 21,
    "activePerOneMillion": 2539.75,
    "recoveredPerOneMillion": 5418.76,
    "criticalPerOneMillion": 18.86
  },
  {
    "updated": 1603500523560,
    "country": "Peru",
    "countryInfo": {
      "_id": 604,
      "iso2": "PE",
      "iso3": "PER",
      "lat": -10,
      "long": -76,
      "flag": "https://disease.sh/assets/img/flags/pe.png"
    },
    "cases": 883116,
    "todayCases": 3240,
    "deaths": 34033,
    "todayDeaths": 49,
    "recovered": 800480,
    "todayRecovered": 3761,
    "active": 48603,
    "critical": 1080,
    "casesPerOneMillion": 26669,
    "deathsPerOneMillion": 1028,
    "tests": 4343547,
    "testsPerOneMillion": 131169,
    "population": 33114228,
    "continent": "South America",
    "oneCasePerPeople": 37,
    "oneDeathPerPeople": 973,
    "oneTestPerPeople": 8,
    "activePerOneMillion": 1467.74,
    "recoveredPerOneMillion": 24173.29,
    "criticalPerOneMillion": 32.61
  },
  {
    "updated": 1603500523641,
    "country": "Philippines",
    "countryInfo": {
      "_id": 608,
      "iso2": "PH",
      "iso3": "PHL",
      "lat": 13,
      "long": 122,
      "flag": "https://disease.sh/assets/img/flags/ph.png"
    },
    "cases": 365799,
    "todayCases": 1923,
    "deaths": 6915,
    "todayDeaths": 132,
    "recovered": 312691,
    "todayRecovered": 424,
    "active": 46193,
    "critical": 1562,
    "casesPerOneMillion": 3324,
    "deathsPerOneMillion": 63,
    "tests": 4518010,
    "testsPerOneMillion": 41060,
    "population": 110033578,
    "continent": "Asia",
    "oneCasePerPeople": 301,
    "oneDeathPerPeople": 15912,
    "oneTestPerPeople": 24,
    "activePerOneMillion": 419.81,
    "recoveredPerOneMillion": 2841.78,
    "criticalPerOneMillion": 14.2
  },
  {
    "updated": 1603500523654,
    "country": "Poland",
    "countryInfo": {
      "_id": 616,
      "iso2": "PL",
      "iso3": "POL",
      "lat": 52,
      "long": 20,
      "flag": "https://disease.sh/assets/img/flags/pl.png"
    },
    "cases": 228318,
    "todayCases": 13632,
    "deaths": 4172,
    "todayDeaths": 153,
    "recovered": 105092,
    "todayRecovered": 2888,
    "active": 119054,
    "critical": 851,
    "casesPerOneMillion": 6035,
    "deathsPerOneMillion": 110,
    "tests": 4221711,
    "testsPerOneMillion": 111587,
    "population": 37833502,
    "continent": "Europe",
    "oneCasePerPeople": 166,
    "oneDeathPerPeople": 9068,
    "oneTestPerPeople": 9,
    "activePerOneMillion": 3146.79,
    "recoveredPerOneMillion": 2777.75,
    "criticalPerOneMillion": 22.49
  },
  {
    "updated": 1603500523670,
    "country": "Portugal",
    "countryInfo": {
      "_id": 620,
      "iso2": "PT",
      "iso3": "PRT",
      "lat": 39.5,
      "long": -8,
      "flag": "https://disease.sh/assets/img/flags/pt.png"
    },
    "cases": 112440,
    "todayCases": 2899,
    "deaths": 2276,
    "todayDeaths": 31,
    "recovered": 65880,
    "todayRecovered": 1349,
    "active": 44284,
    "critical": 198,
    "casesPerOneMillion": 11037,
    "deathsPerOneMillion": 223,
    "tests": 3156991,
    "testsPerOneMillion": 309895,
    "population": 10187285,
    "continent": "Europe",
    "oneCasePerPeople": 91,
    "oneDeathPerPeople": 4476,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 4346.99,
    "recoveredPerOneMillion": 6466.88,
    "criticalPerOneMillion": 19.44
  },
  {
    "updated": 1603500523662,
    "country": "Qatar",
    "countryInfo": {
      "_id": 634,
      "iso2": "QA",
      "iso3": "QAT",
      "lat": 25.5,
      "long": 51.25,
      "flag": "https://disease.sh/assets/img/flags/qa.png"
    },
    "cases": 130711,
    "todayCases": 249,
    "deaths": 229,
    "todayDeaths": 1,
    "recovered": 127599,
    "todayRecovered": 271,
    "active": 2883,
    "critical": 35,
    "casesPerOneMillion": 46553,
    "deathsPerOneMillion": 82,
    "tests": 918548,
    "testsPerOneMillion": 327141,
    "population": 2807805,
    "continent": "Asia",
    "oneCasePerPeople": 21,
    "oneDeathPerPeople": 12261,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 1026.78,
    "recoveredPerOneMillion": 45444.4,
    "criticalPerOneMillion": 12.47
  },
  {
    "updated": 1603500523656,
    "country": "Romania",
    "countryInfo": {
      "_id": 642,
      "iso2": "RO",
      "iso3": "ROU",
      "lat": 46,
      "long": 25,
      "flag": "https://disease.sh/assets/img/flags/ro.png"
    },
    "cases": 201032,
    "todayCases": 5028,
    "deaths": 6245,
    "todayDeaths": 82,
    "recovered": 144429,
    "todayRecovered": 3340,
    "active": 50358,
    "critical": 782,
    "casesPerOneMillion": 10472,
    "deathsPerOneMillion": 325,
    "tests": 3002800,
    "testsPerOneMillion": 156422,
    "population": 19196823,
    "continent": "Europe",
    "oneCasePerPeople": 95,
    "oneDeathPerPeople": 3074,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 2623.25,
    "recoveredPerOneMillion": 7523.59,
    "criticalPerOneMillion": 40.74
  },
  {
    "updated": 1603500523553,
    "country": "Russia",
    "countryInfo": {
      "_id": 643,
      "iso2": "RU",
      "iso3": "RUS",
      "lat": 60,
      "long": 100,
      "flag": "https://disease.sh/assets/img/flags/ru.png"
    },
    "cases": 1480646,
    "todayCases": 17340,
    "deaths": 25525,
    "todayDeaths": 283,
    "recovered": 1119251,
    "todayRecovered": 11263,
    "active": 335870,
    "critical": 2300,
    "casesPerOneMillion": 10145,
    "deathsPerOneMillion": 175,
    "tests": 56230544,
    "testsPerOneMillion": 385262,
    "population": 145954214,
    "continent": "Europe",
    "oneCasePerPeople": 99,
    "oneDeathPerPeople": 5718,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 2301.2,
    "recoveredPerOneMillion": 7668.51,
    "criticalPerOneMillion": 15.76
  },
  {
    "updated": 1603500524058,
    "country": "Rwanda",
    "countryInfo": {
      "_id": 646,
      "iso2": "RW",
      "iso3": "RWA",
      "lat": -2,
      "long": 30,
      "flag": "https://disease.sh/assets/img/flags/rw.png"
    },
    "cases": 5052,
    "todayCases": 35,
    "deaths": 34,
    "todayDeaths": null,
    "recovered": 4806,
    "todayRecovered": 3,
    "active": 212,
    "critical": null,
    "casesPerOneMillion": 387,
    "deathsPerOneMillion": 3,
    "tests": 542222,
    "testsPerOneMillion": 41549,
    "population": 13050178,
    "continent": "Africa",
    "oneCasePerPeople": 2583,
    "oneDeathPerPeople": 383829,
    "oneTestPerPeople": 24,
    "activePerOneMillion": 16.24,
    "recoveredPerOneMillion": 368.27,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524056,
    "country": "R\u00e9union",
    "countryInfo": {
      "_id": 638,
      "iso2": "RE",
      "iso3": "REU",
      "lat": -21.1,
      "long": 55.6,
      "flag": "https://disease.sh/assets/img/flags/re.png"
    },
    "cases": 5149,
    "todayCases": 134,
    "deaths": 20,
    "todayDeaths": 1,
    "recovered": 4630,
    "todayRecovered": 185,
    "active": 499,
    "critical": 10,
    "casesPerOneMillion": 5738,
    "deathsPerOneMillion": 22,
    "tests": 35419,
    "testsPerOneMillion": 39472,
    "population": 897311,
    "continent": "Africa",
    "oneCasePerPeople": 174,
    "oneDeathPerPeople": 44866,
    "oneTestPerPeople": 25,
    "activePerOneMillion": 556.11,
    "recoveredPerOneMillion": 5159.86,
    "criticalPerOneMillion": 11.14
  },
  {
    "updated": 1603500523848,
    "country": "S. Korea",
    "countryInfo": {
      "_id": 410,
      "iso2": "KR",
      "iso3": "KOR",
      "lat": 37,
      "long": 127.5,
      "flag": "https://disease.sh/assets/img/flags/kr.png"
    },
    "cases": 25698,
    "todayCases": 155,
    "deaths": 455,
    "todayDeaths": 2,
    "recovered": 23717,
    "todayRecovered": 70,
    "active": 1526,
    "critical": 62,
    "casesPerOneMillion": 501,
    "deathsPerOneMillion": 9,
    "tests": 2528621,
    "testsPerOneMillion": 49307,
    "population": 51283105,
    "continent": "Asia",
    "oneCasePerPeople": 1996,
    "oneDeathPerPeople": 112710,
    "oneTestPerPeople": 20,
    "activePerOneMillion": 29.76,
    "recoveredPerOneMillion": 462.47,
    "criticalPerOneMillion": 1.21
  },
  {
    "updated": 1603500524261,
    "country": "Saint Kitts and Nevis",
    "countryInfo": {
      "_id": 659,
      "iso2": "KN",
      "iso3": "KNA",
      "lat": 17.3333,
      "long": -62.75,
      "flag": "https://disease.sh/assets/img/flags/kn.png"
    },
    "cases": 19,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 19,
    "todayRecovered": null,
    "active": 0,
    "critical": null,
    "casesPerOneMillion": 356,
    "deathsPerOneMillion": null,
    "tests": 2933,
    "testsPerOneMillion": 55011,
    "population": 53317,
    "continent": "North America",
    "oneCasePerPeople": 2806,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 18,
    "activePerOneMillion": 0,
    "recoveredPerOneMillion": 356.36,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524253,
    "country": "Saint Lucia",
    "countryInfo": {
      "_id": 662,
      "iso2": "LC",
      "iso3": "LCA",
      "lat": 13.8833,
      "long": -61.1333,
      "flag": "https://disease.sh/assets/img/flags/lc.png"
    },
    "cases": 48,
    "todayCases": 6,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 27,
    "todayRecovered": null,
    "active": 21,
    "critical": null,
    "casesPerOneMillion": 261,
    "deathsPerOneMillion": null,
    "tests": 9621,
    "testsPerOneMillion": 52319,
    "population": 183890,
    "continent": "North America",
    "oneCasePerPeople": 3831,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 19,
    "activePerOneMillion": 114.2,
    "recoveredPerOneMillion": 146.83,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524170,
    "country": "Saint Martin",
    "countryInfo": {
      "_id": 663,
      "iso2": "MF",
      "iso3": "MAF",
      "lat": 18.11,
      "long": -63.03,
      "flag": "https://disease.sh/assets/img/flags/mf.png"
    },
    "cases": 538,
    "todayCases": null,
    "deaths": 8,
    "todayDeaths": null,
    "recovered": 422,
    "todayRecovered": null,
    "active": 108,
    "critical": 12,
    "casesPerOneMillion": 13841,
    "deathsPerOneMillion": 206,
    "tests": 6072,
    "testsPerOneMillion": 156217,
    "population": 38869,
    "continent": "North America",
    "oneCasePerPeople": 72,
    "oneDeathPerPeople": 4859,
    "oneTestPerPeople": 6,
    "activePerOneMillion": 2778.56,
    "recoveredPerOneMillion": 10856.98,
    "criticalPerOneMillion": 308.73
  },
  {
    "updated": 1603500524263,
    "country": "Saint Pierre Miquelon",
    "countryInfo": {
      "_id": 666,
      "iso2": "PM",
      "iso3": "SPM",
      "lat": 46.8333,
      "long": -56.3333,
      "flag": "https://disease.sh/assets/img/flags/pm.png"
    },
    "cases": 16,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 12,
    "todayRecovered": null,
    "active": 4,
    "critical": null,
    "casesPerOneMillion": 2766,
    "deathsPerOneMillion": null,
    "tests": 2222,
    "testsPerOneMillion": 384097,
    "population": 5785,
    "continent": "North America",
    "oneCasePerPeople": 362,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 691.44,
    "recoveredPerOneMillion": 2074.33,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524251,
    "country": "Saint Vincent and the Grenadines",
    "countryInfo": {
      "_id": 670,
      "iso2": "VC",
      "iso3": "VCT",
      "lat": 13.25,
      "long": -61.2,
      "flag": "https://disease.sh/assets/img/flags/vc.png"
    },
    "cases": 73,
    "todayCases": 5,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 64,
    "todayRecovered": null,
    "active": 9,
    "critical": null,
    "casesPerOneMillion": 657,
    "deathsPerOneMillion": null,
    "tests": 6080,
    "testsPerOneMillion": 54750,
    "population": 111051,
    "continent": "North America",
    "oneCasePerPeople": 1521,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 18,
    "activePerOneMillion": 81.04,
    "recoveredPerOneMillion": 576.31,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524160,
    "country": "San Marino",
    "countryInfo": {
      "_id": 674,
      "iso2": "SM",
      "iso3": "SMR",
      "lat": 43.7667,
      "long": 12.4167,
      "flag": "https://disease.sh/assets/img/flags/sm.png"
    },
    "cases": 819,
    "todayCases": 17,
    "deaths": 42,
    "todayDeaths": null,
    "recovered": 716,
    "todayRecovered": 5,
    "active": 61,
    "critical": 2,
    "casesPerOneMillion": 24122,
    "deathsPerOneMillion": 1237,
    "tests": 9184,
    "testsPerOneMillion": 270492,
    "population": 33953,
    "continent": "Europe",
    "oneCasePerPeople": 41,
    "oneDeathPerPeople": 808,
    "oneTestPerPeople": 4,
    "activePerOneMillion": 1796.6,
    "recoveredPerOneMillion": 21087.97,
    "criticalPerOneMillion": 58.9
  },
  {
    "updated": 1603500524158,
    "country": "Sao Tome and Principe",
    "countryInfo": {
      "_id": 678,
      "iso2": "ST",
      "iso3": "STP",
      "lat": 1,
      "long": 7,
      "flag": "https://disease.sh/assets/img/flags/st.png"
    },
    "cases": 938,
    "todayCases": 3,
    "deaths": 15,
    "todayDeaths": null,
    "recovered": 898,
    "todayRecovered": null,
    "active": 25,
    "critical": null,
    "casesPerOneMillion": 4256,
    "deathsPerOneMillion": 68,
    "tests": 5975,
    "testsPerOneMillion": 27108,
    "population": 220412,
    "continent": "Africa",
    "oneCasePerPeople": 235,
    "oneDeathPerPeople": 14694,
    "oneTestPerPeople": 37,
    "activePerOneMillion": 113.42,
    "recoveredPerOneMillion": 4074.19,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523646,
    "country": "Saudi Arabia",
    "countryInfo": {
      "_id": 682,
      "iso2": "SA",
      "iso3": "SAU",
      "lat": 25,
      "long": 45,
      "flag": "https://disease.sh/assets/img/flags/sa.png"
    },
    "cases": 344157,
    "todayCases": 383,
    "deaths": 5264,
    "todayDeaths": 14,
    "recovered": 330578,
    "todayRecovered": 397,
    "active": 8315,
    "critical": 796,
    "casesPerOneMillion": 9838,
    "deathsPerOneMillion": 150,
    "tests": 7615539,
    "testsPerOneMillion": 217702,
    "population": 34981543,
    "continent": "Asia",
    "oneCasePerPeople": 102,
    "oneDeathPerPeople": 6645,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 237.7,
    "recoveredPerOneMillion": 9450.07,
    "criticalPerOneMillion": 22.75
  },
  {
    "updated": 1603500523940,
    "country": "Senegal",
    "countryInfo": {
      "_id": 686,
      "iso2": "SN",
      "iso3": "SEN",
      "lat": 14,
      "long": -14,
      "flag": "https://disease.sh/assets/img/flags/sn.png"
    },
    "cases": 15525,
    "todayCases": 17,
    "deaths": 321,
    "todayDeaths": null,
    "recovered": 14082,
    "todayRecovered": 56,
    "active": 1122,
    "critical": 4,
    "casesPerOneMillion": 920,
    "deathsPerOneMillion": 19,
    "tests": 201364,
    "testsPerOneMillion": 11930,
    "population": 16878234,
    "continent": "Africa",
    "oneCasePerPeople": 1087,
    "oneDeathPerPeople": 52580,
    "oneTestPerPeople": 84,
    "activePerOneMillion": 66.48,
    "recoveredPerOneMillion": 834.33,
    "criticalPerOneMillion": 0.24
  },
  {
    "updated": 1603500523837,
    "country": "Serbia",
    "countryInfo": {
      "_id": 688,
      "iso2": "RS",
      "iso3": "SRB",
      "lat": 44,
      "long": 21,
      "flag": "https://disease.sh/assets/img/flags/rs.png"
    },
    "cases": 38115,
    "todayCases": 579,
    "deaths": 786,
    "todayDeaths": 3,
    "recovered": 31536,
    "todayRecovered": null,
    "active": 5793,
    "critical": 24,
    "casesPerOneMillion": 4368,
    "deathsPerOneMillion": 90,
    "tests": 1271455,
    "testsPerOneMillion": 145705,
    "population": 8726200,
    "continent": "Europe",
    "oneCasePerPeople": 229,
    "oneDeathPerPeople": 11102,
    "oneTestPerPeople": 7,
    "activePerOneMillion": 663.86,
    "recoveredPerOneMillion": 3613.94,
    "criticalPerOneMillion": 2.75
  },
  {
    "updated": 1603500524247,
    "country": "Seychelles",
    "countryInfo": {
      "_id": 690,
      "iso2": "SC",
      "iso3": "SYC",
      "lat": -4.5833,
      "long": 55.6667,
      "flag": "https://disease.sh/assets/img/flags/sc.png"
    },
    "cases": 153,
    "todayCases": 2,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 149,
    "todayRecovered": 1,
    "active": 4,
    "critical": null,
    "casesPerOneMillion": 1553,
    "deathsPerOneMillion": null,
    "tests": 5200,
    "testsPerOneMillion": 52772,
    "population": 98538,
    "continent": "Africa",
    "oneCasePerPeople": 644,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 19,
    "activePerOneMillion": 40.59,
    "recoveredPerOneMillion": 1512.11,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524150,
    "country": "Sierra Leone",
    "countryInfo": {
      "_id": 694,
      "iso2": "SL",
      "iso3": "SLE",
      "lat": 8.5,
      "long": -11.5,
      "flag": "https://disease.sh/assets/img/flags/sl.png"
    },
    "cases": 2343,
    "todayCases": 3,
    "deaths": 74,
    "todayDeaths": 1,
    "recovered": 1782,
    "todayRecovered": 5,
    "active": 487,
    "critical": null,
    "casesPerOneMillion": 292,
    "deathsPerOneMillion": 9,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 8026805,
    "continent": "Africa",
    "oneCasePerPeople": 3426,
    "oneDeathPerPeople": 108470,
    "oneTestPerPeople": null,
    "activePerOneMillion": 60.67,
    "recoveredPerOneMillion": 222.01,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523759,
    "country": "Singapore",
    "countryInfo": {
      "_id": 702,
      "iso2": "SG",
      "iso3": "SGP",
      "lat": 1.3667,
      "long": 103.8,
      "flag": "https://disease.sh/assets/img/flags/sg.png"
    },
    "cases": 57951,
    "todayCases": 10,
    "deaths": 28,
    "todayDeaths": null,
    "recovered": 57832,
    "todayRecovered": 3,
    "active": 91,
    "critical": null,
    "casesPerOneMillion": 9881,
    "deathsPerOneMillion": 5,
    "tests": 3486260,
    "testsPerOneMillion": 594446,
    "population": 5864724,
    "continent": "Asia",
    "oneCasePerPeople": 101,
    "oneDeathPerPeople": 209454,
    "oneTestPerPeople": 2,
    "activePerOneMillion": 15.52,
    "recoveredPerOneMillion": 9860.99,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524163,
    "country": "Sint Maarten",
    "countryInfo": {
      "_id": 534,
      "iso2": "SX",
      "iso3": "SXM",
      "lat": 18.02,
      "long": -63.06,
      "flag": "https://disease.sh/assets/img/flags/sx.png"
    },
    "cases": 776,
    "todayCases": 7,
    "deaths": 22,
    "todayDeaths": null,
    "recovered": 702,
    "todayRecovered": 21,
    "active": 52,
    "critical": 6,
    "casesPerOneMillion": 18035,
    "deathsPerOneMillion": 511,
    "tests": 5961,
    "testsPerOneMillion": 138541,
    "population": 43027,
    "continent": "North America",
    "oneCasePerPeople": 55,
    "oneDeathPerPeople": 1956,
    "oneTestPerPeople": 7,
    "activePerOneMillion": 1208.54,
    "recoveredPerOneMillion": 16315.34,
    "criticalPerOneMillion": 139.45
  },
  {
    "updated": 1603500523839,
    "country": "Slovakia",
    "countryInfo": {
      "_id": 703,
      "iso2": "SK",
      "iso3": "SVK",
      "lat": 48.6667,
      "long": 19.5,
      "flag": "https://disease.sh/assets/img/flags/sk.png"
    },
    "cases": 37911,
    "todayCases": 2581,
    "deaths": 134,
    "todayDeaths": 19,
    "recovered": 8859,
    "todayRecovered": 96,
    "active": 28918,
    "critical": 62,
    "casesPerOneMillion": 6943,
    "deathsPerOneMillion": 25,
    "tests": 664544,
    "testsPerOneMillion": 121701,
    "population": 5460477,
    "continent": "Europe",
    "oneCasePerPeople": 144,
    "oneDeathPerPeople": 40750,
    "oneTestPerPeople": 8,
    "activePerOneMillion": 5295.87,
    "recoveredPerOneMillion": 1622.39,
    "criticalPerOneMillion": 11.35
  },
  {
    "updated": 1603500523852,
    "country": "Slovenia",
    "countryInfo": {
      "_id": 705,
      "iso2": "SI",
      "iso3": "SVN",
      "lat": 46,
      "long": 15,
      "flag": "https://disease.sh/assets/img/flags/si.png"
    },
    "cases": 19307,
    "todayCases": 1656,
    "deaths": 214,
    "todayDeaths": 3,
    "recovered": 7659,
    "todayRecovered": 360,
    "active": 11434,
    "critical": 67,
    "casesPerOneMillion": 9287,
    "deathsPerOneMillion": 103,
    "tests": 313988,
    "testsPerOneMillion": 151026,
    "population": 2079028,
    "continent": "Europe",
    "oneCasePerPeople": 108,
    "oneDeathPerPeople": 9715,
    "oneTestPerPeople": 7,
    "activePerOneMillion": 5499.69,
    "recoveredPerOneMillion": 3683.93,
    "criticalPerOneMillion": 32.23
  },
  {
    "updated": 1603500524267,
    "country": "Solomon Islands",
    "countryInfo": {
      "_id": 90,
      "iso2": "SB",
      "iso3": "SLB",
      "lat": -8,
      "long": 159,
      "flag": "https://disease.sh/assets/img/flags/sb.png"
    },
    "cases": 4,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 3,
    "todayRecovered": null,
    "active": 1,
    "critical": null,
    "casesPerOneMillion": 6,
    "deathsPerOneMillion": null,
    "tests": 96,
    "testsPerOneMillion": 139,
    "population": 692025,
    "continent": "Australia/Oceania",
    "oneCasePerPeople": 173006,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 7209,
    "activePerOneMillion": 1.45,
    "recoveredPerOneMillion": 4.34,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524139,
    "country": "Somalia",
    "countryInfo": {
      "_id": 706,
      "iso2": "SO",
      "iso3": "SOM",
      "lat": 10,
      "long": 49,
      "flag": "https://disease.sh/assets/img/flags/so.png"
    },
    "cases": 3897,
    "todayCases": null,
    "deaths": 102,
    "todayDeaths": null,
    "recovered": 3166,
    "todayRecovered": null,
    "active": 629,
    "critical": null,
    "casesPerOneMillion": 243,
    "deathsPerOneMillion": 6,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 16027872,
    "continent": "Africa",
    "oneCasePerPeople": 4113,
    "oneDeathPerPeople": 157136,
    "oneTestPerPeople": null,
    "activePerOneMillion": 39.24,
    "recoveredPerOneMillion": 197.53,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523563,
    "country": "South Africa",
    "countryInfo": {
      "_id": 710,
      "iso2": "ZA",
      "iso3": "ZAF",
      "lat": -29,
      "long": 24,
      "flag": "https://disease.sh/assets/img/flags/za.png"
    },
    "cases": 712412,
    "todayCases": 1897,
    "deaths": 18891,
    "todayDeaths": 48,
    "recovered": 643523,
    "todayRecovered": 963,
    "active": 49998,
    "critical": 546,
    "casesPerOneMillion": 11965,
    "deathsPerOneMillion": 317,
    "tests": 4657116,
    "testsPerOneMillion": 78217,
    "population": 59540914,
    "continent": "Africa",
    "oneCasePerPeople": 84,
    "oneDeathPerPeople": 3152,
    "oneTestPerPeople": 13,
    "activePerOneMillion": 839.73,
    "recoveredPerOneMillion": 10808.08,
    "criticalPerOneMillion": 9.17
  },
  {
    "updated": 1603500524144,
    "country": "South Sudan",
    "countryInfo": {
      "_id": 728,
      "iso2": "SS",
      "iso3": "SSD",
      "lat": 6.8769,
      "long": 31.3069,
      "flag": "https://disease.sh/assets/img/flags/ss.png"
    },
    "cases": 2876,
    "todayCases": 4,
    "deaths": 56,
    "todayDeaths": 1,
    "recovered": 1290,
    "todayRecovered": null,
    "active": 1530,
    "critical": null,
    "casesPerOneMillion": 256,
    "deathsPerOneMillion": 5,
    "tests": 12044,
    "testsPerOneMillion": 1072,
    "population": 11234532,
    "continent": "Africa",
    "oneCasePerPeople": 3906,
    "oneDeathPerPeople": 200617,
    "oneTestPerPeople": 933,
    "activePerOneMillion": 136.19,
    "recoveredPerOneMillion": 114.82,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523555,
    "country": "Spain",
    "countryInfo": {
      "_id": 724,
      "iso2": "ES",
      "iso3": "ESP",
      "lat": 40,
      "long": -4,
      "flag": "https://disease.sh/assets/img/flags/es.png"
    },
    "cases": 1110372,
    "todayCases": 19851,
    "deaths": 34752,
    "todayDeaths": 231,
    "recovered": null,
    "todayRecovered": null,
    "active": 1075620,
    "critical": 2031,
    "casesPerOneMillion": 23746,
    "deathsPerOneMillion": 743,
    "tests": 15503165,
    "testsPerOneMillion": 331544,
    "population": 46760495,
    "continent": "Europe",
    "oneCasePerPeople": 42,
    "oneDeathPerPeople": 1346,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 23002.75,
    "recoveredPerOneMillion": null,
    "criticalPerOneMillion": 43.43
  },
  {
    "updated": 1603500524042,
    "country": "Sri Lanka",
    "countryInfo": {
      "_id": 144,
      "iso2": "LK",
      "iso3": "LKA",
      "lat": 7,
      "long": 81,
      "flag": "https://disease.sh/assets/img/flags/lk.png"
    },
    "cases": 7153,
    "todayCases": 866,
    "deaths": 14,
    "todayDeaths": null,
    "recovered": 3644,
    "todayRecovered": 83,
    "active": 3495,
    "critical": null,
    "casesPerOneMillion": 334,
    "deathsPerOneMillion": 0.7,
    "tests": 423332,
    "testsPerOneMillion": 19744,
    "population": 21441452,
    "continent": "Asia",
    "oneCasePerPeople": 2998,
    "oneDeathPerPeople": 1531532,
    "oneTestPerPeople": 51,
    "activePerOneMillion": 163,
    "recoveredPerOneMillion": 169.95,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524250,
    "country": "St. Barth",
    "countryInfo": {
      "_id": 652,
      "iso2": "BL",
      "iso3": "BLM",
      "lat": 17.89,
      "long": -62.82,
      "flag": "https://disease.sh/assets/img/flags/bl.png"
    },
    "cases": 77,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 66,
    "todayRecovered": null,
    "active": 11,
    "critical": null,
    "casesPerOneMillion": 7789,
    "deathsPerOneMillion": null,
    "tests": 3526,
    "testsPerOneMillion": 356666,
    "population": 9886,
    "continent": "North America",
    "oneCasePerPeople": 128,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 1112.68,
    "recoveredPerOneMillion": 6676.11,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523942,
    "country": "Sudan",
    "countryInfo": {
      "_id": 736,
      "iso2": "SD",
      "iso3": "SDN",
      "lat": 15,
      "long": 30,
      "flag": "https://disease.sh/assets/img/flags/sd.png"
    },
    "cases": 13724,
    "todayCases": null,
    "deaths": 836,
    "todayDeaths": null,
    "recovered": 6764,
    "todayRecovered": null,
    "active": 6124,
    "critical": null,
    "casesPerOneMillion": 311,
    "deathsPerOneMillion": 19,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 44162303,
    "continent": "Africa",
    "oneCasePerPeople": 3218,
    "oneDeathPerPeople": 52826,
    "oneTestPerPeople": null,
    "activePerOneMillion": 138.67,
    "recoveredPerOneMillion": 153.16,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524055,
    "country": "Suriname",
    "countryInfo": {
      "_id": 740,
      "iso2": "SR",
      "iso3": "SUR",
      "lat": 4,
      "long": -56,
      "flag": "https://disease.sh/assets/img/flags/sr.png"
    },
    "cases": 5155,
    "todayCases": 1,
    "deaths": 109,
    "todayDeaths": null,
    "recovered": 5010,
    "todayRecovered": 15,
    "active": 36,
    "critical": 6,
    "casesPerOneMillion": 8763,
    "deathsPerOneMillion": 185,
    "tests": 17798,
    "testsPerOneMillion": 30255,
    "population": 588273,
    "continent": "South America",
    "oneCasePerPeople": 114,
    "oneDeathPerPeople": 5397,
    "oneTestPerPeople": 33,
    "activePerOneMillion": 61.2,
    "recoveredPerOneMillion": 8516.45,
    "criticalPerOneMillion": 10.2
  },
  {
    "updated": 1603500524047,
    "country": "Swaziland",
    "countryInfo": {
      "_id": 748,
      "iso2": "SZ",
      "iso3": "SWZ",
      "lat": -26.5,
      "long": 31.5,
      "flag": "https://disease.sh/assets/img/flags/sz.png"
    },
    "cases": 5831,
    "todayCases": 17,
    "deaths": 116,
    "todayDeaths": null,
    "recovered": 5485,
    "todayRecovered": 17,
    "active": 230,
    "critical": 19,
    "casesPerOneMillion": 5010,
    "deathsPerOneMillion": 100,
    "tests": 45870,
    "testsPerOneMillion": 39410,
    "population": 1163906,
    "continent": "Africa",
    "oneCasePerPeople": 200,
    "oneDeathPerPeople": 10034,
    "oneTestPerPeople": 25,
    "activePerOneMillion": 197.61,
    "recoveredPerOneMillion": 4712.58,
    "criticalPerOneMillion": 16.32
  },
  {
    "updated": 1603500523673,
    "country": "Sweden",
    "countryInfo": {
      "_id": 752,
      "iso2": "SE",
      "iso3": "SWE",
      "lat": 62,
      "long": 15,
      "flag": "https://disease.sh/assets/img/flags/se.png"
    },
    "cases": 110594,
    "todayCases": null,
    "deaths": 5933,
    "todayDeaths": 7,
    "recovered": null,
    "todayRecovered": null,
    "active": 104661,
    "critical": 39,
    "casesPerOneMillion": 10929,
    "deathsPerOneMillion": 586,
    "tests": 2074744,
    "testsPerOneMillion": 205035,
    "population": 10118993,
    "continent": "Europe",
    "oneCasePerPeople": 91,
    "oneDeathPerPeople": 1706,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 10343.03,
    "recoveredPerOneMillion": null,
    "criticalPerOneMillion": 3.85
  },
  {
    "updated": 1603500523737,
    "country": "Switzerland",
    "countryInfo": {
      "_id": 756,
      "iso2": "CH",
      "iso3": "CHE",
      "lat": 47,
      "long": 8,
      "flag": "https://disease.sh/assets/img/flags/ch.png"
    },
    "cases": 103653,
    "todayCases": 6634,
    "deaths": 2067,
    "todayDeaths": 15,
    "recovered": 55800,
    "todayRecovered": 100,
    "active": 45786,
    "critical": 116,
    "casesPerOneMillion": 11949,
    "deathsPerOneMillion": 238,
    "tests": 1726438,
    "testsPerOneMillion": 199026,
    "population": 8674421,
    "continent": "Europe",
    "oneCasePerPeople": 84,
    "oneDeathPerPeople": 4197,
    "oneTestPerPeople": 5,
    "activePerOneMillion": 5278.28,
    "recoveredPerOneMillion": 6432.71,
    "criticalPerOneMillion": 13.37
  },
  {
    "updated": 1603500524052,
    "country": "Syrian Arab Republic",
    "countryInfo": {
      "_id": 760,
      "iso2": "SY",
      "iso3": "SYR",
      "lat": 35,
      "long": 38,
      "flag": "https://disease.sh/assets/img/flags/sy.png"
    },
    "cases": 5319,
    "todayCases": 52,
    "deaths": 264,
    "todayDeaths": 4,
    "recovered": 1692,
    "todayRecovered": 37,
    "active": 3363,
    "critical": null,
    "casesPerOneMillion": 302,
    "deathsPerOneMillion": 15,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 17630464,
    "continent": "Asia",
    "oneCasePerPeople": 3315,
    "oneDeathPerPeople": 66782,
    "oneTestPerPeople": null,
    "activePerOneMillion": 190.75,
    "recoveredPerOneMillion": 95.97,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524169,
    "country": "Taiwan",
    "countryInfo": {
      "_id": 158,
      "iso2": "TW",
      "iso3": "TWN",
      "lat": 23.5,
      "long": 121,
      "flag": "https://disease.sh/assets/img/flags/tw.png"
    },
    "cases": 548,
    "todayCases": null,
    "deaths": 7,
    "todayDeaths": null,
    "recovered": 497,
    "todayRecovered": null,
    "active": 44,
    "critical": null,
    "casesPerOneMillion": 23,
    "deathsPerOneMillion": 0.3,
    "tests": 99800,
    "testsPerOneMillion": 4188,
    "population": 23830358,
    "continent": "Asia",
    "oneCasePerPeople": 43486,
    "oneDeathPerPeople": 3404337,
    "oneTestPerPeople": 239,
    "activePerOneMillion": 1.85,
    "recoveredPerOneMillion": 20.86,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523953,
    "country": "Tajikistan",
    "countryInfo": {
      "_id": 762,
      "iso2": "TJ",
      "iso3": "TJK",
      "lat": 39,
      "long": 71,
      "flag": "https://disease.sh/assets/img/flags/tj.png"
    },
    "cases": 10695,
    "todayCases": 42,
    "deaths": 81,
    "todayDeaths": null,
    "recovered": 9782,
    "todayRecovered": 58,
    "active": 832,
    "critical": null,
    "casesPerOneMillion": 1114,
    "deathsPerOneMillion": 8,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 9603233,
    "continent": "Asia",
    "oneCasePerPeople": 898,
    "oneDeathPerPeople": 118558,
    "oneTestPerPeople": null,
    "activePerOneMillion": 86.64,
    "recoveredPerOneMillion": 1018.62,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524237,
    "country": "Tanzania",
    "countryInfo": {
      "_id": 834,
      "iso2": "TZ",
      "iso3": "TZA",
      "lat": -6,
      "long": 35,
      "flag": "https://disease.sh/assets/img/flags/tz.png"
    },
    "cases": 509,
    "todayCases": null,
    "deaths": 21,
    "todayDeaths": null,
    "recovered": 183,
    "todayRecovered": null,
    "active": 305,
    "critical": 7,
    "casesPerOneMillion": 8,
    "deathsPerOneMillion": 0.3,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 60250432,
    "continent": "Africa",
    "oneCasePerPeople": 118370,
    "oneDeathPerPeople": 2869068,
    "oneTestPerPeople": null,
    "activePerOneMillion": 5.06,
    "recoveredPerOneMillion": 3.04,
    "criticalPerOneMillion": 0.12
  },
  {
    "updated": 1603500524140,
    "country": "Thailand",
    "countryInfo": {
      "_id": 764,
      "iso2": "TH",
      "iso3": "THA",
      "lat": 15,
      "long": 100,
      "flag": "https://disease.sh/assets/img/flags/th.png"
    },
    "cases": 3727,
    "todayCases": 8,
    "deaths": 59,
    "todayDeaths": null,
    "recovered": 3518,
    "todayRecovered": 4,
    "active": 150,
    "critical": 1,
    "casesPerOneMillion": 53,
    "deathsPerOneMillion": 0.8,
    "tests": 977854,
    "testsPerOneMillion": 13998,
    "population": 69855116,
    "continent": "Asia",
    "oneCasePerPeople": 18743,
    "oneDeathPerPeople": 1183985,
    "oneTestPerPeople": 71,
    "activePerOneMillion": 2.15,
    "recoveredPerOneMillion": 50.36,
    "criticalPerOneMillion": 0.01
  },
  {
    "updated": 1603500524256,
    "country": "Timor-Leste",
    "countryInfo": {
      "_id": 626,
      "iso2": "TL",
      "iso3": "TLS",
      "lat": -8.55,
      "long": 125.5167,
      "flag": "https://disease.sh/assets/img/flags/tl.png"
    },
    "cases": 29,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 28,
    "todayRecovered": null,
    "active": 1,
    "critical": null,
    "casesPerOneMillion": 22,
    "deathsPerOneMillion": null,
    "tests": 10129,
    "testsPerOneMillion": 7638,
    "population": 1326172,
    "continent": "Asia",
    "oneCasePerPeople": 45730,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 131,
    "activePerOneMillion": 0.75,
    "recoveredPerOneMillion": 21.11,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524151,
    "country": "Togo",
    "countryInfo": {
      "_id": 768,
      "iso2": "TG",
      "iso3": "TGO",
      "lat": 8,
      "long": 1.1667,
      "flag": "https://disease.sh/assets/img/flags/tg.png"
    },
    "cases": 2162,
    "todayCases": 23,
    "deaths": 52,
    "todayDeaths": null,
    "recovered": 1586,
    "todayRecovered": 12,
    "active": 524,
    "critical": null,
    "casesPerOneMillion": 259,
    "deathsPerOneMillion": 6,
    "tests": 111706,
    "testsPerOneMillion": 13397,
    "population": 8338043,
    "continent": "Africa",
    "oneCasePerPeople": 3857,
    "oneDeathPerPeople": 160347,
    "oneTestPerPeople": 75,
    "activePerOneMillion": 62.84,
    "recoveredPerOneMillion": 190.21,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524050,
    "country": "Trinidad and Tobago",
    "countryInfo": {
      "_id": 780,
      "iso2": "TT",
      "iso3": "TTO",
      "lat": 11,
      "long": -61,
      "flag": "https://disease.sh/assets/img/flags/tt.png"
    },
    "cases": 5487,
    "todayCases": 41,
    "deaths": 104,
    "todayDeaths": 1,
    "recovered": 3945,
    "todayRecovered": 69,
    "active": 1438,
    "critical": 14,
    "casesPerOneMillion": 3917,
    "deathsPerOneMillion": 74,
    "tests": 32009,
    "testsPerOneMillion": 22849,
    "population": 1400913,
    "continent": "North America",
    "oneCasePerPeople": 255,
    "oneDeathPerPeople": 13470,
    "oneTestPerPeople": 44,
    "activePerOneMillion": 1026.47,
    "recoveredPerOneMillion": 2816.02,
    "criticalPerOneMillion": 9.99
  },
  {
    "updated": 1603500523772,
    "country": "Tunisia",
    "countryInfo": {
      "_id": 788,
      "iso2": "TN",
      "iso3": "TUN",
      "lat": 34,
      "long": 9,
      "flag": "https://disease.sh/assets/img/flags/tn.png"
    },
    "cases": 47214,
    "todayCases": 1322,
    "deaths": 784,
    "todayDeaths": 44,
    "recovered": 5032,
    "todayRecovered": null,
    "active": 41398,
    "critical": 163,
    "casesPerOneMillion": 3982,
    "deathsPerOneMillion": 66,
    "tests": 314496,
    "testsPerOneMillion": 26524,
    "population": 11857139,
    "continent": "Africa",
    "oneCasePerPeople": 251,
    "oneDeathPerPeople": 15124,
    "oneTestPerPeople": 38,
    "activePerOneMillion": 3491.4,
    "recoveredPerOneMillion": 424.39,
    "criticalPerOneMillion": 13.75
  },
  {
    "updated": 1603500523643,
    "country": "Turkey",
    "countryInfo": {
      "_id": 792,
      "iso2": "TR",
      "iso3": "TUR",
      "lat": 39,
      "long": 35,
      "flag": "https://disease.sh/assets/img/flags/tr.png"
    },
    "cases": 357693,
    "todayCases": 2165,
    "deaths": 9658,
    "todayDeaths": 74,
    "recovered": 311520,
    "todayRecovered": 1493,
    "active": 36515,
    "critical": 1648,
    "casesPerOneMillion": 4227,
    "deathsPerOneMillion": 114,
    "tests": 12992246,
    "testsPerOneMillion": 153533,
    "population": 84621631,
    "continent": "Asia",
    "oneCasePerPeople": 237,
    "oneDeathPerPeople": 8762,
    "oneTestPerPeople": 7,
    "activePerOneMillion": 431.51,
    "recoveredPerOneMillion": 3681.33,
    "criticalPerOneMillion": 19.47
  },
  {
    "updated": 1603500524165,
    "country": "Turks and Caicos Islands",
    "countryInfo": {
      "_id": 796,
      "iso2": "TC",
      "iso3": "TCA",
      "lat": 21.75,
      "long": -71.5833,
      "flag": "https://disease.sh/assets/img/flags/tc.png"
    },
    "cases": 699,
    "todayCases": 1,
    "deaths": 6,
    "todayDeaths": null,
    "recovered": 689,
    "todayRecovered": null,
    "active": 4,
    "critical": 1,
    "casesPerOneMillion": 17979,
    "deathsPerOneMillion": 154,
    "tests": 4099,
    "testsPerOneMillion": 105430,
    "population": 38879,
    "continent": "North America",
    "oneCasePerPeople": 56,
    "oneDeathPerPeople": 6480,
    "oneTestPerPeople": 9,
    "activePerOneMillion": 102.88,
    "recoveredPerOneMillion": 17721.65,
    "criticalPerOneMillion": 25.72
  },
  {
    "updated": 1603500523666,
    "country": "UAE",
    "countryInfo": {
      "_id": 784,
      "iso2": "AE",
      "iso3": "ARE",
      "lat": 24,
      "long": 54,
      "flag": "https://disease.sh/assets/img/flags/ae.png"
    },
    "cases": 122273,
    "todayCases": 1563,
    "deaths": 475,
    "todayDeaths": 1,
    "recovered": 115068,
    "todayRecovered": 1704,
    "active": 6730,
    "critical": null,
    "casesPerOneMillion": 12317,
    "deathsPerOneMillion": 48,
    "tests": 12223225,
    "testsPerOneMillion": 1231244,
    "population": 9927540,
    "continent": "Asia",
    "oneCasePerPeople": 81,
    "oneDeathPerPeople": 20900,
    "oneTestPerPeople": 1,
    "activePerOneMillion": 677.91,
    "recoveredPerOneMillion": 11590.79,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523562,
    "country": "UK",
    "countryInfo": {
      "_id": 826,
      "iso2": "GB",
      "iso3": "GBR",
      "lat": 54,
      "long": -2,
      "flag": "https://disease.sh/assets/img/flags/gb.png"
    },
    "cases": 830998,
    "todayCases": 20530,
    "deaths": 44571,
    "todayDeaths": 224,
    "recovered": null,
    "todayRecovered": null,
    "active": 786427,
    "critical": 707,
    "casesPerOneMillion": 12221,
    "deathsPerOneMillion": 655,
    "tests": 31157988,
    "testsPerOneMillion": 458220,
    "population": 67997872,
    "continent": "Europe",
    "oneCasePerPeople": 82,
    "oneDeathPerPeople": 1526,
    "oneTestPerPeople": 2,
    "activePerOneMillion": 11565.46,
    "recoveredPerOneMillion": null,
    "criticalPerOneMillion": 10.4
  },
  {
    "updated": 1603500523549,
    "country": "USA",
    "countryInfo": {
      "_id": 840,
      "iso2": "US",
      "iso3": "USA",
      "lat": 38,
      "long": -97,
      "flag": "https://disease.sh/assets/img/flags/us.png"
    },
    "cases": 8746899,
    "todayCases": 81156,
    "deaths": 229284,
    "todayDeaths": 903,
    "recovered": 5698122,
    "todayRecovered": 42821,
    "active": 2819493,
    "critical": 16329,
    "casesPerOneMillion": 26377,
    "deathsPerOneMillion": 691,
    "tests": 131030574,
    "testsPerOneMillion": 395133,
    "population": 331611010,
    "continent": "North America",
    "oneCasePerPeople": 38,
    "oneDeathPerPeople": 1446,
    "oneTestPerPeople": 3,
    "activePerOneMillion": 8502.41,
    "recoveredPerOneMillion": 17183.15,
    "criticalPerOneMillion": 49.24
  },
  {
    "updated": 1603500523950,
    "country": "Uganda",
    "countryInfo": {
      "_id": 800,
      "iso2": "UG",
      "iso3": "UGA",
      "lat": 1,
      "long": 32,
      "flag": "https://disease.sh/assets/img/flags/ug.png"
    },
    "cases": 11163,
    "todayCases": 122,
    "deaths": 99,
    "todayDeaths": 1,
    "recovered": 7269,
    "todayRecovered": 59,
    "active": 3795,
    "critical": null,
    "casesPerOneMillion": 242,
    "deathsPerOneMillion": 2,
    "tests": 532332,
    "testsPerOneMillion": 11528,
    "population": 46177192,
    "continent": "Africa",
    "oneCasePerPeople": 4137,
    "oneDeathPerPeople": 466436,
    "oneTestPerPeople": 87,
    "activePerOneMillion": 82.18,
    "recoveredPerOneMillion": 157.42,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523647,
    "country": "Ukraine",
    "countryInfo": {
      "_id": 804,
      "iso2": "UA",
      "iso3": "UKR",
      "lat": 49,
      "long": 32,
      "flag": "https://disease.sh/assets/img/flags/ua.png"
    },
    "cases": 330396,
    "todayCases": 7517,
    "deaths": 6164,
    "todayDeaths": 121,
    "recovered": 137578,
    "todayRecovered": 2680,
    "active": 186654,
    "critical": 177,
    "casesPerOneMillion": 7569,
    "deathsPerOneMillion": 141,
    "tests": 2950463,
    "testsPerOneMillion": 67593,
    "population": 43650159,
    "continent": "Europe",
    "oneCasePerPeople": 132,
    "oneDeathPerPeople": 7081,
    "oneTestPerPeople": 15,
    "activePerOneMillion": 4276.14,
    "recoveredPerOneMillion": 3151.83,
    "criticalPerOneMillion": 4.05
  },
  {
    "updated": 1603500524146,
    "country": "Uruguay",
    "countryInfo": {
      "_id": 858,
      "iso2": "UY",
      "iso3": "URY",
      "lat": -33,
      "long": -56,
      "flag": "https://disease.sh/assets/img/flags/uy.png"
    },
    "cases": 2759,
    "todayCases": 58,
    "deaths": 53,
    "todayDeaths": null,
    "recovered": 2241,
    "todayRecovered": 37,
    "active": 465,
    "critical": 8,
    "casesPerOneMillion": 793,
    "deathsPerOneMillion": 15,
    "tests": 295579,
    "testsPerOneMillion": 84997,
    "population": 3477515,
    "continent": "South America",
    "oneCasePerPeople": 1260,
    "oneDeathPerPeople": 65613,
    "oneTestPerPeople": 12,
    "activePerOneMillion": 133.72,
    "recoveredPerOneMillion": 644.43,
    "criticalPerOneMillion": 2.3
  },
  {
    "updated": 1603500523755,
    "country": "Uzbekistan",
    "countryInfo": {
      "_id": 860,
      "iso2": "UZ",
      "iso3": "UZB",
      "lat": 41,
      "long": 64,
      "flag": "https://disease.sh/assets/img/flags/uz.png"
    },
    "cases": 64724,
    "todayCases": 285,
    "deaths": 542,
    "todayDeaths": 2,
    "recovered": 61957,
    "todayRecovered": 299,
    "active": 2225,
    "critical": 252,
    "casesPerOneMillion": 1925,
    "deathsPerOneMillion": 16,
    "tests": 1377915,
    "testsPerOneMillion": 40986,
    "population": 33619442,
    "continent": "Asia",
    "oneCasePerPeople": 519,
    "oneDeathPerPeople": 62028,
    "oneTestPerPeople": 24,
    "activePerOneMillion": 66.18,
    "recoveredPerOneMillion": 1842.89,
    "criticalPerOneMillion": 7.5
  },
  {
    "updated": 1603500523749,
    "country": "Venezuela",
    "countryInfo": {
      "_id": 862,
      "iso2": "VE",
      "iso3": "VEN",
      "lat": 8,
      "long": -66,
      "flag": "https://disease.sh/assets/img/flags/ve.png"
    },
    "cases": 88416,
    "todayCases": null,
    "deaths": 759,
    "todayDeaths": null,
    "recovered": 82284,
    "todayRecovered": null,
    "active": 5373,
    "critical": 117,
    "casesPerOneMillion": 3112,
    "deathsPerOneMillion": 27,
    "tests": 2022949,
    "testsPerOneMillion": 71205,
    "population": 28410403,
    "continent": "South America",
    "oneCasePerPeople": 321,
    "oneDeathPerPeople": 37431,
    "oneTestPerPeople": 14,
    "activePerOneMillion": 189.12,
    "recoveredPerOneMillion": 2896.26,
    "criticalPerOneMillion": 4.12
  },
  {
    "updated": 1603500524157,
    "country": "Vietnam",
    "countryInfo": {
      "_id": 704,
      "iso2": "VN",
      "iso3": "VNM",
      "lat": 21,
      "long": 105.8,
      "flag": "https://disease.sh/assets/img/flags/vn.png"
    },
    "cases": 1148,
    "todayCases": null,
    "deaths": 35,
    "todayDeaths": null,
    "recovered": 1049,
    "todayRecovered": null,
    "active": 64,
    "critical": null,
    "casesPerOneMillion": 12,
    "deathsPerOneMillion": 0.4,
    "tests": 1246480,
    "testsPerOneMillion": 12770,
    "population": 97611928,
    "continent": "Asia",
    "oneCasePerPeople": 85028,
    "oneDeathPerPeople": 2788912,
    "oneTestPerPeople": 78,
    "activePerOneMillion": 0.66,
    "recoveredPerOneMillion": 10.75,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524269,
    "country": "Wallis and Futuna",
    "countryInfo": {
      "_id": 876,
      "iso2": "WF",
      "iso3": "WLF",
      "lat": -13.3,
      "long": -176.2,
      "flag": "https://disease.sh/assets/img/flags/wf.png"
    },
    "cases": 1,
    "todayCases": null,
    "deaths": null,
    "todayDeaths": null,
    "recovered": 1,
    "todayRecovered": 1,
    "active": 0,
    "critical": null,
    "casesPerOneMillion": 89,
    "deathsPerOneMillion": null,
    "tests": 48,
    "testsPerOneMillion": 4295,
    "population": 11175,
    "continent": "Australia/Oceania",
    "oneCasePerPeople": 11175,
    "oneDeathPerPeople": null,
    "oneTestPerPeople": 233,
    "activePerOneMillion": 0,
    "recoveredPerOneMillion": 89.49,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524266,
    "country": "Western Sahara",
    "countryInfo": {
      "_id": 732,
      "iso2": "EH",
      "iso3": "ESH",
      "lat": 24.5,
      "long": -13,
      "flag": "https://disease.sh/assets/img/flags/eh.png"
    },
    "cases": 10,
    "todayCases": null,
    "deaths": 1,
    "todayDeaths": null,
    "recovered": 8,
    "todayRecovered": null,
    "active": 1,
    "critical": null,
    "casesPerOneMillion": 17,
    "deathsPerOneMillion": 2,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 601821,
    "continent": "Africa",
    "oneCasePerPeople": 60182,
    "oneDeathPerPeople": 601821,
    "oneTestPerPeople": null,
    "activePerOneMillion": 1.66,
    "recoveredPerOneMillion": 13.29,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524152,
    "country": "Yemen",
    "countryInfo": {
      "_id": 887,
      "iso2": "YE",
      "iso3": "YEM",
      "lat": 15,
      "long": 48,
      "flag": "https://disease.sh/assets/img/flags/ye.png"
    },
    "cases": 2060,
    "todayCases": 3,
    "deaths": 599,
    "todayDeaths": 2,
    "recovered": 1354,
    "todayRecovered": 10,
    "active": 107,
    "critical": null,
    "casesPerOneMillion": 69,
    "deathsPerOneMillion": 20,
    "tests": null,
    "testsPerOneMillion": null,
    "population": 30027214,
    "continent": "Asia",
    "oneCasePerPeople": 14576,
    "oneDeathPerPeople": 50129,
    "oneTestPerPeople": null,
    "activePerOneMillion": 3.56,
    "recoveredPerOneMillion": 45.09,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500523938,
    "country": "Zambia",
    "countryInfo": {
      "_id": 894,
      "iso2": "ZM",
      "iso3": "ZMB",
      "lat": -15,
      "long": 30,
      "flag": "https://disease.sh/assets/img/flags/zm.png"
    },
    "cases": 16095,
    "todayCases": 60,
    "deaths": 346,
    "todayDeaths": null,
    "recovered": 15179,
    "todayRecovered": 11,
    "active": 570,
    "critical": null,
    "casesPerOneMillion": 868,
    "deathsPerOneMillion": 19,
    "tests": 225645,
    "testsPerOneMillion": 12171,
    "population": 18540277,
    "continent": "Africa",
    "oneCasePerPeople": 1152,
    "oneDeathPerPeople": 53585,
    "oneTestPerPeople": 82,
    "activePerOneMillion": 30.74,
    "recoveredPerOneMillion": 818.7,
    "criticalPerOneMillion": null
  },
  {
    "updated": 1603500524039,
    "country": "Zimbabwe",
    "countryInfo": {
      "_id": 716,
      "iso2": "ZW",
      "iso3": "ZWE",
      "lat": -20,
      "long": 30,
      "flag": "https://disease.sh/assets/img/flags/zw.png"
    },
    "cases": 8257,
    "todayCases": 15,
    "deaths": 236,
    "todayDeaths": null,
    "recovered": 7771,
    "todayRecovered": 29,
    "active": 250,
    "critical": null,
    "casesPerOneMillion": 553,
    "deathsPerOneMillion": 16,
    "tests": 162958,
    "testsPerOneMillion": 10915,
    "population": 14929932,
    "continent": "Africa",
    "oneCasePerPeople": 1808,
    "oneDeathPerPeople": 63262,
    "oneTestPerPeople": 92,
    "activePerOneMillion": 16.74,
    "recoveredPerOneMillion": 520.5,
    "criticalPerOneMillion": null
  }
]'''


class JHUCSSECountries:
    def __init__(self):
        self.request_url = "https://disease.sh/v3/covid-19/jhucsse"
        self.example_response = '''[
  {
    "country": "Afghanistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 40626,
      "deaths": 1505,
      "recovered": 33831
    },
    "coordinates": {
      "latitude": "33.93911",
      "longitude": "67.709953"
    },
    "province": null
  },
  {
    "country": "Albania",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18250,
      "deaths": 465,
      "recovered": 10395
    },
    "coordinates": {
      "latitude": "41.1533",
      "longitude": "20.1683"
    },
    "province": null
  },
  {
    "country": "Algeria",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 55357,
      "deaths": 1888,
      "recovered": 38618
    },
    "coordinates": {
      "latitude": "28.0339",
      "longitude": "1.6596"
    },
    "province": null
  },
  {
    "country": "Andorra",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3811,
      "deaths": 63,
      "recovered": 2470
    },
    "coordinates": {
      "latitude": "42.5063",
      "longitude": "1.5218"
    },
    "province": null
  },
  {
    "country": "Angola",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8582,
      "deaths": 260,
      "recovered": 3305
    },
    "coordinates": {
      "latitude": "-11.2027",
      "longitude": "17.8739"
    },
    "province": null
  },
  {
    "country": "Antigua and Barbuda",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 122,
      "deaths": 3,
      "recovered": 107
    },
    "coordinates": {
      "latitude": "17.0608",
      "longitude": "-61.7964"
    },
    "province": null
  },
  {
    "country": "Argentina",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1053650,
      "deaths": 27957,
      "recovered": 851854
    },
    "coordinates": {
      "latitude": "-38.4161",
      "longitude": "-63.6167"
    },
    "province": null
  },
  {
    "country": "Armenia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 70836,
      "deaths": 1131,
      "recovered": 49787
    },
    "coordinates": {
      "latitude": "40.0691",
      "longitude": "45.0382"
    },
    "province": null
  },
  {
    "country": "Australia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 114,
      "deaths": 3,
      "recovered": 110
    },
    "coordinates": {
      "latitude": "-35.4735",
      "longitude": "149.0124"
    },
    "province": "Australian Capital Territory"
  },
  {
    "country": "Australia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4370,
      "deaths": 53,
      "recovered": 3143
    },
    "coordinates": {
      "latitude": "-33.8688",
      "longitude": "151.2093"
    },
    "province": "New South Wales"
  },
  {
    "country": "Australia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 33,
      "deaths": 0,
      "recovered": 33
    },
    "coordinates": {
      "latitude": "-12.4634",
      "longitude": "130.8456"
    },
    "province": "Northern Territory"
  },
  {
    "country": "Australia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1167,
      "deaths": 6,
      "recovered": 1155
    },
    "coordinates": {
      "latitude": "-27.4698",
      "longitude": "153.0251"
    },
    "province": "Queensland"
  },
  {
    "country": "Australia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 485,
      "deaths": 4,
      "recovered": 473
    },
    "coordinates": {
      "latitude": "-34.9285",
      "longitude": "138.6007"
    },
    "province": "South Australia"
  },
  {
    "country": "Australia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 230,
      "deaths": 13,
      "recovered": 217
    },
    "coordinates": {
      "latitude": "-42.8821",
      "longitude": "147.3272"
    },
    "province": "Tasmania"
  },
  {
    "country": "Australia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20330,
      "deaths": 817,
      "recovered": 19340
    },
    "coordinates": {
      "latitude": "-37.8136",
      "longitude": "144.9631"
    },
    "province": "Victoria"
  },
  {
    "country": "Australia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 747,
      "deaths": 9,
      "recovered": 690
    },
    "coordinates": {
      "latitude": "-31.9505",
      "longitude": "115.8605"
    },
    "province": "Western Australia"
  },
  {
    "country": "Austria",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 71844,
      "deaths": 941,
      "recovered": 53970
    },
    "coordinates": {
      "latitude": "47.5162",
      "longitude": "14.5501"
    },
    "province": null
  },
  {
    "country": "Azerbaijan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 47418,
      "deaths": 648,
      "recovered": 40619
    },
    "coordinates": {
      "latitude": "40.1431",
      "longitude": "47.5769"
    },
    "province": null
  },
  {
    "country": "Bahamas",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6135,
      "deaths": 130,
      "recovered": 3705
    },
    "coordinates": {
      "latitude": "25.025885",
      "longitude": "-78.035889"
    },
    "province": null
  },
  {
    "country": "Bahrain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 79211,
      "deaths": 308,
      "recovered": 75840
    },
    "coordinates": {
      "latitude": "26.0275",
      "longitude": "50.55"
    },
    "province": null
  },
  {
    "country": "Bangladesh",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 394827,
      "deaths": 5747,
      "recovered": 310532
    },
    "coordinates": {
      "latitude": "23.685",
      "longitude": "90.3563"
    },
    "province": null
  },
  {
    "country": "Barbados",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 224,
      "deaths": 7,
      "recovered": 207
    },
    "coordinates": {
      "latitude": "13.1939",
      "longitude": "-59.5432"
    },
    "province": null
  },
  {
    "country": "Belarus",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 90380,
      "deaths": 945,
      "recovered": 81501
    },
    "coordinates": {
      "latitude": "53.7098",
      "longitude": "27.9534"
    },
    "province": null
  },
  {
    "country": "Belgium",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 270132,
      "deaths": 10588,
      "recovered": 22213
    },
    "coordinates": {
      "latitude": "50.8333",
      "longitude": "4.469936"
    },
    "province": null
  },
  {
    "country": "Belize",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2995,
      "deaths": 46,
      "recovered": 1826
    },
    "coordinates": {
      "latitude": "17.1899",
      "longitude": "-88.4976"
    },
    "province": null
  },
  {
    "country": "Benin",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2557,
      "deaths": 41,
      "recovered": 2330
    },
    "coordinates": {
      "latitude": "9.3077",
      "longitude": "2.3158"
    },
    "province": null
  },
  {
    "country": "Bhutan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 336,
      "deaths": 0,
      "recovered": 306
    },
    "coordinates": {
      "latitude": "27.5142",
      "longitude": "90.4336"
    },
    "province": null
  },
  {
    "country": "Bolivia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 140445,
      "deaths": 8584,
      "recovered": 106950
    },
    "coordinates": {
      "latitude": "-16.2902",
      "longitude": "-63.5887"
    },
    "province": null
  },
  {
    "country": "Bosnia and Herzegovina",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 37314,
      "deaths": 1051,
      "recovered": 25989
    },
    "coordinates": {
      "latitude": "43.9159",
      "longitude": "17.6791"
    },
    "province": null
  },
  {
    "country": "Botswana",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5923,
      "deaths": 21,
      "recovered": 927
    },
    "coordinates": {
      "latitude": "-22.3285",
      "longitude": "24.6849"
    },
    "province": null
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 30028,
      "deaths": 685,
      "recovered": 27176
    },
    "coordinates": {
      "latitude": "-9.0238",
      "longitude": "-70.812"
    },
    "province": "Acre"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 89847,
      "deaths": 2196,
      "recovered": 85557
    },
    "coordinates": {
      "latitude": "-9.5713",
      "longitude": "-36.782"
    },
    "province": "Alagoas"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 50822,
      "deaths": 738,
      "recovered": 36905
    },
    "coordinates": {
      "latitude": "0.902",
      "longitude": "-52.003"
    },
    "province": "Amapa"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 155230,
      "deaths": 4396,
      "recovered": 120012
    },
    "coordinates": {
      "latitude": "-3.4168",
      "longitude": "-65.8561"
    },
    "province": "Amazonas"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 340665,
      "deaths": 7407,
      "recovered": 311054
    },
    "coordinates": {
      "latitude": "-12.5797",
      "longitude": "-41.7007"
    },
    "province": "Bahia"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 268274,
      "deaths": 9243,
      "recovered": 223281
    },
    "coordinates": {
      "latitude": "-5.4984",
      "longitude": "-39.3206"
    },
    "province": "Ceara"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 207670,
      "deaths": 3600,
      "recovered": 189807
    },
    "coordinates": {
      "latitude": "-15.7998",
      "longitude": "-47.8645"
    },
    "province": "Distrito Federal"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 147898,
      "deaths": 3759,
      "recovered": 127835
    },
    "coordinates": {
      "latitude": "-19.1834",
      "longitude": "-40.3089"
    },
    "province": "Espirito Santo"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 243243,
      "deaths": 5491,
      "recovered": 218177
    },
    "coordinates": {
      "latitude": "-15.827",
      "longitude": "-49.8362"
    },
    "province": "Goias"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 182944,
      "deaths": 3968,
      "recovered": 167126
    },
    "coordinates": {
      "latitude": "-4.9609",
      "longitude": "-45.2744"
    },
    "province": "Maranhao"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 138178,
      "deaths": 3711,
      "recovered": 112218
    },
    "coordinates": {
      "latitude": "-12.6819",
      "longitude": "-56.9211"
    },
    "province": "Mato Grosso"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 78710,
      "deaths": 1524,
      "recovered": 68629
    },
    "coordinates": {
      "latitude": "-20.7722",
      "longitude": "-54.7852"
    },
    "province": "Mato Grosso do Sul"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 343159,
      "deaths": 8621,
      "recovered": 286280
    },
    "coordinates": {
      "latitude": "-18.5122",
      "longitude": "-44.555"
    },
    "province": "Minas Gerais"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 244229,
      "deaths": 6697,
      "recovered": 221997
    },
    "coordinates": {
      "latitude": "-1.9981",
      "longitude": "-54.9306"
    },
    "province": "Para"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 129731,
      "deaths": 3029,
      "recovered": 101073
    },
    "coordinates": {
      "latitude": "-7.24",
      "longitude": "-36.782"
    },
    "province": "Paraiba"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 204326,
      "deaths": 5047,
      "recovered": 140100
    },
    "coordinates": {
      "latitude": "-25.2521",
      "longitude": "-52.0215"
    },
    "province": "Parana"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 157777,
      "deaths": 8527,
      "recovered": 131135
    },
    "coordinates": {
      "latitude": "-8.8137",
      "longitude": "-36.9541"
    },
    "province": "Pernambuco"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 108346,
      "deaths": 2322,
      "recovered": 99255
    },
    "coordinates": {
      "latitude": "-7.7183",
      "longitude": "-42.7289"
    },
    "province": "Piaui"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 79371,
      "deaths": 2558,
      "recovered": 42040
    },
    "coordinates": {
      "latitude": "-5.4026",
      "longitude": "-36.9541"
    },
    "province": "Rio Grande do Norte"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 228762,
      "deaths": 5518,
      "recovered": 198688
    },
    "coordinates": {
      "latitude": "-30.0346",
      "longitude": "-51.2177"
    },
    "province": "Rio Grande do Sul"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 295021,
      "deaths": 20021,
      "recovered": 258928
    },
    "coordinates": {
      "latitude": "-22.9068",
      "longitude": "-43.1729"
    },
    "province": "Rio de Janeiro"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 69806,
      "deaths": 1430,
      "recovered": 60189
    },
    "coordinates": {
      "latitude": "-11.5057",
      "longitude": "-63.5806"
    },
    "province": "Rondonia"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 54905,
      "deaths": 690,
      "recovered": 48508
    },
    "coordinates": {
      "latitude": "-2.7376",
      "longitude": "-62.0751"
    },
    "province": "Roraima"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 241044,
      "deaths": 3011,
      "recovered": 213495
    },
    "coordinates": {
      "latitude": "-27.2423",
      "longitude": "-50.2189"
    },
    "province": "Santa Catarina"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1076939,
      "deaths": 38482,
      "recovered": 908199
    },
    "coordinates": {
      "latitude": "-23.5505",
      "longitude": "-46.6333"
    },
    "province": "Sao Paulo"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 83139,
      "deaths": 2157,
      "recovered": 73030
    },
    "coordinates": {
      "latitude": "-10.5741",
      "longitude": "-37.3857"
    },
    "province": "Sergipe"
  },
  {
    "country": "Brazil",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 73566,
      "deaths": 1072,
      "recovered": 55699
    },
    "coordinates": {
      "latitude": "-10.1753",
      "longitude": "-48.2982"
    },
    "province": "Tocantins"
  },
  {
    "country": "Brunei",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 148,
      "deaths": 3,
      "recovered": 143
    },
    "coordinates": {
      "latitude": "4.5353",
      "longitude": "114.7277"
    },
    "province": null
  },
  {
    "country": "Bulgaria",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 34930,
      "deaths": 1064,
      "recovered": 17833
    },
    "coordinates": {
      "latitude": "42.7339",
      "longitude": "25.4858"
    },
    "province": null
  },
  {
    "country": "Burkina Faso",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2414,
      "deaths": 65,
      "recovered": 1869
    },
    "coordinates": {
      "latitude": "12.2383",
      "longitude": "-1.5616"
    },
    "province": null
  },
  {
    "country": "Burma",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 41008,
      "deaths": 1005,
      "recovered": 21144
    },
    "coordinates": {
      "latitude": "21.9162",
      "longitude": "95.956"
    },
    "province": null
  },
  {
    "country": "Burundi",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 551,
      "deaths": 1,
      "recovered": 497
    },
    "coordinates": {
      "latitude": "-3.3731",
      "longitude": "29.9189"
    },
    "province": null
  },
  {
    "country": "Cabo Verde",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8122,
      "deaths": 91,
      "recovered": 6940
    },
    "coordinates": {
      "latitude": "16.5388",
      "longitude": "-23.0418"
    },
    "province": null
  },
  {
    "country": "Cambodia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 286,
      "deaths": 0,
      "recovered": 280
    },
    "coordinates": {
      "latitude": "11.55",
      "longitude": "104.9167"
    },
    "province": null
  },
  {
    "country": "Cameroon",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 21570,
      "deaths": 425,
      "recovered": 20117
    },
    "coordinates": {
      "latitude": "3.848",
      "longitude": "11.5021"
    },
    "province": null
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 23829,
      "deaths": 296,
      "recovered": 20014
    },
    "coordinates": {
      "latitude": "53.9333",
      "longitude": "-116.5765"
    },
    "province": "Alberta"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12057,
      "deaths": 256,
      "recovered": 4931
    },
    "coordinates": {
      "latitude": "53.7267",
      "longitude": "-127.6476"
    },
    "province": "British Columbia"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 0,
      "deaths": 1,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Diamond Princess"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13,
      "deaths": 0,
      "recovered": 13
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Grand Princess"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3773,
      "deaths": 47,
      "recovered": 1920
    },
    "coordinates": {
      "latitude": "53.7609",
      "longitude": "-98.8139"
    },
    "province": "Manitoba"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 322,
      "deaths": 4,
      "recovered": 237
    },
    "coordinates": {
      "latitude": "46.5653",
      "longitude": "-66.4619"
    },
    "province": "New Brunswick"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 288,
      "deaths": 4,
      "recovered": 276
    },
    "coordinates": {
      "latitude": "53.1355",
      "longitude": "-57.6604"
    },
    "province": "Newfoundland and Labrador"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8,
      "deaths": 0,
      "recovered": 5
    },
    "coordinates": {
      "latitude": "64.8255",
      "longitude": "-124.8457"
    },
    "province": "Northwest Territories"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1097,
      "deaths": 65,
      "recovered": 1028
    },
    "coordinates": {
      "latitude": "44.682",
      "longitude": "-63.7443"
    },
    "province": "Nova Scotia"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 70270,
      "deaths": 3124,
      "recovered": 60742
    },
    "coordinates": {
      "latitude": "51.2538",
      "longitude": "-85.3232"
    },
    "province": "Ontario"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 64,
      "deaths": 0,
      "recovered": 61
    },
    "coordinates": {
      "latitude": "46.5107",
      "longitude": "-63.4168"
    },
    "province": "Prince Edward Island"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 97321,
      "deaths": 6094,
      "recovered": 82033
    },
    "coordinates": {
      "latitude": "52.9399",
      "longitude": "-73.5491"
    },
    "province": "Quebec"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2558,
      "deaths": 25,
      "recovered": 2024
    },
    "coordinates": {
      "latitude": "52.9399",
      "longitude": "-106.4509"
    },
    "province": "Saskatchewan"
  },
  {
    "country": "Canada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17,
      "deaths": 0,
      "recovered": 15
    },
    "coordinates": {
      "latitude": "64.2823",
      "longitude": "-135.0"
    },
    "province": "Yukon"
  },
  {
    "country": "Central African Republic",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4862,
      "deaths": 62,
      "recovered": 1924
    },
    "coordinates": {
      "latitude": "6.6111",
      "longitude": "20.9394"
    },
    "province": null
  },
  {
    "country": "Chad",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1410,
      "deaths": 96,
      "recovered": 1223
    },
    "coordinates": {
      "latitude": "15.4542",
      "longitude": "18.7322"
    },
    "province": null
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 21002,
      "deaths": 522,
      "recovered": 20055
    },
    "coordinates": {
      "latitude": "-23.6509",
      "longitude": "-70.3975"
    },
    "province": "Antofagasta"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10688,
      "deaths": 138,
      "recovered": 9375
    },
    "coordinates": {
      "latitude": "-38.9489",
      "longitude": "-72.3311"
    },
    "province": "Araucania"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9256,
      "deaths": 174,
      "recovered": 8641
    },
    "coordinates": {
      "latitude": "-18.594",
      "longitude": "-69.4785"
    },
    "province": "Arica y Parinacota"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7670,
      "deaths": 83,
      "recovered": 7338
    },
    "coordinates": {
      "latitude": "-27.5661",
      "longitude": "-70.0503"
    },
    "province": "Atacama"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 929,
      "deaths": 2,
      "recovered": 737
    },
    "coordinates": {
      "latitude": "-45.9864",
      "longitude": "-73.7669"
    },
    "province": "Aysen"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 27732,
      "deaths": 432,
      "recovered": 25310
    },
    "coordinates": {
      "latitude": "-37.4464",
      "longitude": "-72.1416"
    },
    "province": "Biobio"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12544,
      "deaths": 238,
      "recovered": 12125
    },
    "coordinates": {
      "latitude": "-29.959",
      "longitude": "-71.3389"
    },
    "province": "Coquimbo"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13077,
      "deaths": 116,
      "recovered": 11296
    },
    "coordinates": {
      "latitude": "-41.9198",
      "longitude": "-72.1416"
    },
    "province": "Los Lagos"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2919,
      "deaths": 29,
      "recovered": 2433
    },
    "coordinates": {
      "latitude": "-40.231",
      "longitude": "-72.3311"
    },
    "province": "Los Rios"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11621,
      "deaths": 119,
      "recovered": 10765
    },
    "coordinates": {
      "latitude": "-52.368",
      "longitude": "-70.9863"
    },
    "province": "Magallanes"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18086,
      "deaths": 390,
      "recovered": 16828
    },
    "coordinates": {
      "latitude": "-35.5183",
      "longitude": "-71.6885"
    },
    "province": "Maule"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 294031,
      "deaths": 9686,
      "recovered": 281237
    },
    "coordinates": {
      "latitude": "-33.4376",
      "longitude": "-70.6505"
    },
    "province": "Metropolitana"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7116,
      "deaths": 140,
      "recovered": 6687
    },
    "coordinates": {
      "latitude": "-36.7226",
      "longitude": "-71.7622"
    },
    "province": "Nuble"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18187,
      "deaths": 480,
      "recovered": 17018
    },
    "coordinates": {
      "latitude": "-34.5755",
      "longitude": "-71.0022"
    },
    "province": "OHiggins"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12542,
      "deaths": 240,
      "recovered": 11987
    },
    "coordinates": {
      "latitude": "-19.9232",
      "longitude": "-69.5132"
    },
    "province": "Tarapaca"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 50,
      "deaths": 1,
      "recovered": 50
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "Chile",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 29681,
      "deaths": 1002,
      "recovered": 27883
    },
    "coordinates": {
      "latitude": "-33.0472",
      "longitude": "-71.6127"
    },
    "province": "Valparaiso"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 991,
      "deaths": 6,
      "recovered": 985
    },
    "coordinates": {
      "latitude": "31.8257",
      "longitude": "117.2264"
    },
    "province": "Anhui"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 938,
      "deaths": 9,
      "recovered": 928
    },
    "coordinates": {
      "latitude": "40.1824",
      "longitude": "116.4142"
    },
    "province": "Beijing"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 589,
      "deaths": 6,
      "recovered": 579
    },
    "coordinates": {
      "latitude": "30.0572",
      "longitude": "107.874"
    },
    "province": "Chongqing"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 427,
      "deaths": 1,
      "recovered": 409
    },
    "coordinates": {
      "latitude": "26.0789",
      "longitude": "117.9874"
    },
    "province": "Fujian"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 170,
      "deaths": 2,
      "recovered": 168
    },
    "coordinates": {
      "latitude": "35.7518",
      "longitude": "104.2861"
    },
    "province": "Gansu"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1895,
      "deaths": 8,
      "recovered": 1851
    },
    "coordinates": {
      "latitude": "23.3417",
      "longitude": "113.4244"
    },
    "province": "Guangdong"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 260,
      "deaths": 2,
      "recovered": 258
    },
    "coordinates": {
      "latitude": "23.8298",
      "longitude": "108.7881"
    },
    "province": "Guangxi"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 147,
      "deaths": 2,
      "recovered": 145
    },
    "coordinates": {
      "latitude": "26.8154",
      "longitude": "106.8748"
    },
    "province": "Guizhou"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 171,
      "deaths": 6,
      "recovered": 165
    },
    "coordinates": {
      "latitude": "19.1959",
      "longitude": "109.7453"
    },
    "province": "Hainan"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 368,
      "deaths": 6,
      "recovered": 359
    },
    "coordinates": {
      "latitude": "37.8957",
      "longitude": "114.9042"
    },
    "province": "Hebei"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 948,
      "deaths": 13,
      "recovered": 935
    },
    "coordinates": {
      "latitude": "47.862",
      "longitude": "127.7615"
    },
    "province": "Heilongjiang"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1283,
      "deaths": 22,
      "recovered": 1257
    },
    "coordinates": {
      "latitude": "33.882",
      "longitude": "113.614"
    },
    "province": "Henan"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5280,
      "deaths": 105,
      "recovered": 5019
    },
    "coordinates": {
      "latitude": "22.3",
      "longitude": "114.2"
    },
    "province": "Hong Kong"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 68139,
      "deaths": 4512,
      "recovered": 63627
    },
    "coordinates": {
      "latitude": "30.9756",
      "longitude": "112.2707"
    },
    "province": "Hubei"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1019,
      "deaths": 4,
      "recovered": 1015
    },
    "coordinates": {
      "latitude": "27.6104",
      "longitude": "111.7088"
    },
    "province": "Hunan"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 275,
      "deaths": 1,
      "recovered": 266
    },
    "coordinates": {
      "latitude": "44.0935",
      "longitude": "113.9448"
    },
    "province": "Inner Mongolia"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 670,
      "deaths": 0,
      "recovered": 665
    },
    "coordinates": {
      "latitude": "32.9711",
      "longitude": "119.455"
    },
    "province": "Jiangsu"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 935,
      "deaths": 1,
      "recovered": 934
    },
    "coordinates": {
      "latitude": "27.614",
      "longitude": "115.7221"
    },
    "province": "Jiangxi"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 157,
      "deaths": 2,
      "recovered": 155
    },
    "coordinates": {
      "latitude": "43.6661",
      "longitude": "126.1923"
    },
    "province": "Jilin"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 280,
      "deaths": 2,
      "recovered": 271
    },
    "coordinates": {
      "latitude": "41.2956",
      "longitude": "122.6085"
    },
    "province": "Liaoning"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 46,
      "deaths": 0,
      "recovered": 46
    },
    "coordinates": {
      "latitude": "22.1667",
      "longitude": "113.55"
    },
    "province": "Macau"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 75,
      "deaths": 0,
      "recovered": 75
    },
    "coordinates": {
      "latitude": "37.2692",
      "longitude": "106.1655"
    },
    "province": "Ningxia"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18,
      "deaths": 0,
      "recovered": 18
    },
    "coordinates": {
      "latitude": "35.7452",
      "longitude": "95.9956"
    },
    "province": "Qinghai"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 438,
      "deaths": 3,
      "recovered": 414
    },
    "coordinates": {
      "latitude": "35.1917",
      "longitude": "108.8701"
    },
    "province": "Shaanxi"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 845,
      "deaths": 7,
      "recovered": 827
    },
    "coordinates": {
      "latitude": "36.3427",
      "longitude": "118.1498"
    },
    "province": "Shandong"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1114,
      "deaths": 7,
      "recovered": 1028
    },
    "coordinates": {
      "latitude": "31.202",
      "longitude": "121.4491"
    },
    "province": "Shanghai"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 209,
      "deaths": 0,
      "recovered": 204
    },
    "coordinates": {
      "latitude": "37.5777",
      "longitude": "112.2922"
    },
    "province": "Shanxi"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 733,
      "deaths": 3,
      "recovered": 701
    },
    "coordinates": {
      "latitude": "30.6171",
      "longitude": "102.7103"
    },
    "province": "Sichuan"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 256,
      "deaths": 3,
      "recovered": 242
    },
    "coordinates": {
      "latitude": "39.3054",
      "longitude": "117.323"
    },
    "province": "Tianjin"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1,
      "deaths": 0,
      "recovered": 1
    },
    "coordinates": {
      "latitude": "31.6927",
      "longitude": "88.0924"
    },
    "province": "Tibet"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 902,
      "deaths": 3,
      "recovered": 899
    },
    "coordinates": {
      "latitude": "41.1129",
      "longitude": "85.2401"
    },
    "province": "Xinjiang"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 211,
      "deaths": 2,
      "recovered": 204
    },
    "coordinates": {
      "latitude": "24.974",
      "longitude": "101.487"
    },
    "province": "Yunnan"
  },
  {
    "country": "China",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1283,
      "deaths": 1,
      "recovered": 1279
    },
    "coordinates": {
      "latitude": "29.1832",
      "longitude": "120.0934"
    },
    "province": "Zhejiang"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2876,
      "deaths": 117,
      "recovered": 2738
    },
    "coordinates": {
      "latitude": "-1.4429",
      "longitude": "-71.5724"
    },
    "province": "Amazonas"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 149191,
      "deaths": 2940,
      "recovered": 137659
    },
    "coordinates": {
      "latitude": "7.1986",
      "longitude": "-75.3412"
    },
    "province": "Antioquia"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2742,
      "deaths": 83,
      "recovered": 2435
    },
    "coordinates": {
      "latitude": "7.0762",
      "longitude": "-70.7105"
    },
    "province": "Arauca"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 70288,
      "deaths": 3113,
      "recovered": 65982
    },
    "coordinates": {
      "latitude": "10.6966",
      "longitude": "-74.8741"
    },
    "province": "Atlantico"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 31708,
      "deaths": 823,
      "recovered": 30285
    },
    "coordinates": {
      "latitude": "8.6704",
      "longitude": "-74.03"
    },
    "province": "Bolivar"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11710,
      "deaths": 247,
      "recovered": 9984
    },
    "coordinates": {
      "latitude": "5.4545",
      "longitude": "-73.362"
    },
    "province": "Boyaca"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10405,
      "deaths": 223,
      "recovered": 8442
    },
    "coordinates": {
      "latitude": "5.2983",
      "longitude": "-75.2479"
    },
    "province": "Caldas"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 304567,
      "deaths": 7404,
      "recovered": 271761
    },
    "coordinates": {
      "latitude": "4.711",
      "longitude": "-74.0721"
    },
    "province": "Capital District"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10587,
      "deaths": 374,
      "recovered": 9373
    },
    "coordinates": {
      "latitude": "0.8699",
      "longitude": "-73.8419"
    },
    "province": "Caqueta"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4196,
      "deaths": 72,
      "recovered": 3290
    },
    "coordinates": {
      "latitude": "5.7589",
      "longitude": "-71.5724"
    },
    "province": "Casanare"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12175,
      "deaths": 343,
      "recovered": 10741
    },
    "coordinates": {
      "latitude": "2.705",
      "longitude": "-76.82600000000002"
    },
    "province": "Cauca"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 24108,
      "deaths": 756,
      "recovered": 21598
    },
    "coordinates": {
      "latitude": "9.3373",
      "longitude": "-73.6536"
    },
    "province": "Cesar"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4122,
      "deaths": 160,
      "recovered": 3870
    },
    "coordinates": {
      "latitude": "5.2528",
      "longitude": "-76.82600000000002"
    },
    "province": "Choco"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 25753,
      "deaths": 1608,
      "recovered": 23146
    },
    "coordinates": {
      "latitude": "8.0493",
      "longitude": "-75.574"
    },
    "province": "Cordoba"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 39568,
      "deaths": 1144,
      "recovered": 36243
    },
    "coordinates": {
      "latitude": "5.026",
      "longitude": "-74.03"
    },
    "province": "Cundinamarca"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1097,
      "deaths": 18,
      "recovered": 1047
    },
    "coordinates": {
      "latitude": "2.5854",
      "longitude": "-68.5247"
    },
    "province": "Guainia"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1307,
      "deaths": 21,
      "recovered": 1173
    },
    "coordinates": {
      "latitude": "1.0654",
      "longitude": "-73.2603"
    },
    "province": "Guaviare"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18950,
      "deaths": 546,
      "recovered": 16416
    },
    "coordinates": {
      "latitude": "2.5359",
      "longitude": "-75.5277"
    },
    "province": "Huila"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9386,
      "deaths": 381,
      "recovered": 8576
    },
    "coordinates": {
      "latitude": "11.3548",
      "longitude": "-72.5205"
    },
    "province": "La Guajira"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16685,
      "deaths": 877,
      "recovered": 15094
    },
    "coordinates": {
      "latitude": "10.4113",
      "longitude": "-74.4057"
    },
    "province": "Magdalena"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20772,
      "deaths": 490,
      "recovered": 19082
    },
    "coordinates": {
      "latitude": "3.272",
      "longitude": "-73.0877"
    },
    "province": "Meta"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20728,
      "deaths": 747,
      "recovered": 18783
    },
    "coordinates": {
      "latitude": "1.2892",
      "longitude": "-77.3579"
    },
    "province": "Narino"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 19446,
      "deaths": 1018,
      "recovered": 17450
    },
    "coordinates": {
      "latitude": "7.9463",
      "longitude": "-72.8988"
    },
    "province": "Norte de Santander"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4224,
      "deaths": 196,
      "recovered": 3747
    },
    "coordinates": {
      "latitude": "0.436",
      "longitude": "-75.5277"
    },
    "province": "Putumayo"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7642,
      "deaths": 193,
      "recovered": 6208
    },
    "coordinates": {
      "latitude": "4.461",
      "longitude": "-75.6674"
    },
    "province": "Quindio"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15488,
      "deaths": 345,
      "recovered": 13723
    },
    "coordinates": {
      "latitude": "5.3158",
      "longitude": "-75.9928"
    },
    "province": "Risaralda"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1806,
      "deaths": 29,
      "recovered": 1703
    },
    "coordinates": {
      "latitude": "12.5567",
      "longitude": "-81.7185"
    },
    "province": "San Andres y Providencia"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 38814,
      "deaths": 1580,
      "recovered": 34187
    },
    "coordinates": {
      "latitude": "6.6437",
      "longitude": "-73.6536"
    },
    "province": "Santander"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15205,
      "deaths": 606,
      "recovered": 14125
    },
    "coordinates": {
      "latitude": "8.814",
      "longitude": "-74.7233"
    },
    "province": "Sucre"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16678,
      "deaths": 518,
      "recovered": 14673
    },
    "coordinates": {
      "latitude": "4.0925",
      "longitude": "-75.1545"
    },
    "province": "Tolima"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 0,
      "deaths": 0,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 76407,
      "deaths": 2644,
      "recovered": 68588
    },
    "coordinates": {
      "latitude": "3.8009",
      "longitude": "-76.6413"
    },
    "province": "Valle del Cauca"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 992,
      "deaths": 12,
      "recovered": 961
    },
    "coordinates": {
      "latitude": "0.8554",
      "longitude": "-70.812"
    },
    "province": "Vaupes"
  },
  {
    "country": "Colombia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 750,
      "deaths": 9,
      "recovered": 727
    },
    "coordinates": {
      "latitude": "4.4234",
      "longitude": "-69.2878"
    },
    "province": "Vichada"
  },
  {
    "country": "Comoros",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 517,
      "deaths": 7,
      "recovered": 494
    },
    "coordinates": {
      "latitude": "-11.6455",
      "longitude": "43.3333"
    },
    "province": null
  },
  {
    "country": "Congo (Brazzaville)",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5156,
      "deaths": 92,
      "recovered": 3887
    },
    "coordinates": {
      "latitude": "-0.228",
      "longitude": "15.8277"
    },
    "province": null
  },
  {
    "country": "Congo (Kinshasa)",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11097,
      "deaths": 304,
      "recovered": 10379
    },
    "coordinates": {
      "latitude": "-4.0383",
      "longitude": "21.7587"
    },
    "province": null
  },
  {
    "country": "Costa Rica",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 100616,
      "deaths": 1251,
      "recovered": 61162
    },
    "coordinates": {
      "latitude": "9.7489",
      "longitude": "-83.7534"
    },
    "province": null
  },
  {
    "country": "Cote d'Ivoire",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20390,
      "deaths": 121,
      "recovered": 20088
    },
    "coordinates": {
      "latitude": "7.54",
      "longitude": "-5.5471"
    },
    "province": null
  },
  {
    "country": "Croatia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 29850,
      "deaths": 406,
      "recovered": 22064
    },
    "coordinates": {
      "latitude": "45.1",
      "longitude": "15.2"
    },
    "province": null
  },
  {
    "country": "Cuba",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6421,
      "deaths": 128,
      "recovered": 5871
    },
    "coordinates": {
      "latitude": "21.521757",
      "longitude": "-77.78116700000002"
    },
    "province": null
  },
  {
    "country": "Cyprus",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3154,
      "deaths": 25,
      "recovered": 1444
    },
    "coordinates": {
      "latitude": "35.1264",
      "longitude": "33.4299"
    },
    "province": null
  },
  {
    "country": "Czechia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 223065,
      "deaths": 1845,
      "recovered": 87225
    },
    "coordinates": {
      "latitude": "49.8175",
      "longitude": "15.473"
    },
    "province": null
  },
  {
    "country": "Denmark",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 490,
      "deaths": 0,
      "recovered": 473
    },
    "coordinates": {
      "latitude": "61.8926",
      "longitude": "-6.9118"
    },
    "province": "Faroe Islands"
  },
  {
    "country": "Denmark",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17,
      "deaths": 0,
      "recovered": 16
    },
    "coordinates": {
      "latitude": "71.7069",
      "longitude": "-42.6043"
    },
    "province": "Greenland"
  },
  {
    "country": "Denmark",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 37763,
      "deaths": 694,
      "recovered": 30877
    },
    "coordinates": {
      "latitude": "56.2639",
      "longitude": "9.5018"
    },
    "province": null
  },
  {
    "country": "Diamond Princess",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 712,
      "deaths": 13,
      "recovered": 659
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": null
  },
  {
    "country": "Djibouti",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5522,
      "deaths": 61,
      "recovered": 5389
    },
    "coordinates": {
      "latitude": "11.8251",
      "longitude": "42.5903"
    },
    "province": null
  },
  {
    "country": "Dominica",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 33,
      "deaths": 0,
      "recovered": 29
    },
    "coordinates": {
      "latitude": "15.415",
      "longitude": "-61.371"
    },
    "province": null
  },
  {
    "country": "Dominican Republic",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 122873,
      "deaths": 2212,
      "recovered": 100920
    },
    "coordinates": {
      "latitude": "18.7357",
      "longitude": "-70.1627"
    },
    "province": null
  },
  {
    "country": "Ecuador",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 156451,
      "deaths": 12500,
      "recovered": 134187
    },
    "coordinates": {
      "latitude": "-1.8312",
      "longitude": "-78.1834"
    },
    "province": null
  },
  {
    "country": "Egypt",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 106060,
      "deaths": 6166,
      "recovered": 98624
    },
    "coordinates": {
      "latitude": "26.820553000000004",
      "longitude": "30.802498"
    },
    "province": null
  },
  {
    "country": "El Salvador",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 32262,
      "deaths": 936,
      "recovered": 27904
    },
    "coordinates": {
      "latitude": "13.7942",
      "longitude": "-88.8965"
    },
    "province": null
  },
  {
    "country": "Equatorial Guinea",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5074,
      "deaths": 83,
      "recovered": 4961
    },
    "coordinates": {
      "latitude": "1.6508",
      "longitude": "10.2679"
    },
    "province": null
  },
  {
    "country": "Eritrea",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 457,
      "deaths": 0,
      "recovered": 391
    },
    "coordinates": {
      "latitude": "15.1794",
      "longitude": "39.7823"
    },
    "province": null
  },
  {
    "country": "Estonia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4247,
      "deaths": 71,
      "recovered": 3366
    },
    "coordinates": {
      "latitude": "58.5953",
      "longitude": "25.0136"
    },
    "province": null
  },
  {
    "country": "Eswatini",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5814,
      "deaths": 116,
      "recovered": 5468
    },
    "coordinates": {
      "latitude": "-26.5225",
      "longitude": "31.4659"
    },
    "province": null
  },
  {
    "country": "Ethiopia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 91693,
      "deaths": 1396,
      "recovered": 45260
    },
    "coordinates": {
      "latitude": "9.145",
      "longitude": "40.4897"
    },
    "province": null
  },
  {
    "country": "Fiji",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 33,
      "deaths": 2,
      "recovered": 30
    },
    "coordinates": {
      "latitude": "-17.7134",
      "longitude": "178.065"
    },
    "province": null
  },
  {
    "country": "Finland",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 14255,
      "deaths": 355,
      "recovered": 9800
    },
    "coordinates": {
      "latitude": "61.92411",
      "longitude": "25.748151"
    },
    "province": null
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10342,
      "deaths": 69,
      "recovered": 9995
    },
    "coordinates": {
      "latitude": "4.0",
      "longitude": "-53.0"
    },
    "province": "French Guiana"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5161,
      "deaths": 19,
      "recovered": 3536
    },
    "coordinates": {
      "latitude": "-17.6797",
      "longitude": "-149.4068"
    },
    "province": "French Polynesia"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7329,
      "deaths": 115,
      "recovered": 2199
    },
    "coordinates": {
      "latitude": "16.265",
      "longitude": "-61.551"
    },
    "province": "Guadeloupe"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2257,
      "deaths": 24,
      "recovered": 98
    },
    "coordinates": {
      "latitude": "14.6415",
      "longitude": "-61.0242"
    },
    "province": "Martinique"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4203,
      "deaths": 44,
      "recovered": 2964
    },
    "coordinates": {
      "latitude": "-12.8275",
      "longitude": "45.166244"
    },
    "province": "Mayotte"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 27,
      "deaths": 0,
      "recovered": 27
    },
    "coordinates": {
      "latitude": "-20.904305",
      "longitude": "165.618042"
    },
    "province": "New Caledonia"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5015,
      "deaths": 19,
      "recovered": 4445
    },
    "coordinates": {
      "latitude": "-21.1151",
      "longitude": "55.5364"
    },
    "province": "Reunion"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 77,
      "deaths": 0,
      "recovered": 66
    },
    "coordinates": {
      "latitude": "17.9",
      "longitude": "-62.8333"
    },
    "province": "Saint Barthelemy"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16,
      "deaths": 0,
      "recovered": 12
    },
    "coordinates": {
      "latitude": "46.8852",
      "longitude": "-56.3159"
    },
    "province": "Saint Pierre and Miquelon"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 538,
      "deaths": 8,
      "recovered": 422
    },
    "coordinates": {
      "latitude": "18.0708",
      "longitude": "-63.0501"
    },
    "province": "St Martin"
  },
  {
    "country": "France",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1007026,
      "deaths": 33939,
      "recovered": 88898
    },
    "coordinates": {
      "latitude": "46.2276",
      "longitude": "2.2137"
    },
    "province": null
  },
  {
    "country": "Gabon",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8901,
      "deaths": 54,
      "recovered": 8479
    },
    "coordinates": {
      "latitude": "-0.8037",
      "longitude": "11.6094"
    },
    "province": null
  },
  {
    "country": "Gambia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3659,
      "deaths": 119,
      "recovered": 2660
    },
    "coordinates": {
      "latitude": "13.4432",
      "longitude": "-15.3101"
    },
    "province": null
  },
  {
    "country": "Georgia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 22803,
      "deaths": 178,
      "recovered": 9401
    },
    "coordinates": {
      "latitude": "42.3154",
      "longitude": "43.3569"
    },
    "province": null
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 65085,
      "deaths": 1957,
      "recovered": 51191
    },
    "coordinates": {
      "latitude": "48.6616",
      "longitude": "9.3501"
    },
    "province": "Baden-Wurttemberg"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 86054,
      "deaths": 2734,
      "recovered": 69028
    },
    "coordinates": {
      "latitude": "48.7904",
      "longitude": "11.4979"
    },
    "province": "Bayern"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 24481,
      "deaths": 245,
      "recovered": 17736
    },
    "coordinates": {
      "latitude": "52.52",
      "longitude": "13.405"
    },
    "province": "Berlin"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6144,
      "deaths": 185,
      "recovered": 4807
    },
    "coordinates": {
      "latitude": "52.4125",
      "longitude": "12.5316"
    },
    "province": "Brandenburg"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4020,
      "deaths": 63,
      "recovered": 2683
    },
    "coordinates": {
      "latitude": "53.0793",
      "longitude": "8.8017"
    },
    "province": "Bremen"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10683,
      "deaths": 283,
      "recovered": 8102
    },
    "coordinates": {
      "latitude": "53.5511",
      "longitude": "9.9937"
    },
    "province": "Hamburg"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 29398,
      "deaths": 600,
      "recovered": 21146
    },
    "coordinates": {
      "latitude": "50.6521",
      "longitude": "9.1624"
    },
    "province": "Hessen"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1946,
      "deaths": 21,
      "recovered": 1419
    },
    "coordinates": {
      "latitude": "53.6127",
      "longitude": "12.4296"
    },
    "province": "Mecklenburg-Vorpommern"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 28078,
      "deaths": 723,
      "recovered": 22367
    },
    "coordinates": {
      "latitude": "52.6367",
      "longitude": "9.8451"
    },
    "province": "Niedersachsen"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 100247,
      "deaths": 1994,
      "recovered": 74816
    },
    "coordinates": {
      "latitude": "51.4332",
      "longitude": "7.6616"
    },
    "province": "Nordrhein-Westfalen"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15186,
      "deaths": 267,
      "recovered": 11579
    },
    "coordinates": {
      "latitude": "50.1183",
      "longitude": "7.309"
    },
    "province": "Rheinland-Pfalz"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5065,
      "deaths": 178,
      "recovered": 3721
    },
    "coordinates": {
      "latitude": "49.3964",
      "longitude": "7.023"
    },
    "province": "Saarland"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12071,
      "deaths": 272,
      "recovered": 7956
    },
    "coordinates": {
      "latitude": "51.1045",
      "longitude": "13.2017"
    },
    "province": "Sachsen"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3645,
      "deaths": 73,
      "recovered": 2818
    },
    "coordinates": {
      "latitude": "51.9503",
      "longitude": "11.6923"
    },
    "province": "Sachsen-Anhalt"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6284,
      "deaths": 164,
      "recovered": 5116
    },
    "coordinates": {
      "latitude": "54.2194",
      "longitude": "9.6961"
    },
    "province": "Schleswig-Holstein"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5394,
      "deaths": 201,
      "recovered": 4294
    },
    "coordinates": {
      "latitude": "51.011",
      "longitude": "10.8453"
    },
    "province": "Thuringen"
  },
  {
    "country": "Germany",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 93,
      "deaths": 0,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "Ghana",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 47538,
      "deaths": 312,
      "recovered": 46789
    },
    "coordinates": {
      "latitude": "7.9465",
      "longitude": "-1.0232"
    },
    "province": null
  },
  {
    "country": "Greece",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 28216,
      "deaths": 549,
      "recovered": 1347
    },
    "coordinates": {
      "latitude": "39.0742",
      "longitude": "21.8243"
    },
    "province": null
  },
  {
    "country": "Grenada",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 27,
      "deaths": 0,
      "recovered": 24
    },
    "coordinates": {
      "latitude": "12.1165",
      "longitude": "-61.679"
    },
    "province": null
  },
  {
    "country": "Guatemala",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 103172,
      "deaths": 3580,
      "recovered": 92665
    },
    "coordinates": {
      "latitude": "15.7835",
      "longitude": "-90.2308"
    },
    "province": null
  },
  {
    "country": "Guinea",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11635,
      "deaths": 71,
      "recovered": 10474
    },
    "coordinates": {
      "latitude": "9.9456",
      "longitude": "-9.6966"
    },
    "province": null
  },
  {
    "country": "Guinea-Bissau",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2403,
      "deaths": 41,
      "recovered": 1818
    },
    "coordinates": {
      "latitude": "11.8037",
      "longitude": "-15.1804"
    },
    "province": null
  },
  {
    "country": "Guyana",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3877,
      "deaths": 117,
      "recovered": 2853
    },
    "coordinates": {
      "latitude": "4.860416000000002",
      "longitude": "-58.93018000000001"
    },
    "province": null
  },
  {
    "country": "Haiti",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9007,
      "deaths": 231,
      "recovered": 7311
    },
    "coordinates": {
      "latitude": "18.9712",
      "longitude": "-72.2852"
    },
    "province": null
  },
  {
    "country": "Holy See",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 27,
      "deaths": 0,
      "recovered": 15
    },
    "coordinates": {
      "latitude": "41.9029",
      "longitude": "12.4534"
    },
    "province": null
  },
  {
    "country": "Honduras",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 91509,
      "deaths": 2604,
      "recovered": 37132
    },
    "coordinates": {
      "latitude": "15.2",
      "longitude": "-86.2419"
    },
    "province": null
  },
  {
    "country": "Hungary",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 52212,
      "deaths": 1305,
      "recovered": 15254
    },
    "coordinates": {
      "latitude": "47.1625",
      "longitude": "19.5033"
    },
    "province": null
  },
  {
    "country": "Iceland",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4268,
      "deaths": 11,
      "recovered": 3098
    },
    "coordinates": {
      "latitude": "64.9631",
      "longitude": "-19.0208"
    },
    "province": null
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4184,
      "deaths": 57,
      "recovered": 3937
    },
    "coordinates": {
      "latitude": "11.225999",
      "longitude": "92.968178"
    },
    "province": "Andaman and Nicobar Islands"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 796919,
      "deaths": 6524,
      "recovered": 758138
    },
    "coordinates": {
      "latitude": "15.9129",
      "longitude": "79.74"
    },
    "province": "Andhra Pradesh"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 14077,
      "deaths": 32,
      "recovered": 11407
    },
    "coordinates": {
      "latitude": "27.768456",
      "longitude": "96.384277"
    },
    "province": "Arunachal Pradesh"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 203282,
      "deaths": 896,
      "recovered": 177662
    },
    "coordinates": {
      "latitude": "26.357149",
      "longitude": "92.830441"
    },
    "province": "Assam"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 209447,
      "deaths": 1026,
      "recovered": 197208
    },
    "coordinates": {
      "latitude": "25.679658",
      "longitude": "85.60484"
    },
    "province": "Bihar"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13848,
      "deaths": 212,
      "recovered": 12924
    },
    "coordinates": {
      "latitude": "30.733839",
      "longitude": "76.76827800000002"
    },
    "province": "Chandigarh"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 170130,
      "deaths": 1680,
      "recovered": 143212
    },
    "coordinates": {
      "latitude": "21.264705",
      "longitude": "82.035366"
    },
    "province": "Chhattisgarh"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3213,
      "deaths": 2,
      "recovered": 3164
    },
    "coordinates": {
      "latitude": "20.194742",
      "longitude": "73.080901"
    },
    "province": "Dadra and Nagar Haveli and Daman and Diu"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 344318,
      "deaths": 6163,
      "recovered": 312918
    },
    "coordinates": {
      "latitude": "28.646519",
      "longitude": "77.10898"
    },
    "province": "Delhi"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 41586,
      "deaths": 564,
      "recovered": 38031
    },
    "coordinates": {
      "latitude": "15.359682",
      "longitude": "74.057396"
    },
    "province": "Goa"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 163959,
      "deaths": 3667,
      "recovered": 146171
    },
    "coordinates": {
      "latitude": "22.694884",
      "longitude": "71.590923"
    },
    "province": "Gujarat"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 154495,
      "deaths": 1688,
      "recovered": 142798
    },
    "coordinates": {
      "latitude": "29.20004",
      "longitude": "76.332824"
    },
    "province": "Haryana"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 19844,
      "deaths": 284,
      "recovered": 16937
    },
    "coordinates": {
      "latitude": "31.927213",
      "longitude": "77.233081"
    },
    "province": "Himachal Pradesh"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 90166,
      "deaths": 1412,
      "recovered": 80802
    },
    "coordinates": {
      "latitude": "33.75943",
      "longitude": "76.612638"
    },
    "province": "Jammu and Kashmir"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 98610,
      "deaths": 859,
      "recovered": 91629
    },
    "coordinates": {
      "latitude": "23.654536",
      "longitude": "85.557631"
    },
    "province": "Jharkhand"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 788551,
      "deaths": 10770,
      "recovered": 684835
    },
    "coordinates": {
      "latitude": "14.70518",
      "longitude": "76.166436"
    },
    "province": "Karnataka"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 369323,
      "deaths": 1255,
      "recovered": 274675
    },
    "coordinates": {
      "latitude": "10.450898",
      "longitude": "76.405749"
    },
    "province": "Kerala"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5812,
      "deaths": 68,
      "recovered": 4902
    },
    "coordinates": {
      "latitude": "34.1526",
      "longitude": "77.5771"
    },
    "province": "Ladakh"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 0,
      "deaths": 0,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "13.6999972",
      "longitude": "72.18333259999999"
    },
    "province": "Lakshadweep"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 164341,
      "deaths": 2842,
      "recovered": 149353
    },
    "coordinates": {
      "latitude": "23.541513",
      "longitude": "78.289633"
    },
    "province": "Madhya Pradesh"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1625197,
      "deaths": 42831,
      "recovered": 1431856
    },
    "coordinates": {
      "latitude": "19.449759",
      "longitude": "76.108221"
    },
    "province": "Maharashtra"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16621,
      "deaths": 127,
      "recovered": 12393
    },
    "coordinates": {
      "latitude": "24.738975",
      "longitude": "93.882541"
    },
    "province": "Manipur"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8720,
      "deaths": 78,
      "recovered": 6981
    },
    "coordinates": {
      "latitude": "25.536934",
      "longitude": "91.278882"
    },
    "province": "Meghalaya"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2359,
      "deaths": 0,
      "recovered": 2175
    },
    "coordinates": {
      "latitude": "23.309381",
      "longitude": "92.83822"
    },
    "province": "Mizoram"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8296,
      "deaths": 28,
      "recovered": 6469
    },
    "coordinates": {
      "latitude": "26.06702",
      "longitude": "94.470302"
    },
    "province": "Nagaland"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 276094,
      "deaths": 1196,
      "recovered": 257041
    },
    "coordinates": {
      "latitude": "20.505428",
      "longitude": "84.418059"
    },
    "province": "Odisha"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 33832,
      "deaths": 582,
      "recovered": 29211
    },
    "coordinates": {
      "latitude": "11.882658",
      "longitude": "78.86498"
    },
    "province": "Puducherry"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 129693,
      "deaths": 4072,
      "recovered": 121155
    },
    "coordinates": {
      "latitude": "30.841465000000003",
      "longitude": "75.40879"
    },
    "province": "Punjab"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 180755,
      "deaths": 1800,
      "recovered": 160614
    },
    "coordinates": {
      "latitude": "26.583423",
      "longitude": "73.847973"
    },
    "province": "Rajasthan"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3727,
      "deaths": 63,
      "recovered": 3410
    },
    "coordinates": {
      "latitude": "27.571671",
      "longitude": "88.472712"
    },
    "province": "Sikkim"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 700193,
      "deaths": 10825,
      "recovered": 655170
    },
    "coordinates": {
      "latitude": "11.006091",
      "longitude": "78.400624"
    },
    "province": "Tamil Nadu"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 229001,
      "deaths": 1298,
      "recovered": 207326
    },
    "coordinates": {
      "latitude": "18.1124",
      "longitude": "79.0193"
    },
    "province": "Telangana"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 30070,
      "deaths": 339,
      "recovered": 27502
    },
    "coordinates": {
      "latitude": "23.746783",
      "longitude": "91.743565"
    },
    "province": "Tripura"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 0,
      "deaths": 0,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 463858,
      "deaths": 6790,
      "recovered": 427937
    },
    "coordinates": {
      "latitude": "26.925425",
      "longitude": "80.560982"
    },
    "province": "Uttar Pradesh"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 59508,
      "deaths": 968,
      "recovered": 53643
    },
    "coordinates": {
      "latitude": "30.156447",
      "longitude": "79.197608"
    },
    "province": "Uttarakhand"
  },
  {
    "country": "India",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 337283,
      "deaths": 6308,
      "recovered": 294911
    },
    "coordinates": {
      "latitude": "23.814082",
      "longitude": "87.979803"
    },
    "province": "West Bengal"
  },
  {
    "country": "Indonesia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 377541,
      "deaths": 12959,
      "recovered": 301006
    },
    "coordinates": {
      "latitude": "-0.7893",
      "longitude": "113.9213"
    },
    "province": null
  },
  {
    "country": "Iran",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 550757,
      "deaths": 31650,
      "recovered": 442674
    },
    "coordinates": {
      "latitude": "32.427908",
      "longitude": "53.68804599999999"
    },
    "province": null
  },
  {
    "country": "Iraq",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 442164,
      "deaths": 10465,
      "recovered": 371826
    },
    "coordinates": {
      "latitude": "33.223191",
      "longitude": "43.679291"
    },
    "province": null
  },
  {
    "country": "Ireland",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 54476,
      "deaths": 1871,
      "recovered": 23364
    },
    "coordinates": {
      "latitude": "53.1424",
      "longitude": "-7.6921"
    },
    "province": null
  },
  {
    "country": "Israel",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 308247,
      "deaths": 2319,
      "recovered": 288337
    },
    "coordinates": {
      "latitude": "31.046051",
      "longitude": "34.851612"
    },
    "province": null
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7091,
      "deaths": 501,
      "recovered": 3214
    },
    "coordinates": {
      "latitude": "42.35122196",
      "longitude": "13.39843823"
    },
    "province": "Abruzzo"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1481,
      "deaths": 42,
      "recovered": 611
    },
    "coordinates": {
      "latitude": "40.63947052",
      "longitude": "15.80514834"
    },
    "province": "Basilicata"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3286,
      "deaths": 105,
      "recovered": 1644
    },
    "coordinates": {
      "latitude": "38.90597598",
      "longitude": "16.59440194"
    },
    "province": "Calabria"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 32025,
      "deaths": 551,
      "recovered": 8913
    },
    "coordinates": {
      "latitude": "40.83956555",
      "longitude": "14.25084984"
    },
    "province": "Campania"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 43477,
      "deaths": 4537,
      "recovered": 27277
    },
    "coordinates": {
      "latitude": "44.49436681",
      "longitude": "11.3417208"
    },
    "province": "Emilia-Romagna"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7075,
      "deaths": 368,
      "recovered": 4482
    },
    "coordinates": {
      "latitude": "45.6494354",
      "longitude": "13.76813649"
    },
    "province": "Friuli Venezia Giulia"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 29621,
      "deaths": 1070,
      "recovered": 10020
    },
    "coordinates": {
      "latitude": "41.89277044",
      "longitude": "12.48366722"
    },
    "province": "Lazio"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20581,
      "deaths": 1673,
      "recovered": 13842
    },
    "coordinates": {
      "latitude": "44.41149315",
      "longitude": "8.9326992"
    },
    "province": "Liguria"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 138729,
      "deaths": 17152,
      "recovered": 88059
    },
    "coordinates": {
      "latitude": "45.46679409",
      "longitude": "9.190347404"
    },
    "province": "Lombardia"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10192,
      "deaths": 998,
      "recovered": 6570
    },
    "coordinates": {
      "latitude": "43.61675973",
      "longitude": "13.5188753"
    },
    "province": "Marche"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1070,
      "deaths": 26,
      "recovered": 594
    },
    "coordinates": {
      "latitude": "41.55774754",
      "longitude": "14.65916051"
    },
    "province": "Molise"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5549,
      "deaths": 296,
      "recovered": 2935
    },
    "coordinates": {
      "latitude": "46.49933453",
      "longitude": "11.35662422"
    },
    "province": "P.A. Bolzano"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7319,
      "deaths": 423,
      "recovered": 5927
    },
    "coordinates": {
      "latitude": "46.06893511",
      "longitude": "11.12123097"
    },
    "province": "P.A. Trento"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 49668,
      "deaths": 4227,
      "recovered": 30661
    },
    "coordinates": {
      "latitude": "45.0732745",
      "longitude": "7.680687483"
    },
    "province": "Piemonte"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12810,
      "deaths": 645,
      "recovered": 5886
    },
    "coordinates": {
      "latitude": "41.12559576",
      "longitude": "16.86736689"
    },
    "province": "Puglia"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6886,
      "deaths": 181,
      "recovered": 2712
    },
    "coordinates": {
      "latitude": "39.21531192",
      "longitude": "9.110616306"
    },
    "province": "Sardegna"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 14586,
      "deaths": 397,
      "recovered": 5649
    },
    "coordinates": {
      "latitude": "38.11569725",
      "longitude": "13.362356699999998"
    },
    "province": "Sicilia"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 26611,
      "deaths": 1229,
      "recovered": 12121
    },
    "coordinates": {
      "latitude": "43.76923077",
      "longitude": "11.25588885"
    },
    "province": "Toscana"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5860,
      "deaths": 97,
      "recovered": 2493
    },
    "coordinates": {
      "latitude": "43.10675841",
      "longitude": "12.38824698"
    },
    "province": "Umbria"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2219,
      "deaths": 149,
      "recovered": 1165
    },
    "coordinates": {
      "latitude": "45.73750286",
      "longitude": "7.320149366"
    },
    "province": "Valle d'Aosta"
  },
  {
    "country": "Italy",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 39590,
      "deaths": 2301,
      "recovered": 24681
    },
    "coordinates": {
      "latitude": "45.43490485",
      "longitude": "12.33845213"
    },
    "province": "Veneto"
  },
  {
    "country": "Jamaica",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8600,
      "deaths": 179,
      "recovered": 4095
    },
    "coordinates": {
      "latitude": "18.1096",
      "longitude": "-77.2975"
    },
    "province": null
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5775,
      "deaths": 91,
      "recovered": 5394
    },
    "coordinates": {
      "latitude": "35.035551",
      "longitude": "137.211621"
    },
    "province": "Aichi"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 61,
      "deaths": 0,
      "recovered": 59
    },
    "coordinates": {
      "latitude": "39.748679",
      "longitude": "140.408228"
    },
    "province": "Akita"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 149,
      "deaths": 1,
      "recovered": 39
    },
    "coordinates": {
      "latitude": "40.781541",
      "longitude": "140.828896"
    },
    "province": "Aomori"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4681,
      "deaths": 76,
      "recovered": 4232
    },
    "coordinates": {
      "latitude": "35.510141",
      "longitude": "140.198917"
    },
    "province": "Chiba"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 116,
      "deaths": 6,
      "recovered": 109
    },
    "coordinates": {
      "latitude": "33.624835",
      "longitude": "132.856842"
    },
    "province": "Ehime"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 256,
      "deaths": 11,
      "recovered": 237
    },
    "coordinates": {
      "latitude": "35.846614",
      "longitude": "136.22465400000002"
    },
    "province": "Fukui"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5173,
      "deaths": 100,
      "recovered": 4987
    },
    "coordinates": {
      "latitude": "33.526032",
      "longitude": "130.666949"
    },
    "province": "Fukuoka"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 379,
      "deaths": 6,
      "recovered": 290
    },
    "coordinates": {
      "latitude": "37.378867",
      "longitude": "140.223295"
    },
    "province": "Fukushima"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 660,
      "deaths": 10,
      "recovered": 625
    },
    "coordinates": {
      "latitude": "35.778671",
      "longitude": "137.055925"
    },
    "province": "Gifu"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 820,
      "deaths": 19,
      "recovered": 730
    },
    "coordinates": {
      "latitude": "36.504479",
      "longitude": "138.985605"
    },
    "province": "Gunma"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 649,
      "deaths": 5,
      "recovered": 617
    },
    "coordinates": {
      "latitude": "34.605309000000005",
      "longitude": "132.788719"
    },
    "province": "Hiroshima"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2641,
      "deaths": 108,
      "recovered": 2266
    },
    "coordinates": {
      "latitude": "43.385711",
      "longitude": "142.552318"
    },
    "province": "Hokkaido"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3058,
      "deaths": 60,
      "recovered": 2847
    },
    "coordinates": {
      "latitude": "35.039913",
      "longitude": "134.828057"
    },
    "province": "Hyogo"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 735,
      "deaths": 19,
      "recovered": 684
    },
    "coordinates": {
      "latitude": "36.303588",
      "longitude": "140.319591"
    },
    "province": "Ibaraki"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 796,
      "deaths": 48,
      "recovered": 731
    },
    "coordinates": {
      "latitude": "36.769464",
      "longitude": "136.771027"
    },
    "province": "Ishikawa"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 26,
      "deaths": 0,
      "recovered": 23
    },
    "coordinates": {
      "latitude": "39.593287",
      "longitude": "141.361777"
    },
    "province": "Iwate"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 102,
      "deaths": 2,
      "recovered": 94
    },
    "coordinates": {
      "latitude": "34.217292",
      "longitude": "133.969047"
    },
    "province": "Kagawa"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 463,
      "deaths": 12,
      "recovered": 453
    },
    "coordinates": {
      "latitude": "31.009484000000004",
      "longitude": "130.430665"
    },
    "province": "Kagoshima"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8164,
      "deaths": 158,
      "recovered": 7429
    },
    "coordinates": {
      "latitude": "35.415312",
      "longitude": "139.338983"
    },
    "province": "Kanagawa"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 140,
      "deaths": 4,
      "recovered": 135
    },
    "coordinates": {
      "latitude": "33.422519",
      "longitude": "133.367307"
    },
    "province": "Kochi"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 767,
      "deaths": 8,
      "recovered": 686
    },
    "coordinates": {
      "latitude": "32.608154",
      "longitude": "130.74523100000002"
    },
    "province": "Kumamoto"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1958,
      "deaths": 30,
      "recovered": 1820
    },
    "coordinates": {
      "latitude": "35.253815",
      "longitude": "135.443341"
    },
    "province": "Kyoto"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 553,
      "deaths": 6,
      "recovered": 529
    },
    "coordinates": {
      "latitude": "34.508018",
      "longitude": "136.376013"
    },
    "province": "Mie"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 545,
      "deaths": 2,
      "recovered": 491
    },
    "coordinates": {
      "latitude": "38.446859",
      "longitude": "140.927086"
    },
    "province": "Miyagi"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 366,
      "deaths": 1,
      "recovered": 365
    },
    "coordinates": {
      "latitude": "32.193203999999994",
      "longitude": "131.299374"
    },
    "province": "Miyazaki"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 328,
      "deaths": 4,
      "recovered": 319
    },
    "coordinates": {
      "latitude": "36.132134",
      "longitude": "138.045528"
    },
    "province": "Nagano"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 242,
      "deaths": 3,
      "recovered": 236
    },
    "coordinates": {
      "latitude": "33.235712",
      "longitude": "129.608033"
    },
    "province": "Nagasaki"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 621,
      "deaths": 9,
      "recovered": 588
    },
    "coordinates": {
      "latitude": "34.317451",
      "longitude": "135.871644"
    },
    "province": "Nara"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 180,
      "deaths": 0,
      "recovered": 179
    },
    "coordinates": {
      "latitude": "37.521819",
      "longitude": "138.918647"
    },
    "province": "Niigata"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 159,
      "deaths": 2,
      "recovered": 155
    },
    "coordinates": {
      "latitude": "33.200697",
      "longitude": "131.43323999999998"
    },
    "province": "Oita"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 188,
      "deaths": 1,
      "recovered": 155
    },
    "coordinates": {
      "latitude": "34.89246",
      "longitude": "133.826252"
    },
    "province": "Okayama"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3055,
      "deaths": 57,
      "recovered": 2641
    },
    "coordinates": {
      "latitude": "25.768923",
      "longitude": "126.668016"
    },
    "province": "Okinawa"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11780,
      "deaths": 231,
      "recovered": 10984
    },
    "coordinates": {
      "latitude": "34.620965000000005",
      "longitude": "135.507481"
    },
    "province": "Osaka"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1116,
      "deaths": 1,
      "recovered": 514
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Port Quarantine"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 251,
      "deaths": 1,
      "recovered": 250
    },
    "coordinates": {
      "latitude": "33.286977",
      "longitude": "130.115738"
    },
    "province": "Saga"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5522,
      "deaths": 103,
      "recovered": 4948
    },
    "coordinates": {
      "latitude": "35.997101",
      "longitude": "139.347635"
    },
    "province": "Saitama"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 533,
      "deaths": 9,
      "recovered": 506
    },
    "coordinates": {
      "latitude": "35.21582700000001",
      "longitude": "136.138064"
    },
    "province": "Shiga"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 140,
      "deaths": 0,
      "recovered": 140
    },
    "coordinates": {
      "latitude": "35.07076",
      "longitude": "132.55406399999998"
    },
    "province": "Shimane"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 585,
      "deaths": 2,
      "recovered": 567
    },
    "coordinates": {
      "latitude": "34.916975",
      "longitude": "138.40778400000002"
    },
    "province": "Shizuoka"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 473,
      "deaths": 1,
      "recovered": 442
    },
    "coordinates": {
      "latitude": "36.689912",
      "longitude": "139.819213"
    },
    "province": "Tochigi"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 164,
      "deaths": 9,
      "recovered": 140
    },
    "coordinates": {
      "latitude": "33.919178",
      "longitude": "134.242091"
    },
    "province": "Tokushima"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 29536,
      "deaths": 442,
      "recovered": 27227
    },
    "coordinates": {
      "latitude": "35.711343",
      "longitude": "139.446921"
    },
    "province": "Tokyo"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 35,
      "deaths": 0,
      "recovered": 36
    },
    "coordinates": {
      "latitude": "35.359069",
      "longitude": "133.863619"
    },
    "province": "Tottori"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 422,
      "deaths": 26,
      "recovered": 396
    },
    "coordinates": {
      "latitude": "36.637464",
      "longitude": "137.26934599999998"
    },
    "province": "Toyama"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8,
      "deaths": 0,
      "recovered": 8
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 266,
      "deaths": 4,
      "recovered": 242
    },
    "coordinates": {
      "latitude": "33.911879",
      "longitude": "135.505446"
    },
    "province": "Wakayama"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 84,
      "deaths": 1,
      "recovered": 79
    },
    "coordinates": {
      "latitude": "38.448396",
      "longitude": "140.102154"
    },
    "province": "Yamagata"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 211,
      "deaths": 2,
      "recovered": 205
    },
    "coordinates": {
      "latitude": "34.201190000000004",
      "longitude": "131.573293"
    },
    "province": "Yamaguchi"
  },
  {
    "country": "Japan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 202,
      "deaths": 6,
      "recovered": 193
    },
    "coordinates": {
      "latitude": "35.612364",
      "longitude": "138.61148899999998"
    },
    "province": "Yamanashi"
  },
  {
    "country": "Jordan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 46441,
      "deaths": 481,
      "recovered": 7340
    },
    "coordinates": {
      "latitude": "31.24",
      "longitude": "36.51"
    },
    "province": null
  },
  {
    "country": "Kazakhstan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 110086,
      "deaths": 1796,
      "recovered": 105493
    },
    "coordinates": {
      "latitude": "48.0196",
      "longitude": "66.9237"
    },
    "province": null
  },
  {
    "country": "Kenya",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 47212,
      "deaths": 870,
      "recovered": 33050
    },
    "coordinates": {
      "latitude": "-0.0236",
      "longitude": "37.9062"
    },
    "province": null
  },
  {
    "country": "Korea, South",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 25698,
      "deaths": 455,
      "recovered": 23717
    },
    "coordinates": {
      "latitude": "35.90775700000001",
      "longitude": "127.766922"
    },
    "province": null
  },
  {
    "country": "Kosovo",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17263,
      "deaths": 657,
      "recovered": 14831
    },
    "coordinates": {
      "latitude": "42.602636",
      "longitude": "20.902977"
    },
    "province": null
  },
  {
    "country": "Kuwait",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 119420,
      "deaths": 730,
      "recovered": 110714
    },
    "coordinates": {
      "latitude": "29.31166",
      "longitude": "47.481766"
    },
    "province": null
  },
  {
    "country": "Kyrgyzstan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 54006,
      "deaths": 1122,
      "recovered": 46726
    },
    "coordinates": {
      "latitude": "41.20438",
      "longitude": "74.766098"
    },
    "province": null
  },
  {
    "country": "Laos",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 24,
      "deaths": 0,
      "recovered": 22
    },
    "coordinates": {
      "latitude": "19.85627",
      "longitude": "102.495496"
    },
    "province": null
  },
  {
    "country": "Latvia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3958,
      "deaths": 49,
      "recovered": 1357
    },
    "coordinates": {
      "latitude": "56.8796",
      "longitude": "24.6032"
    },
    "province": null
  },
  {
    "country": "Lebanon",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 67027,
      "deaths": 552,
      "recovered": 31409
    },
    "coordinates": {
      "latitude": "33.8547",
      "longitude": "35.8623"
    },
    "province": null
  },
  {
    "country": "Lesotho",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1923,
      "deaths": 43,
      "recovered": 961
    },
    "coordinates": {
      "latitude": "-29.61",
      "longitude": "28.2336"
    },
    "province": null
  },
  {
    "country": "Liberia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1385,
      "deaths": 82,
      "recovered": 1278
    },
    "coordinates": {
      "latitude": "6.4280550000000005",
      "longitude": "-9.429499"
    },
    "province": null
  },
  {
    "country": "Libya",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 52620,
      "deaths": 768,
      "recovered": 29057
    },
    "coordinates": {
      "latitude": "26.3351",
      "longitude": "17.228331"
    },
    "province": null
  },
  {
    "country": "Liechtenstein",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 282,
      "deaths": 1,
      "recovered": 158
    },
    "coordinates": {
      "latitude": "47.14",
      "longitude": "9.55"
    },
    "province": null
  },
  {
    "country": "Lithuania",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8663,
      "deaths": 125,
      "recovered": 3773
    },
    "coordinates": {
      "latitude": "55.1694",
      "longitude": "23.8813"
    },
    "province": null
  },
  {
    "country": "Luxembourg",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12333,
      "deaths": 140,
      "recovered": 8474
    },
    "coordinates": {
      "latitude": "49.8153",
      "longitude": "6.1296"
    },
    "province": null
  },
  {
    "country": "MS Zaandam",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9,
      "deaths": 2,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": null
  },
  {
    "country": "Madagascar",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16810,
      "deaths": 238,
      "recovered": 16215
    },
    "coordinates": {
      "latitude": "-18.766947",
      "longitude": "46.869107"
    },
    "province": null
  },
  {
    "country": "Malawi",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5874,
      "deaths": 183,
      "recovered": 4764
    },
    "coordinates": {
      "latitude": "-13.2543",
      "longitude": "34.3015"
    },
    "province": null
  },
  {
    "country": "Malaysia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 23804,
      "deaths": 204,
      "recovered": 15417
    },
    "coordinates": {
      "latitude": "4.210483999999999",
      "longitude": "101.975766"
    },
    "province": null
  },
  {
    "country": "Maldives",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11358,
      "deaths": 37,
      "recovered": 10383
    },
    "coordinates": {
      "latitude": "3.2028",
      "longitude": "73.2207"
    },
    "province": null
  },
  {
    "country": "Mali",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3440,
      "deaths": 132,
      "recovered": 2608
    },
    "coordinates": {
      "latitude": "17.570692",
      "longitude": "-3.996166000000001"
    },
    "province": null
  },
  {
    "country": "Malta",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5137,
      "deaths": 49,
      "recovered": 3384
    },
    "coordinates": {
      "latitude": "35.9375",
      "longitude": "14.3754"
    },
    "province": null
  },
  {
    "country": "Mauritania",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7650,
      "deaths": 163,
      "recovered": 7369
    },
    "coordinates": {
      "latitude": "21.0079",
      "longitude": "-10.9408"
    },
    "province": null
  },
  {
    "country": "Mauritius",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 425,
      "deaths": 10,
      "recovered": 386
    },
    "coordinates": {
      "latitude": "-20.348404",
      "longitude": "57.552152"
    },
    "province": null
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8746,
      "deaths": 769,
      "recovered": 6874
    },
    "coordinates": {
      "latitude": "21.8853",
      "longitude": "-102.2916"
    },
    "province": "Aguascalientes"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 22125,
      "deaths": 3733,
      "recovered": 17479
    },
    "coordinates": {
      "latitude": "30.8406",
      "longitude": "-115.2838"
    },
    "province": "Baja California"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11900,
      "deaths": 577,
      "recovered": 10444
    },
    "coordinates": {
      "latitude": "26.0444",
      "longitude": "-111.6661"
    },
    "province": "Baja California Sur"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6379,
      "deaths": 854,
      "recovered": 5463
    },
    "coordinates": {
      "latitude": "19.8301",
      "longitude": "-90.5349"
    },
    "province": "Campeche"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7465,
      "deaths": 1066,
      "recovered": 6266
    },
    "coordinates": {
      "latitude": "16.7569",
      "longitude": "-93.1292"
    },
    "province": "Chiapas"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15521,
      "deaths": 1671,
      "recovered": 10850
    },
    "coordinates": {
      "latitude": "28.633000000000006",
      "longitude": "-106.0691"
    },
    "province": "Chihuahua"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 151917,
      "deaths": 14554,
      "recovered": 126746
    },
    "coordinates": {
      "latitude": "19.4326",
      "longitude": "-99.1332"
    },
    "province": "Ciudad de Mexico"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 31183,
      "deaths": 2153,
      "recovered": 26452
    },
    "coordinates": {
      "latitude": "27.0587",
      "longitude": "-101.7068"
    },
    "province": "Coahuila"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6278,
      "deaths": 689,
      "recovered": 5193
    },
    "coordinates": {
      "latitude": "19.1223",
      "longitude": "-104.0072"
    },
    "province": "Colima"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11919,
      "deaths": 730,
      "recovered": 9348
    },
    "coordinates": {
      "latitude": "24.5593",
      "longitude": "-104.6588"
    },
    "province": "Durango"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 46025,
      "deaths": 3254,
      "recovered": 40409
    },
    "coordinates": {
      "latitude": "21.019",
      "longitude": "-101.2574"
    },
    "province": "Guanajuato"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 21580,
      "deaths": 2096,
      "recovered": 18764
    },
    "coordinates": {
      "latitude": "17.4392",
      "longitude": "-99.5451"
    },
    "province": "Guerrero"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 14964,
      "deaths": 2186,
      "recovered": 11911
    },
    "coordinates": {
      "latitude": "20.0911",
      "longitude": "-98.7624"
    },
    "province": "Hidalgo"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 32193,
      "deaths": 3762,
      "recovered": 25988
    },
    "coordinates": {
      "latitude": "20.6595",
      "longitude": "-103.3494"
    },
    "province": "Jalisco"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 94208,
      "deaths": 10348,
      "recovered": 80473
    },
    "coordinates": {
      "latitude": "19.4969",
      "longitude": "-99.7233"
    },
    "province": "Mexico"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 23857,
      "deaths": 1889,
      "recovered": 20874
    },
    "coordinates": {
      "latitude": "19.5665",
      "longitude": "-101.7068"
    },
    "province": "Michoacan"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6671,
      "deaths": 1168,
      "recovered": 5207
    },
    "coordinates": {
      "latitude": "18.6813",
      "longitude": "-99.1013"
    },
    "province": "Morelos"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6567,
      "deaths": 822,
      "recovered": 5427
    },
    "coordinates": {
      "latitude": "21.7514",
      "longitude": "-104.8455"
    },
    "province": "Nayarit"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 49454,
      "deaths": 3618,
      "recovered": 41577
    },
    "coordinates": {
      "latitude": "25.5922",
      "longitude": "-99.9962"
    },
    "province": "Nuevo Leon"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20254,
      "deaths": 1598,
      "recovered": 17744
    },
    "coordinates": {
      "latitude": "17.0732",
      "longitude": "-96.7266"
    },
    "province": "Oaxaca"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 34532,
      "deaths": 4582,
      "recovered": 28899
    },
    "coordinates": {
      "latitude": "19.0414",
      "longitude": "-98.2063"
    },
    "province": "Puebla"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12170,
      "deaths": 1124,
      "recovered": 9348
    },
    "coordinates": {
      "latitude": "20.5888",
      "longitude": "-100.3899"
    },
    "province": "Queretaro"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13155,
      "deaths": 1795,
      "recovered": 10997
    },
    "coordinates": {
      "latitude": "19.1817",
      "longitude": "-88.4791"
    },
    "province": "Quintana Roo"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 26871,
      "deaths": 1892,
      "recovered": 23666
    },
    "coordinates": {
      "latitude": "22.1565",
      "longitude": "-100.9855"
    },
    "province": "San Luis Potosi"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 21077,
      "deaths": 3504,
      "recovered": 16801
    },
    "coordinates": {
      "latitude": "25.1721",
      "longitude": "-107.4795"
    },
    "province": "Sinaloa"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 37028,
      "deaths": 3097,
      "recovered": 33132
    },
    "coordinates": {
      "latitude": "29.2972",
      "longitude": "-110.3309"
    },
    "province": "Sonora"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 33857,
      "deaths": 2999,
      "recovered": 30132
    },
    "coordinates": {
      "latitude": "17.8409",
      "longitude": "-92.6189"
    },
    "province": "Tabasco"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 31246,
      "deaths": 2536,
      "recovered": 27940
    },
    "coordinates": {
      "latitude": "24.2669",
      "longitude": "-98.8363"
    },
    "province": "Tamaulipas"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8258,
      "deaths": 1101,
      "recovered": 6961
    },
    "coordinates": {
      "latitude": "19.3139",
      "longitude": "-98.2404"
    },
    "province": "Tlaxcala"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 36245,
      "deaths": 4664,
      "recovered": 30643
    },
    "coordinates": {
      "latitude": "19.1738",
      "longitude": "-96.1342"
    },
    "province": "Veracruz"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20730,
      "deaths": 1734,
      "recovered": 17708
    },
    "coordinates": {
      "latitude": "20.7099",
      "longitude": "-89.0943"
    },
    "province": "Yucatan"
  },
  {
    "country": "Mexico",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9796,
      "deaths": 850,
      "recovered": 7721
    },
    "coordinates": {
      "latitude": "22.7709",
      "longitude": "-102.5832"
    },
    "province": "Zacatecas"
  },
  {
    "country": "Moldova",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 69568,
      "deaths": 1641,
      "recovered": 50422
    },
    "coordinates": {
      "latitude": "47.4116",
      "longitude": "28.3699"
    },
    "province": null
  },
  {
    "country": "Monaco",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 281,
      "deaths": 2,
      "recovered": 233
    },
    "coordinates": {
      "latitude": "43.7333",
      "longitude": "7.4167"
    },
    "province": null
  },
  {
    "country": "Mongolia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 328,
      "deaths": 0,
      "recovered": 312
    },
    "coordinates": {
      "latitude": "46.8625",
      "longitude": "103.8467"
    },
    "province": null
  },
  {
    "country": "Montenegro",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16259,
      "deaths": 253,
      "recovered": 12093
    },
    "coordinates": {
      "latitude": "42.708678000000006",
      "longitude": "19.37439"
    },
    "province": null
  },
  {
    "country": "Morocco",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 186731,
      "deaths": 3132,
      "recovered": 154481
    },
    "coordinates": {
      "latitude": "31.7917",
      "longitude": "-7.0926"
    },
    "province": null
  },
  {
    "country": "Mozambique",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11559,
      "deaths": 81,
      "recovered": 9226
    },
    "coordinates": {
      "latitude": "-18.665695",
      "longitude": "35.529562"
    },
    "province": null
  },
  {
    "country": "Namibia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12460,
      "deaths": 133,
      "recovered": 10609
    },
    "coordinates": {
      "latitude": "-22.9576",
      "longitude": "18.4904"
    },
    "province": null
  },
  {
    "country": "Nepal",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 148509,
      "deaths": 812,
      "recovered": 102820
    },
    "coordinates": {
      "latitude": "28.1667",
      "longitude": "84.25"
    },
    "province": null
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4389,
      "deaths": 36,
      "recovered": 4120
    },
    "coordinates": {
      "latitude": "12.5211",
      "longitude": "-69.9683"
    },
    "province": "Aruba"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 150,
      "deaths": 3,
      "recovered": 121
    },
    "coordinates": {
      "latitude": "12.1784",
      "longitude": "-68.2385"
    },
    "province": "Bonaire, Sint Eustatius and Saba"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 804,
      "deaths": 1,
      "recovered": 509
    },
    "coordinates": {
      "latitude": "12.1696",
      "longitude": "-68.99"
    },
    "province": "Curacao"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3968,
      "deaths": 70,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "52.862485",
      "longitude": "6.618435000000002"
    },
    "province": "Drenthe"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4703,
      "deaths": 106,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "52.550383",
      "longitude": "5.515162"
    },
    "province": "Flevoland"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4558,
      "deaths": 76,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "53.087337",
      "longitude": "5.7925"
    },
    "province": "Friesland"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 24760,
      "deaths": 763,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "52.061738",
      "longitude": "5.939114"
    },
    "province": "Gelderland"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4897,
      "deaths": 24,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "53.217922",
      "longitude": "6.741514"
    },
    "province": "Groningen"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11828,
      "deaths": 779,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "51.209227",
      "longitude": "5.93387"
    },
    "province": "Limburg"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 38327,
      "deaths": 1631,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "51.561174",
      "longitude": "5.184942"
    },
    "province": "Noord-Brabant"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 52071,
      "deaths": 945,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "52.60090600000001",
      "longitude": "4.918688"
    },
    "province": "Noord-Holland"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12922,
      "deaths": 377,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "52.444558",
      "longitude": "6.441722"
    },
    "province": "Overijssel"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 769,
      "deaths": 22,
      "recovered": 681
    },
    "coordinates": {
      "latitude": "18.0425",
      "longitude": "-63.0548"
    },
    "province": "Sint Maarten"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1905,
      "deaths": 22,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 22779,
      "deaths": 474,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "52.084251",
      "longitude": "5.163824"
    },
    "province": "Utrecht"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2555,
      "deaths": 78,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "51.47936",
      "longitude": "3.861559"
    },
    "province": "Zeeland"
  },
  {
    "country": "Netherlands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 77132,
      "deaths": 1574,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "51.937835",
      "longitude": "4.462114"
    },
    "province": "Zuid-Holland"
  },
  {
    "country": "New Zealand",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1923,
      "deaths": 25,
      "recovered": 1832
    },
    "coordinates": {
      "latitude": "-40.9006",
      "longitude": "174.886"
    },
    "province": null
  },
  {
    "country": "Nicaragua",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5434,
      "deaths": 155,
      "recovered": 4225
    },
    "coordinates": {
      "latitude": "12.865416",
      "longitude": "-85.207229"
    },
    "province": null
  },
  {
    "country": "Niger",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1215,
      "deaths": 69,
      "recovered": 1128
    },
    "coordinates": {
      "latitude": "17.607789",
      "longitude": "8.081666"
    },
    "province": null
  },
  {
    "country": "Nigeria",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 61805,
      "deaths": 1127,
      "recovered": 56985
    },
    "coordinates": {
      "latitude": "9.082",
      "longitude": "8.6753"
    },
    "province": null
  },
  {
    "country": "North Macedonia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 25473,
      "deaths": 874,
      "recovered": 18047
    },
    "coordinates": {
      "latitude": "41.6086",
      "longitude": "21.7453"
    },
    "province": null
  },
  {
    "country": "Norway",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17234,
      "deaths": 279,
      "recovered": 11863
    },
    "coordinates": {
      "latitude": "60.472",
      "longitude": "8.4689"
    },
    "province": null
  },
  {
    "country": "Oman",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 111837,
      "deaths": 1147,
      "recovered": 97949
    },
    "coordinates": {
      "latitude": "21.512583",
      "longitude": "55.92325500000001"
    },
    "province": null
  },
  {
    "country": "Pakistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3688,
      "deaths": 85,
      "recovered": 2835
    },
    "coordinates": {
      "latitude": "34.027401",
      "longitude": "73.947253"
    },
    "province": "Azad Jammu and Kashmir"
  },
  {
    "country": "Pakistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15767,
      "deaths": 148,
      "recovered": 15382
    },
    "coordinates": {
      "latitude": "28.328492",
      "longitude": "65.898403"
    },
    "province": "Balochistan"
  },
  {
    "country": "Pakistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4127,
      "deaths": 90,
      "recovered": 3834
    },
    "coordinates": {
      "latitude": "35.792146",
      "longitude": "74.982138"
    },
    "province": "Gilgit-Baltistan"
  },
  {
    "country": "Pakistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18578,
      "deaths": 205,
      "recovered": 17050
    },
    "coordinates": {
      "latitude": "33.665087",
      "longitude": "73.121219"
    },
    "province": "Islamabad"
  },
  {
    "country": "Pakistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 38886,
      "deaths": 1267,
      "recovered": 37142
    },
    "coordinates": {
      "latitude": "34.485332",
      "longitude": "72.09169"
    },
    "province": "Khyber Pakhtunkhwa"
  },
  {
    "country": "Pakistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 102253,
      "deaths": 2329,
      "recovered": 97301
    },
    "coordinates": {
      "latitude": "30.811346",
      "longitude": "72.13913199999998"
    },
    "province": "Punjab"
  },
  {
    "country": "Pakistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 142917,
      "deaths": 2591,
      "recovered": 136102
    },
    "coordinates": {
      "latitude": "26.009446",
      "longitude": "68.77680699999999"
    },
    "province": "Sindh"
  },
  {
    "country": "Panama",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 127227,
      "deaths": 2612,
      "recovered": 103398
    },
    "coordinates": {
      "latitude": "8.538",
      "longitude": "-80.7821"
    },
    "province": null
  },
  {
    "country": "Papua New Guinea",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 583,
      "deaths": 7,
      "recovered": 545
    },
    "coordinates": {
      "latitude": "-6.314993",
      "longitude": "143.95555"
    },
    "province": null
  },
  {
    "country": "Paraguay",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 57526,
      "deaths": 1262,
      "recovered": 38187
    },
    "coordinates": {
      "latitude": "-23.4425",
      "longitude": "-58.4438"
    },
    "province": null
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16114,
      "deaths": 225,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-5.077253",
      "longitude": "-78.050172"
    },
    "province": "Amazonas"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 25339,
      "deaths": 1346,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-9.407125",
      "longitude": "-77.67179499999997"
    },
    "province": "Ancash"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5494,
      "deaths": 106,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-14.027713",
      "longitude": "-72.975378"
    },
    "province": "Apurimac"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 43811,
      "deaths": 1428,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-15.843524",
      "longitude": "-72.475539"
    },
    "province": "Arequipa"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12795,
      "deaths": 326,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-14.091648",
      "longitude": "-74.08344"
    },
    "province": "Ayacucho"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 21599,
      "deaths": 506,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-6.430284",
      "longitude": "-78.74559599999998"
    },
    "province": "Cajamarca"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 36101,
      "deaths": 1822,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-11.954609",
      "longitude": "-77.136042"
    },
    "province": "Callao"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 21888,
      "deaths": 450,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-13.191068",
      "longitude": "-72.153609"
    },
    "province": "Cusco"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7125,
      "deaths": 122,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-13.023888",
      "longitude": "-75.00277"
    },
    "province": "Huancavelica"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16975,
      "deaths": 408,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-9.421676",
      "longitude": "-76.040642"
    },
    "province": "Huanuco"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 29270,
      "deaths": 1660,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-14.235097",
      "longitude": "-75.574821"
    },
    "province": "Ica"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 22164,
      "deaths": 816,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-11.541783",
      "longitude": "-74.876968"
    },
    "province": "Junin"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 31836,
      "deaths": 2268,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-7.92139",
      "longitude": "-78.370238"
    },
    "province": "La Libertad"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 28017,
      "deaths": 1760,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-6.353049",
      "longitude": "-79.824113"
    },
    "province": "Lambayeque"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 398886,
      "deaths": 15294,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-11.766533",
      "longitude": "-76.60449799999998"
    },
    "province": "Lima"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 21428,
      "deaths": 967,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-4.124847",
      "longitude": "-74.424115"
    },
    "province": "Loreto"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8661,
      "deaths": 143,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-11.972699",
      "longitude": "-70.53171999999998"
    },
    "province": "Madre de Dios"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13997,
      "deaths": 275,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-16.860271",
      "longitude": "-70.839046"
    },
    "province": "Moquegua"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5561,
      "deaths": 113,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-10.39655",
      "longitude": "-75.307635"
    },
    "province": "Pasco"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 37696,
      "deaths": 2020,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-5.133361",
      "longitude": "-80.335861"
    },
    "province": "Piura"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16576,
      "deaths": 330,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-14.995826999999998",
      "longitude": "-69.922726"
    },
    "province": "Puno"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20259,
      "deaths": 722,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-7.039531",
      "longitude": "-76.729127"
    },
    "province": "San Martin"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12813,
      "deaths": 226,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-17.644160999999997",
      "longitude": "-70.27756"
    },
    "province": "Tacna"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8097,
      "deaths": 313,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-3.857496",
      "longitude": "-80.54525500000003"
    },
    "province": "Tumbes"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17374,
      "deaths": 338,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "-9.621718",
      "longitude": "-73.444929"
    },
    "province": "Ucayali"
  },
  {
    "country": "Peru",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 0,
      "deaths": 0,
      "recovered": 796719
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "Philippines",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 363888,
      "deaths": 6783,
      "recovered": 312333
    },
    "coordinates": {
      "latitude": "12.879721",
      "longitude": "121.774017"
    },
    "province": null
  },
  {
    "country": "Poland",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 214686,
      "deaths": 4019,
      "recovered": 102204
    },
    "coordinates": {
      "latitude": "51.9194",
      "longitude": "19.1451"
    },
    "province": null
  },
  {
    "country": "Portugal",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 109541,
      "deaths": 2245,
      "recovered": 64531
    },
    "coordinates": {
      "latitude": "39.3999",
      "longitude": "-8.2245"
    },
    "province": null
  },
  {
    "country": "Qatar",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 130462,
      "deaths": 228,
      "recovered": 127328
    },
    "coordinates": {
      "latitude": "25.3548",
      "longitude": "51.1839"
    },
    "province": null
  },
  {
    "country": "Romania",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 196004,
      "deaths": 6163,
      "recovered": 141089
    },
    "coordinates": {
      "latitude": "45.9432",
      "longitude": "24.9668"
    },
    "province": null
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5121,
      "deaths": 43,
      "recovered": 4162
    },
    "coordinates": {
      "latitude": "44.6939006",
      "longitude": "40.1520421"
    },
    "province": "Adygea Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17306,
      "deaths": 291,
      "recovered": 16110
    },
    "coordinates": {
      "latitude": "52.6932243",
      "longitude": "82.69314240000001"
    },
    "province": "Altai Krai"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5861,
      "deaths": 12,
      "recovered": 4154
    },
    "coordinates": {
      "latitude": "50.7114101",
      "longitude": "86.8572186"
    },
    "province": "Altai Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5553,
      "deaths": 61,
      "recovered": 4887
    },
    "coordinates": {
      "latitude": "52.8032368",
      "longitude": "128.437295"
    },
    "province": "Amur Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17854,
      "deaths": 271,
      "recovered": 10982
    },
    "coordinates": {
      "latitude": "63.5589686",
      "longitude": "43.1221646"
    },
    "province": "Arkhangelsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8524,
      "deaths": 151,
      "recovered": 6908
    },
    "coordinates": {
      "latitude": "47.1878186",
      "longitude": "47.608851"
    },
    "province": "Astrakhan Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10015,
      "deaths": 48,
      "recovered": 9062
    },
    "coordinates": {
      "latitude": "54.8573563",
      "longitude": "57.1439682"
    },
    "province": "Bashkortostan Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10652,
      "deaths": 61,
      "recovered": 9301
    },
    "coordinates": {
      "latitude": "50.7080119",
      "longitude": "37.5837615"
    },
    "province": "Belgorod Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11495,
      "deaths": 50,
      "recovered": 8708
    },
    "coordinates": {
      "latitude": "52.8873315",
      "longitude": "33.41585300000001"
    },
    "province": "Bryansk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9406,
      "deaths": 103,
      "recovered": 7615
    },
    "coordinates": {
      "latitude": "52.7182426",
      "longitude": "109.492143"
    },
    "province": "Buryatia Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2551,
      "deaths": 44,
      "recovered": 2066
    },
    "coordinates": {
      "latitude": "43.39761470000001",
      "longitude": "45.6985005"
    },
    "province": "Chechen Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17740,
      "deaths": 155,
      "recovered": 13570
    },
    "coordinates": {
      "latitude": "54.4223954",
      "longitude": "61.1865846"
    },
    "province": "Chelyabinsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 222,
      "deaths": 2,
      "recovered": 202
    },
    "coordinates": {
      "latitude": "66.0006475",
      "longitude": "169.4900869"
    },
    "province": "Chukotka Autonomous Okrug"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9384,
      "deaths": 122,
      "recovered": 7812
    },
    "coordinates": {
      "latitude": "55.4259922",
      "longitude": "47.0849429"
    },
    "province": "Chuvashia Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15283,
      "deaths": 735,
      "recovered": 13542
    },
    "coordinates": {
      "latitude": "43.05749160000001",
      "longitude": "47.1332224"
    },
    "province": "Dagestan Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6824,
      "deaths": 89,
      "recovered": 5594
    },
    "coordinates": {
      "latitude": "43.11542075",
      "longitude": "45.01713552"
    },
    "province": "Ingushetia Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 22368,
      "deaths": 342,
      "recovered": 18729
    },
    "coordinates": {
      "latitude": "56.6370122",
      "longitude": "104.719221"
    },
    "province": "Irkutsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10474,
      "deaths": 162,
      "recovered": 7887
    },
    "coordinates": {
      "latitude": "56.9167446",
      "longitude": "41.43521370000001"
    },
    "province": "Ivanovo Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1553,
      "deaths": 22,
      "recovered": 837
    },
    "coordinates": {
      "latitude": "48.57527615",
      "longitude": "132.66307460000002"
    },
    "province": "Jewish Autonomous Okrug"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9293,
      "deaths": 125,
      "recovered": 7104
    },
    "coordinates": {
      "latitude": "43.4806048",
      "longitude": "43.5978976"
    },
    "province": "Kabardino-Balkarian Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6005,
      "deaths": 93,
      "recovered": 4144
    },
    "coordinates": {
      "latitude": "54.7293041",
      "longitude": "21.1489473"
    },
    "province": "Kaliningrad Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8227,
      "deaths": 90,
      "recovered": 4982
    },
    "coordinates": {
      "latitude": "46.2313018",
      "longitude": "45.3275745"
    },
    "province": "Kalmykia Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11019,
      "deaths": 79,
      "recovered": 8604
    },
    "coordinates": {
      "latitude": "54.4382773",
      "longitude": "35.5272854"
    },
    "province": "Kaluga Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5318,
      "deaths": 70,
      "recovered": 3491
    },
    "coordinates": {
      "latitude": "57.1914882",
      "longitude": "160.03838190000005"
    },
    "province": "Kamchatka Krai"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8823,
      "deaths": 30,
      "recovered": 5215
    },
    "coordinates": {
      "latitude": "43.7368326",
      "longitude": "41.7267991"
    },
    "province": "Karachay-Cherkess Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5469,
      "deaths": 42,
      "recovered": 3646
    },
    "coordinates": {
      "latitude": "62.61940309999999",
      "longitude": "33.4920267"
    },
    "province": "Karelia Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13652,
      "deaths": 185,
      "recovered": 9567
    },
    "coordinates": {
      "latitude": "54.53357809999999",
      "longitude": "87.342861"
    },
    "province": "Kemerovo Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 14512,
      "deaths": 124,
      "recovered": 10784
    },
    "coordinates": {
      "latitude": "51.6312684",
      "longitude": "136.121524"
    },
    "province": "Khabarovsk Krai"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5812,
      "deaths": 57,
      "recovered": 4685
    },
    "coordinates": {
      "latitude": "53.72258845",
      "longitude": "91.44293627"
    },
    "province": "Khakassia Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 26516,
      "deaths": 219,
      "recovered": 23104
    },
    "coordinates": {
      "latitude": "61.0259025",
      "longitude": "69.0982628"
    },
    "province": "Khanty-Mansi Autonomous Okrug"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10604,
      "deaths": 158,
      "recovered": 6569
    },
    "coordinates": {
      "latitude": "57.9665589",
      "longitude": "49.4074599"
    },
    "province": "Kirov Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11453,
      "deaths": 188,
      "recovered": 8898
    },
    "coordinates": {
      "latitude": "63.9881421",
      "longitude": "54.3326073"
    },
    "province": "Komi Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6375,
      "deaths": 96,
      "recovered": 4375
    },
    "coordinates": {
      "latitude": "58.424756",
      "longitude": "44.2533273"
    },
    "province": "Kostroma Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16237,
      "deaths": 368,
      "recovered": 11257
    },
    "coordinates": {
      "latitude": "45.7684014",
      "longitude": "39.0261044"
    },
    "province": "Krasnodar Krai"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 23944,
      "deaths": 615,
      "recovered": 17209
    },
    "coordinates": {
      "latitude": "63.3233807",
      "longitude": "97.0979974"
    },
    "province": "Krasnoyarsk Krai"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5149,
      "deaths": 69,
      "recovered": 4140
    },
    "coordinates": {
      "latitude": "55.7655302",
      "longitude": "64.5632681"
    },
    "province": "Kurgan Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9863,
      "deaths": 70,
      "recovered": 7370
    },
    "coordinates": {
      "latitude": "51.6568453",
      "longitude": "36.4852695"
    },
    "province": "Kursk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10269,
      "deaths": 107,
      "recovered": 6096
    },
    "coordinates": {
      "latitude": "60.1853296",
      "longitude": "32.3925325"
    },
    "province": "Leningrad Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7358,
      "deaths": 63,
      "recovered": 6166
    },
    "coordinates": {
      "latitude": "52.6935178",
      "longitude": "39.1122664"
    },
    "province": "Lipetsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3908,
      "deaths": 35,
      "recovered": 2855
    },
    "coordinates": {
      "latitude": "62.48858785",
      "longitude": "153.9903764"
    },
    "province": "Magadan Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5682,
      "deaths": 61,
      "recovered": 4672
    },
    "coordinates": {
      "latitude": "56.5767504",
      "longitude": "47.8817512"
    },
    "province": "Mari El Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7662,
      "deaths": 48,
      "recovered": 6351
    },
    "coordinates": {
      "latitude": "54.4419829",
      "longitude": "44.4661144"
    },
    "province": "Mordovia Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 381430,
      "deaths": 6187,
      "recovered": 282492
    },
    "coordinates": {
      "latitude": "55.7504461",
      "longitude": "37.6174943"
    },
    "province": "Moscow"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 82305,
      "deaths": 1511,
      "recovered": 61382
    },
    "coordinates": {
      "latitude": "55.50431579999999",
      "longitude": "38.0353929"
    },
    "province": "Moscow Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18136,
      "deaths": 264,
      "recovered": 14774
    },
    "coordinates": {
      "latitude": "68.00004179999999",
      "longitude": "33.9999151"
    },
    "province": "Murmansk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 402,
      "deaths": 0,
      "recovered": 142
    },
    "coordinates": {
      "latitude": "68.27557185",
      "longitude": "57.1686375"
    },
    "province": "Nenets Autonomous Okrug"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 38114,
      "deaths": 682,
      "recovered": 31941
    },
    "coordinates": {
      "latitude": "55.47180329999999",
      "longitude": "44.0911594"
    },
    "province": "Nizhny Novgorod Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6701,
      "deaths": 70,
      "recovered": 5076
    },
    "coordinates": {
      "latitude": "42.79336110000001",
      "longitude": "44.6324493"
    },
    "province": "North Ossetia - Alania Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6627,
      "deaths": 87,
      "recovered": 4308
    },
    "coordinates": {
      "latitude": "58.2843833",
      "longitude": "32.5169757"
    },
    "province": "Novgorod Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15686,
      "deaths": 548,
      "recovered": 13353
    },
    "coordinates": {
      "latitude": "54.9720169",
      "longitude": "79.48139240000002"
    },
    "province": "Novosibirsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 14070,
      "deaths": 381,
      "recovered": 11437
    },
    "coordinates": {
      "latitude": "56.09352629999999",
      "longitude": "73.5099936"
    },
    "province": "Omsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10889,
      "deaths": 147,
      "recovered": 8270
    },
    "coordinates": {
      "latitude": "52.96854329999999",
      "longitude": "36.0692477"
    },
    "province": "Orel Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15995,
      "deaths": 104,
      "recovered": 13866
    },
    "coordinates": {
      "latitude": "52.02692620000001",
      "longitude": "54.7276647"
    },
    "province": "Orenburg Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13719,
      "deaths": 159,
      "recovered": 10301
    },
    "coordinates": {
      "latitude": "53.1655415",
      "longitude": "44.78791810000001"
    },
    "province": "Penza Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12133,
      "deaths": 362,
      "recovered": 8154
    },
    "coordinates": {
      "latitude": "58.5951603",
      "longitude": "56.3159546"
    },
    "province": "Perm Krai"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13811,
      "deaths": 140,
      "recovered": 11572
    },
    "coordinates": {
      "latitude": "45.0819456",
      "longitude": "134.726645"
    },
    "province": "Primorsky Krai"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6805,
      "deaths": 68,
      "recovered": 4428
    },
    "coordinates": {
      "latitude": "57.5358729",
      "longitude": "28.8586826"
    },
    "province": "Pskov Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 27840,
      "deaths": 704,
      "recovered": 22282
    },
    "coordinates": {
      "latitude": "47.6222451",
      "longitude": "40.7957942"
    },
    "province": "Rostov Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9803,
      "deaths": 58,
      "recovered": 7209
    },
    "coordinates": {
      "latitude": "54.42267320000001",
      "longitude": "40.57052460000001"
    },
    "province": "Ryazan Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 54668,
      "deaths": 3533,
      "recovered": 34897
    },
    "coordinates": {
      "latitude": "59.9606739",
      "longitude": "30.158655100000004"
    },
    "province": "Saint Petersburg"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12030,
      "deaths": 106,
      "recovered": 7948
    },
    "coordinates": {
      "latitude": "66.941626",
      "longitude": "129.642371"
    },
    "province": "Sakha (Yakutiya) Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7023,
      "deaths": 1,
      "recovered": 4908
    },
    "coordinates": {
      "latitude": "49.7219665",
      "longitude": "143.448533"
    },
    "province": "Sakhalin Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 14564,
      "deaths": 242,
      "recovered": 11634
    },
    "coordinates": {
      "latitude": "53.2128813",
      "longitude": "50.8914633"
    },
    "province": "Samara Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18774,
      "deaths": 145,
      "recovered": 12564
    },
    "coordinates": {
      "latitude": "51.6520555",
      "longitude": "46.86319520000001"
    },
    "province": "Saratov Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7866,
      "deaths": 208,
      "recovered": 6092
    },
    "coordinates": {
      "latitude": "55.03434960000001",
      "longitude": "33.0192065"
    },
    "province": "Smolensk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 19598,
      "deaths": 391,
      "recovered": 14400
    },
    "coordinates": {
      "latitude": "44.86325770000001",
      "longitude": "43.4406913"
    },
    "province": "Stavropol Krai"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 33684,
      "deaths": 728,
      "recovered": 25799
    },
    "coordinates": {
      "latitude": "58.6414755",
      "longitude": "61.8021546"
    },
    "province": "Sverdlovsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9082,
      "deaths": 46,
      "recovered": 7349
    },
    "coordinates": {
      "latitude": "52.9019574",
      "longitude": "41.3578918"
    },
    "province": "Tambov Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7991,
      "deaths": 104,
      "recovered": 6848
    },
    "coordinates": {
      "latitude": "55.7648572",
      "longitude": "52.43104273"
    },
    "province": "Tatarstan Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10634,
      "deaths": 106,
      "recovered": 7479
    },
    "coordinates": {
      "latitude": "58.6124279",
      "longitude": "82.04753149999998"
    },
    "province": "Tomsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11427,
      "deaths": 404,
      "recovered": 10116
    },
    "coordinates": {
      "latitude": "53.9570701",
      "longitude": "37.3690909"
    },
    "province": "Tula Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8331,
      "deaths": 296,
      "recovered": 4982
    },
    "coordinates": {
      "latitude": "57.1134475",
      "longitude": "35.174442799999994"
    },
    "province": "Tver Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12134,
      "deaths": 56,
      "recovered": 8236
    },
    "coordinates": {
      "latitude": "58.8206488",
      "longitude": "70.36588370000001"
    },
    "province": "Tyumen Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8711,
      "deaths": 111,
      "recovered": 7403
    },
    "coordinates": {
      "latitude": "51.4017149",
      "longitude": "93.8582593"
    },
    "province": "Tyva Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7765,
      "deaths": 117,
      "recovered": 5724
    },
    "coordinates": {
      "latitude": "57.1961165",
      "longitude": "52.69598320000001"
    },
    "province": "Udmurt Republic"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18996,
      "deaths": 230,
      "recovered": 15064
    },
    "coordinates": {
      "latitude": "54.1463177",
      "longitude": "47.2324921"
    },
    "province": "Ulyanovsk Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8762,
      "deaths": 246,
      "recovered": 6374
    },
    "coordinates": {
      "latitude": "56.0503336",
      "longitude": "40.6561633"
    },
    "province": "Vladimir Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18554,
      "deaths": 186,
      "recovered": 16099
    },
    "coordinates": {
      "latitude": "49.6048339",
      "longitude": "44.29035820000001"
    },
    "province": "Volgograd Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6162,
      "deaths": 61,
      "recovered": 4553
    },
    "coordinates": {
      "latitude": "60.0391461",
      "longitude": "43.1215213"
    },
    "province": "Vologda Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 22556,
      "deaths": 259,
      "recovered": 19783
    },
    "coordinates": {
      "latitude": "50.9800393",
      "longitude": "40.15065070000001"
    },
    "province": "Voronezh Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18936,
      "deaths": 114,
      "recovered": 13952
    },
    "coordinates": {
      "latitude": "67.1471631",
      "longitude": "74.3415488"
    },
    "province": "Yamalo-Nenets Autonomous Okrug"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10365,
      "deaths": 55,
      "recovered": 9418
    },
    "coordinates": {
      "latitude": "57.77819760000001",
      "longitude": "39.0021095"
    },
    "province": "Yaroslavl Oblast"
  },
  {
    "country": "Russia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9508,
      "deaths": 99,
      "recovered": 6543
    },
    "coordinates": {
      "latitude": "52.248521",
      "longitude": "115.956325"
    },
    "province": "Zabaykalsky Krai"
  },
  {
    "country": "Rwanda",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5017,
      "deaths": 34,
      "recovered": 4803
    },
    "coordinates": {
      "latitude": "-1.9403",
      "longitude": "29.8739"
    },
    "province": null
  },
  {
    "country": "Saint Kitts and Nevis",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 19,
      "deaths": 0,
      "recovered": 19
    },
    "coordinates": {
      "latitude": "17.357822",
      "longitude": "-62.782998"
    },
    "province": null
  },
  {
    "country": "Saint Lucia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 42,
      "deaths": 0,
      "recovered": 27
    },
    "coordinates": {
      "latitude": "13.9094",
      "longitude": "-60.9789"
    },
    "province": null
  },
  {
    "country": "Saint Vincent and the Grenadines",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 68,
      "deaths": 0,
      "recovered": 64
    },
    "coordinates": {
      "latitude": "12.9843",
      "longitude": "-61.2872"
    },
    "province": null
  },
  {
    "country": "San Marino",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 802,
      "deaths": 42,
      "recovered": 711
    },
    "coordinates": {
      "latitude": "43.9424",
      "longitude": "12.4578"
    },
    "province": null
  },
  {
    "country": "Sao Tome and Principe",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 935,
      "deaths": 15,
      "recovered": 898
    },
    "coordinates": {
      "latitude": "0.1864",
      "longitude": "6.6131"
    },
    "province": null
  },
  {
    "country": "Saudi Arabia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 343774,
      "deaths": 5250,
      "recovered": 330181
    },
    "coordinates": {
      "latitude": "23.885942",
      "longitude": "45.079162"
    },
    "province": null
  },
  {
    "country": "Senegal",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15508,
      "deaths": 321,
      "recovered": 14026
    },
    "coordinates": {
      "latitude": "14.4974",
      "longitude": "-14.4524"
    },
    "province": null
  },
  {
    "country": "Serbia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 37536,
      "deaths": 783,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "44.0165",
      "longitude": "21.0059"
    },
    "province": null
  },
  {
    "country": "Seychelles",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 151,
      "deaths": 0,
      "recovered": 148
    },
    "coordinates": {
      "latitude": "-4.6796",
      "longitude": "55.492"
    },
    "province": null
  },
  {
    "country": "Sierra Leone",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2340,
      "deaths": 73,
      "recovered": 1777
    },
    "coordinates": {
      "latitude": "8.460555000000001",
      "longitude": "-11.779889"
    },
    "province": null
  },
  {
    "country": "Singapore",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 57941,
      "deaths": 28,
      "recovered": 57829
    },
    "coordinates": {
      "latitude": "1.2833",
      "longitude": "103.8333"
    },
    "province": null
  },
  {
    "country": "Slovakia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 35330,
      "deaths": 115,
      "recovered": 8763
    },
    "coordinates": {
      "latitude": "48.669",
      "longitude": "19.699"
    },
    "province": null
  },
  {
    "country": "Slovenia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17646,
      "deaths": 211,
      "recovered": 7299
    },
    "coordinates": {
      "latitude": "46.1512",
      "longitude": "14.9955"
    },
    "province": null
  },
  {
    "country": "Solomon Islands",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4,
      "deaths": 0,
      "recovered": 3
    },
    "coordinates": {
      "latitude": "-9.6457",
      "longitude": "160.1562"
    },
    "province": null
  },
  {
    "country": "Somalia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3897,
      "deaths": 102,
      "recovered": 3166
    },
    "coordinates": {
      "latitude": "5.152149",
      "longitude": "46.199616"
    },
    "province": null
  },
  {
    "country": "South Africa",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 710515,
      "deaths": 18843,
      "recovered": 642560
    },
    "coordinates": {
      "latitude": "-30.5595",
      "longitude": "22.9375"
    },
    "province": null
  },
  {
    "country": "South Sudan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2872,
      "deaths": 55,
      "recovered": 1290
    },
    "coordinates": {
      "latitude": "6.877000000000002",
      "longitude": "31.307"
    },
    "province": null
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 102544,
      "deaths": 2183,
      "recovered": 10671
    },
    "coordinates": {
      "latitude": "37.5443",
      "longitude": "-4.7278"
    },
    "province": "Andalusia"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 47076,
      "deaths": 1559,
      "recovered": 3772
    },
    "coordinates": {
      "latitude": "41.5976",
      "longitude": "-0.9057"
    },
    "province": "Aragon"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9109,
      "deaths": 383,
      "recovered": 1063
    },
    "coordinates": {
      "latitude": "43.3614",
      "longitude": "-5.8593"
    },
    "province": "Asturias"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16663,
      "deaths": 344,
      "recovered": 1533
    },
    "coordinates": {
      "latitude": "39.710358",
      "longitude": "2.995148"
    },
    "province": "Baleares"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 52629,
      "deaths": 1709,
      "recovered": 9970
    },
    "coordinates": {
      "latitude": "39.484",
      "longitude": "-0.7533"
    },
    "province": "C. Valenciana"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16398,
      "deaths": 266,
      "recovered": 1537
    },
    "coordinates": {
      "latitude": "28.2916",
      "longitude": "-16.6291"
    },
    "province": "Canarias"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8386,
      "deaths": 248,
      "recovered": 2287
    },
    "coordinates": {
      "latitude": "43.1828",
      "longitude": "-3.9878"
    },
    "province": "Cantabria"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 56272,
      "deaths": 3336,
      "recovered": 6392
    },
    "coordinates": {
      "latitude": "39.2796",
      "longitude": "-3.0977"
    },
    "province": "Castilla - La Mancha"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 67981,
      "deaths": 3421,
      "recovered": 8716
    },
    "coordinates": {
      "latitude": "41.8357",
      "longitude": "-4.3976"
    },
    "province": "Castilla y Leon"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 188164,
      "deaths": 5958,
      "recovered": 26203
    },
    "coordinates": {
      "latitude": "41.5912",
      "longitude": "1.5209"
    },
    "province": "Catalonia"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1106,
      "deaths": 13,
      "recovered": 163
    },
    "coordinates": {
      "latitude": "35.8894",
      "longitude": "-5.3213"
    },
    "province": "Ceuta"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 15648,
      "deaths": 670,
      "recovered": 2652
    },
    "coordinates": {
      "latitude": "39.4937",
      "longitude": "-6.0679"
    },
    "province": "Extremadura"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 28165,
      "deaths": 850,
      "recovered": 9204
    },
    "coordinates": {
      "latitude": "42.5751",
      "longitude": "-8.1339"
    },
    "province": "Galicia"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11121,
      "deaths": 441,
      "recovered": 3107
    },
    "coordinates": {
      "latitude": "42.2871",
      "longitude": "-2.5396"
    },
    "province": "La Rioja"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 290159,
      "deaths": 10155,
      "recovered": 40736
    },
    "coordinates": {
      "latitude": "40.4168",
      "longitude": "-3.7038"
    },
    "province": "Madrid"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2011,
      "deaths": 11,
      "recovered": 125
    },
    "coordinates": {
      "latitude": "35.2923",
      "longitude": "-2.9381"
    },
    "province": "Melilla"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 28779,
      "deaths": 279,
      "recovered": 2180
    },
    "coordinates": {
      "latitude": "37.9922",
      "longitude": "-1.1307"
    },
    "province": "Murcia"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 27504,
      "deaths": 666,
      "recovered": 3905
    },
    "coordinates": {
      "latitude": "42.6954",
      "longitude": "-1.6761"
    },
    "province": "Navarra"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 56566,
      "deaths": 2029,
      "recovered": 16160
    },
    "coordinates": {
      "latitude": "42.9896",
      "longitude": "-2.6189"
    },
    "province": "Pais Vasco"
  },
  {
    "country": "Spain",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 0,
      "deaths": 0,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "Sri Lanka",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6287,
      "deaths": 14,
      "recovered": 3561
    },
    "coordinates": {
      "latitude": "7.873054",
      "longitude": "80.77179699999998"
    },
    "province": null
  },
  {
    "country": "Sudan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13724,
      "deaths": 836,
      "recovered": 6764
    },
    "coordinates": {
      "latitude": "12.8628",
      "longitude": "30.2176"
    },
    "province": null
  },
  {
    "country": "Suriname",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5154,
      "deaths": 109,
      "recovered": 4995
    },
    "coordinates": {
      "latitude": "3.9193",
      "longitude": "-56.0278"
    },
    "province": null
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 892,
      "deaths": 18,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "56.2784",
      "longitude": "15.018"
    },
    "province": "Blekinge"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2957,
      "deaths": 183,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "61.0917",
      "longitude": "14.6664"
    },
    "province": "Dalarna"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3621,
      "deaths": 170,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "61.3012",
      "longitude": "16.1534"
    },
    "province": "Gavleborg"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 378,
      "deaths": 6,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "57.4684",
      "longitude": "18.4867"
    },
    "province": "Gotland"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3042,
      "deaths": 89,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "56.8967",
      "longitude": "12.8034"
    },
    "province": "Halland"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1589,
      "deaths": 64,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "63.1712",
      "longitude": "14.9592"
    },
    "province": "Jamtland Harjedalen"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6046,
      "deaths": 183,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "57.3708",
      "longitude": "14.3439"
    },
    "province": "Jonkoping"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1035,
      "deaths": 64,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "57.235",
      "longitude": "16.1849"
    },
    "province": "Kalmar"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2035,
      "deaths": 110,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "56.7183",
      "longitude": "14.4115"
    },
    "province": "Kronoberg"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2022,
      "deaths": 88,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "66.8309",
      "longitude": "20.3992"
    },
    "province": "Norrbotten"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3890,
      "deaths": 172,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "59.535",
      "longitude": "15.0066"
    },
    "province": "Orebro"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4850,
      "deaths": 279,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "58.3454",
      "longitude": "15.5198"
    },
    "province": "Ostergotland"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7831,
      "deaths": 283,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "55.9903",
      "longitude": "13.5958"
    },
    "province": "Skane"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2755,
      "deaths": 255,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "59.0336",
      "longitude": "16.7519"
    },
    "province": "Sormland"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 30392,
      "deaths": 2421,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "59.6025",
      "longitude": "18.1384"
    },
    "province": "Stockholm"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5226,
      "deaths": 247,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "60.0092",
      "longitude": "17.2715"
    },
    "province": "Uppsala"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1475,
      "deaths": 75,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "59.7294",
      "longitude": "13.2354"
    },
    "province": "Varmland"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1205,
      "deaths": 31,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "65.3337",
      "longitude": "16.5162"
    },
    "province": "Vasterbotten"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2044,
      "deaths": 137,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "63.4276",
      "longitude": "17.7292"
    },
    "province": "Vasternorrland"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3497,
      "deaths": 184,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "59.6714",
      "longitude": "16.2159"
    },
    "province": "Vastmanland"
  },
  {
    "country": "Sweden",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 22187,
      "deaths": 871,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "58.2528",
      "longitude": "13.0596"
    },
    "province": "Vastra Gotaland"
  },
  {
    "country": "Switzerland",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 97019,
      "deaths": 2046,
      "recovered": 55700
    },
    "coordinates": {
      "latitude": "46.8182",
      "longitude": "8.2275"
    },
    "province": null
  },
  {
    "country": "Syria",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5267,
      "deaths": 260,
      "recovered": 1655
    },
    "coordinates": {
      "latitude": "34.802075",
      "longitude": "38.99681500000001"
    },
    "province": null
  },
  {
    "country": "Taiwan*",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 548,
      "deaths": 7,
      "recovered": 497
    },
    "coordinates": {
      "latitude": "23.7",
      "longitude": "121.0"
    },
    "province": null
  },
  {
    "country": "Tajikistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10653,
      "deaths": 81,
      "recovered": 9724
    },
    "coordinates": {
      "latitude": "38.861",
      "longitude": "71.2761"
    },
    "province": null
  },
  {
    "country": "Tanzania",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 509,
      "deaths": 21,
      "recovered": 183
    },
    "coordinates": {
      "latitude": "-6.369028",
      "longitude": "34.888822"
    },
    "province": null
  },
  {
    "country": "Thailand",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3727,
      "deaths": 59,
      "recovered": 3518
    },
    "coordinates": {
      "latitude": "15.870032",
      "longitude": "100.992541"
    },
    "province": null
  },
  {
    "country": "Timor-Leste",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 29,
      "deaths": 0,
      "recovered": 28
    },
    "coordinates": {
      "latitude": "-8.874217",
      "longitude": "125.727539"
    },
    "province": null
  },
  {
    "country": "Togo",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2139,
      "deaths": 52,
      "recovered": 1574
    },
    "coordinates": {
      "latitude": "8.6195",
      "longitude": "0.8248"
    },
    "province": null
  },
  {
    "country": "Trinidad and Tobago",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 5446,
      "deaths": 103,
      "recovered": 3876
    },
    "coordinates": {
      "latitude": "10.6918",
      "longitude": "-61.2225"
    },
    "province": null
  },
  {
    "country": "Tunisia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 45892,
      "deaths": 740,
      "recovered": 5032
    },
    "coordinates": {
      "latitude": "33.886917",
      "longitude": "9.537499"
    },
    "province": null
  },
  {
    "country": "Turkey",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 355528,
      "deaths": 9584,
      "recovered": 310027
    },
    "coordinates": {
      "latitude": "38.9637",
      "longitude": "35.2433"
    },
    "province": null
  },
  {
    "country": "US",
    "county": null,
    "updatedAt": "2020-08-04 02:27:56",
    "stats": {
      "confirmed": 49,
      "deaths": 0,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Diamond Princess"
  },
  {
    "country": "US",
    "county": null,
    "updatedAt": "2020-08-04 02:27:56",
    "stats": {
      "confirmed": 103,
      "deaths": 3,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Grand Princess"
  },
  {
    "country": "US",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 4056,
      "deaths": 69,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "13.4443",
      "longitude": "144.7937"
    },
    "province": "Guam"
  },
  {
    "country": "US",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 88,
      "deaths": 2,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "15.0979",
      "longitude": "145.6739"
    },
    "province": "Northern Mariana Islands"
  },
  {
    "country": "US",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 0,
      "deaths": 0,
      "recovered": 3353056
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Recovered"
  },
  {
    "country": "US",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1343,
      "deaths": 21,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "18.3358",
      "longitude": "-64.8963"
    },
    "province": "Virgin Islands"
  },
  {
    "country": "Uganda",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11041,
      "deaths": 98,
      "recovered": 7210
    },
    "coordinates": {
      "latitude": "1.373333",
      "longitude": "32.290275"
    },
    "province": null
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7541,
      "deaths": 76,
      "recovered": 3058
    },
    "coordinates": {
      "latitude": "49.4444",
      "longitude": "32.0598"
    },
    "province": "Cherkasy Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7367,
      "deaths": 87,
      "recovered": 1308
    },
    "coordinates": {
      "latitude": "51.4982",
      "longitude": "31.2893"
    },
    "province": "Chernihiv Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18562,
      "deaths": 419,
      "recovered": 9688
    },
    "coordinates": {
      "latitude": "48.2917",
      "longitude": "25.9352"
    },
    "province": "Chernivtsi Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7585,
      "deaths": 115,
      "recovered": 4232
    },
    "coordinates": {
      "latitude": "45.2835",
      "longitude": "34.2008"
    },
    "province": "Crimea Republic*"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12068,
      "deaths": 285,
      "recovered": 5277
    },
    "coordinates": {
      "latitude": "48.4647",
      "longitude": "35.0462"
    },
    "province": "Dnipropetrovsk Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7896,
      "deaths": 84,
      "recovered": 1314
    },
    "coordinates": {
      "latitude": "48.0159",
      "longitude": "37.8028"
    },
    "province": "Donetsk Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 17447,
      "deaths": 399,
      "recovered": 8907
    },
    "coordinates": {
      "latitude": "48.9226",
      "longitude": "24.7111"
    },
    "province": "Ivano-Frankivsk Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 30899,
      "deaths": 472,
      "recovered": 5989
    },
    "coordinates": {
      "latitude": "49.9935",
      "longitude": "36.2304"
    },
    "province": "Kharkiv Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2844,
      "deaths": 60,
      "recovered": 1236
    },
    "coordinates": {
      "latitude": "46.6354",
      "longitude": "32.6169"
    },
    "province": "Kherson Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11942,
      "deaths": 191,
      "recovered": 5218
    },
    "coordinates": {
      "latitude": "49.423",
      "longitude": "26.9871"
    },
    "province": "Khmelnytskyi Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 32500,
      "deaths": 642,
      "recovered": 11304
    },
    "coordinates": {
      "latitude": "50.4501",
      "longitude": "30.5234"
    },
    "province": "Kiev"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13688,
      "deaths": 303,
      "recovered": 7498
    },
    "coordinates": {
      "latitude": "50.053",
      "longitude": "30.7667"
    },
    "province": "Kiev Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1786,
      "deaths": 75,
      "recovered": 1063
    },
    "coordinates": {
      "latitude": "48.5079",
      "longitude": "32.2623"
    },
    "province": "Kirovohrad Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2841,
      "deaths": 53,
      "recovered": 945
    },
    "coordinates": {
      "latitude": "48.574",
      "longitude": "39.3078"
    },
    "province": "Luhansk Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 26021,
      "deaths": 740,
      "recovered": 10248
    },
    "coordinates": {
      "latitude": "49.8397",
      "longitude": "24.0297"
    },
    "province": "Lviv Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6428,
      "deaths": 121,
      "recovered": 1581
    },
    "coordinates": {
      "latitude": "46.975",
      "longitude": "31.9946"
    },
    "province": "Mykolaiv Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 20557,
      "deaths": 311,
      "recovered": 3270
    },
    "coordinates": {
      "latitude": "46.4846",
      "longitude": "30.7326"
    },
    "province": "Odessa Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7216,
      "deaths": 134,
      "recovered": 2354
    },
    "coordinates": {
      "latitude": "49.5883",
      "longitude": "34.5514"
    },
    "province": "Poltava Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16691,
      "deaths": 206,
      "recovered": 12881
    },
    "coordinates": {
      "latitude": "50.6199",
      "longitude": "26.2516"
    },
    "province": "Rivne Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1798,
      "deaths": 55,
      "recovered": 1192
    },
    "coordinates": {
      "latitude": "44.6054",
      "longitude": "33.522"
    },
    "province": "Sevastopol*"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9730,
      "deaths": 142,
      "recovered": 2882
    },
    "coordinates": {
      "latitude": "50.9077",
      "longitude": "34.7981"
    },
    "province": "Sumy Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 18283,
      "deaths": 234,
      "recovered": 13205
    },
    "coordinates": {
      "latitude": "49.5535",
      "longitude": "25.5948"
    },
    "province": "Ternopil Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8782,
      "deaths": 153,
      "recovered": 5394
    },
    "coordinates": {
      "latitude": "49.2331",
      "longitude": "28.4682"
    },
    "province": "Vinnytsia Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11574,
      "deaths": 233,
      "recovered": 6670
    },
    "coordinates": {
      "latitude": "50.7472",
      "longitude": "25.3254"
    },
    "province": "Volyn Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 12285,
      "deaths": 343,
      "recovered": 5732
    },
    "coordinates": {
      "latitude": "48.6208",
      "longitude": "22.2879"
    },
    "province": "Zakarpattia Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 7093,
      "deaths": 97,
      "recovered": 1867
    },
    "coordinates": {
      "latitude": "47.8388",
      "longitude": "35.1396"
    },
    "province": "Zaporizhia Oblast"
  },
  {
    "country": "Ukraine",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10838,
      "deaths": 183,
      "recovered": 6009
    },
    "coordinates": {
      "latitude": "50.2547",
      "longitude": "28.6587"
    },
    "province": "Zhytomyr Oblast"
  },
  {
    "country": "United Arab Emirates",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 120710,
      "deaths": 474,
      "recovered": 113364
    },
    "coordinates": {
      "latitude": "23.424076",
      "longitude": "53.847818"
    },
    "province": null
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 3,
      "deaths": 0,
      "recovered": 3
    },
    "coordinates": {
      "latitude": "18.2206",
      "longitude": "-63.0686"
    },
    "province": "Anguilla"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 188,
      "deaths": 9,
      "recovered": 175
    },
    "coordinates": {
      "latitude": "32.3078",
      "longitude": "-64.7505"
    },
    "province": "Bermuda"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 71,
      "deaths": 1,
      "recovered": 70
    },
    "coordinates": {
      "latitude": "18.4207",
      "longitude": "-64.64"
    },
    "province": "British Virgin Islands"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 236,
      "deaths": 1,
      "recovered": 215
    },
    "coordinates": {
      "latitude": "19.3133",
      "longitude": "-81.2546"
    },
    "province": "Cayman Islands"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 784,
      "deaths": 48,
      "recovered": 659
    },
    "coordinates": {
      "latitude": "49.3723",
      "longitude": "-2.3644"
    },
    "province": "Channel Islands"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 687327,
      "deaths": 39300,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "52.3555",
      "longitude": "-1.1743"
    },
    "province": "England"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13,
      "deaths": 0,
      "recovered": 13
    },
    "coordinates": {
      "latitude": "-51.7963",
      "longitude": "-59.5236"
    },
    "province": "Falkland Islands (Malvinas)"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 630,
      "deaths": 0,
      "recovered": 495
    },
    "coordinates": {
      "latitude": "36.1408",
      "longitude": "-5.3536"
    },
    "province": "Gibraltar"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 348,
      "deaths": 24,
      "recovered": 321
    },
    "coordinates": {
      "latitude": "54.2361",
      "longitude": "-4.5481"
    },
    "province": "Isle of Man"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 13,
      "deaths": 1,
      "recovered": 12
    },
    "coordinates": {
      "latitude": "16.742498",
      "longitude": "-62.187366"
    },
    "province": "Montserrat"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 31034,
      "deaths": 634,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "54.7877",
      "longitude": "-6.4923"
    },
    "province": "Northern Ireland"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 52615,
      "deaths": 2670,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "56.4907",
      "longitude": "-4.2026"
    },
    "province": "Scotland"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 698,
      "deaths": 6,
      "recovered": 689
    },
    "coordinates": {
      "latitude": "21.694000000000006",
      "longitude": "-71.7979"
    },
    "province": "Turks and Caicos Islands"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 0,
      "deaths": 0,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "",
      "longitude": ""
    },
    "province": "Unknown"
  },
  {
    "country": "United Kingdom",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 39491,
      "deaths": 1743,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "52.1307",
      "longitude": "-3.7837"
    },
    "province": "Wales"
  },
  {
    "country": "Uruguay",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2701,
      "deaths": 53,
      "recovered": 2204
    },
    "coordinates": {
      "latitude": "-32.5228",
      "longitude": "-55.7658"
    },
    "province": null
  },
  {
    "country": "Uzbekistan",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 64439,
      "deaths": 540,
      "recovered": 61658
    },
    "coordinates": {
      "latitude": "41.377491",
      "longitude": "64.585262"
    },
    "province": null
  },
  {
    "country": "Venezuela",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 88416,
      "deaths": 759,
      "recovered": 82284
    },
    "coordinates": {
      "latitude": "6.4238",
      "longitude": "-66.5897"
    },
    "province": null
  },
  {
    "country": "Vietnam",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1148,
      "deaths": 35,
      "recovered": 1049
    },
    "coordinates": {
      "latitude": "14.058324",
      "longitude": "108.277199"
    },
    "province": null
  },
  {
    "country": "West Bank and Gaza",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 49134,
      "deaths": 435,
      "recovered": 42544
    },
    "coordinates": {
      "latitude": "31.9522",
      "longitude": "35.2332"
    },
    "province": null
  },
  {
    "country": "Western Sahara",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10,
      "deaths": 1,
      "recovered": 8
    },
    "coordinates": {
      "latitude": "24.2155",
      "longitude": "-12.8858"
    },
    "province": null
  },
  {
    "country": "Yemen",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 2057,
      "deaths": 597,
      "recovered": 1344
    },
    "coordinates": {
      "latitude": "15.552727",
      "longitude": "48.516388"
    },
    "province": null
  },
  {
    "country": "Zambia",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16035,
      "deaths": 346,
      "recovered": 15168
    },
    "coordinates": {
      "latitude": "-13.133897",
      "longitude": "27.849332"
    },
    "province": null
  },
  {
    "country": "Zimbabwe",
    "county": null,
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 8242,
      "deaths": 236,
      "recovered": 7742
    },
    "coordinates": {
      "latitude": "-19.015438",
      "longitude": "29.154857"
    },
    "province": null
  },
  {
    "country": "US",
    "county": "Autauga",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 177064,
      "deaths": 2843,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "32.53952745",
      "longitude": "-86.64408227"
    },
    "province": "Alabama"
  },
  {
    "country": "US",
    "county": "Aleutians East",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 11835,
      "deaths": 68,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "55.32222414",
      "longitude": "-161.9722021"
    },
    "province": "Alaska"
  },
  {
    "country": "US",
    "county": "Apache",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 234906,
      "deaths": 5859,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "35.39465006",
      "longitude": "-109.4892383"
    },
    "province": "Arizona"
  },
  {
    "country": "US",
    "county": "Arkansas",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 102798,
      "deaths": 1772,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "34.29145151",
      "longitude": "-91.37277296"
    },
    "province": "Arkansas"
  },
  {
    "country": "US",
    "county": "Alameda",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 893364,
      "deaths": 17256,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "37.64629437",
      "longitude": "-121.8929271"
    },
    "province": "California"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 90199,
      "deaths": 2198,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "39.87432092",
      "longitude": "-104.3362578"
    },
    "province": "Colorado"
  },
  {
    "country": "US",
    "county": "Fairfield",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 65373,
      "deaths": 4569,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "41.26809896",
      "longitude": "-73.3881171"
    },
    "province": "Connecticut"
  },
  {
    "country": "US",
    "county": "Kent",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 23528,
      "deaths": 670,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "39.08646628",
      "longitude": "-75.56884914"
    },
    "province": "Delaware"
  },
  {
    "country": "US",
    "county": "District of Columbia",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 16537,
      "deaths": 642,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "38.90417773",
      "longitude": "-77.01655992"
    },
    "province": "District of Columbia"
  },
  {
    "country": "US",
    "county": "Alachua",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 768091,
      "deaths": 16267,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "29.67866525",
      "longitude": "-82.35928158"
    },
    "province": "Florida"
  },
  {
    "country": "US",
    "county": "Appling",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 345535,
      "deaths": 7729,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "31.74847232",
      "longitude": "-82.28909114"
    },
    "province": "Georgia"
  },
  {
    "country": "US",
    "county": "Hawaii",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 14335,
      "deaths": 206,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "19.60121157",
      "longitude": "-155.5210167"
    },
    "province": "Hawaii"
  },
  {
    "country": "US",
    "county": "Ada",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 56600,
      "deaths": 553,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "43.4526575",
      "longitude": "-116.24155159999998"
    },
    "province": "Idaho"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 363740,
      "deaths": 9647,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "39.98815591",
      "longitude": "-91.18786813"
    },
    "province": "Illinois"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 155246,
      "deaths": 4065,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "40.7457653",
      "longitude": "-84.93671406"
    },
    "province": "Indiana"
  },
  {
    "country": "US",
    "county": "Adair",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 111733,
      "deaths": 1601,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "41.33075609",
      "longitude": "-94.47105874"
    },
    "province": "Iowa"
  },
  {
    "country": "US",
    "county": "Allen",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 74068,
      "deaths": 937,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "37.88582951",
      "longitude": "-95.30030847"
    },
    "province": "Kansas"
  },
  {
    "country": "US",
    "county": "Adair",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 92299,
      "deaths": 1380,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "37.10459774",
      "longitude": "-85.28129668"
    },
    "province": "Kentucky"
  },
  {
    "country": "US",
    "county": "Acadia",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 178171,
      "deaths": 5799,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "30.2950649",
      "longitude": "-92.41419698"
    },
    "province": "Louisiana"
  },
  {
    "country": "US",
    "county": "Androscoggin",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 6063,
      "deaths": 146,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "44.1664747",
      "longitude": "-70.20380627"
    },
    "province": "Maine"
  },
  {
    "country": "US",
    "county": "Allegany",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 137979,
      "deaths": 4070,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "39.62357628",
      "longitude": "-78.69280486"
    },
    "province": "Maryland"
  },
  {
    "country": "US",
    "county": "Barnstable",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 147215,
      "deaths": 9810,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "41.72980578",
      "longitude": "-70.28854339"
    },
    "province": "Massachusetts"
  },
  {
    "country": "US",
    "county": "Alcona",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 170076,
      "deaths": 7464,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "44.6846864",
      "longitude": "-83.59507875"
    },
    "province": "Michigan"
  },
  {
    "country": "US",
    "county": "Aitkin",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 128152,
      "deaths": 2354,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "46.60962049",
      "longitude": "-93.4116826"
    },
    "province": "Minnesota"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 113081,
      "deaths": 3231,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "31.47669768",
      "longitude": "-91.35326037"
    },
    "province": "Mississippi"
  },
  {
    "country": "US",
    "county": "Adair",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 165210,
      "deaths": 2665,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "40.19058551",
      "longitude": "-92.60078167"
    },
    "province": "Missouri"
  },
  {
    "country": "US",
    "county": "Beaverhead",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 25640,
      "deaths": 278,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "45.13434354",
      "longitude": "-112.8984694"
    },
    "province": "Montana"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 61285,
      "deaths": 587,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "40.52449420000001",
      "longitude": "-98.50117804"
    },
    "province": "Nebraska"
  },
  {
    "country": "US",
    "county": "Carson City",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 92853,
      "deaths": 1736,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "39.15509045",
      "longitude": "-119.7480219"
    },
    "province": "Nevada"
  },
  {
    "country": "US",
    "county": "Belknap",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 9994,
      "deaths": 470,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "43.51637314",
      "longitude": "-71.41684235"
    },
    "province": "New Hampshire"
  },
  {
    "country": "US",
    "county": "Atlantic",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 224385,
      "deaths": 16263,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "39.47538693",
      "longitude": "-74.65848483"
    },
    "province": "New Jersey"
  },
  {
    "country": "US",
    "county": "Bernalillo",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 39377,
      "deaths": 953,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "35.05163625",
      "longitude": "-106.6703554"
    },
    "province": "New Mexico"
  },
  {
    "country": "US",
    "county": "Albany",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 490134,
      "deaths": 33396,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "42.60060306",
      "longitude": "-73.97723916"
    },
    "province": "New York"
  },
  {
    "country": "US",
    "county": "Alamance",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 252992,
      "deaths": 4082,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "36.0434701",
      "longitude": "-79.39976137"
    },
    "province": "North Carolina"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 35052,
      "deaths": 431,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "46.09686891",
      "longitude": "-102.5285397"
    },
    "province": "North Dakota"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 190430,
      "deaths": 5161,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "38.84541072",
      "longitude": "-83.4718964"
    },
    "province": "Ohio"
  },
  {
    "country": "US",
    "county": "Adair",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 112483,
      "deaths": 1221,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "35.88494195",
      "longitude": "-94.65859267"
    },
    "province": "Oklahoma"
  },
  {
    "country": "US",
    "county": "Baker",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 40443,
      "deaths": 635,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "44.70915557",
      "longitude": "-117.6749883"
    },
    "province": "Oregon"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 193401,
      "deaths": 8574,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "39.87140411",
      "longitude": "-77.21610347"
    },
    "province": "Pennsylvania"
  },
  {
    "country": "US",
    "county": "Adjuntas",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 59037,
      "deaths": 783,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "18.180117000000006",
      "longitude": "-66.754367"
    },
    "province": "Puerto Rico"
  },
  {
    "country": "US",
    "county": "Bristol",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 29594,
      "deaths": 1173,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "41.71018079",
      "longitude": "-71.28652315"
    },
    "province": "Rhode Island"
  },
  {
    "country": "US",
    "county": "Abbeville",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 167485,
      "deaths": 3755,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "34.22333378",
      "longitude": "-82.46170658"
    },
    "province": "South Carolina"
  },
  {
    "country": "US",
    "county": "Aurora",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 36017,
      "deaths": 347,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "43.71757685",
      "longitude": "-98.56050467"
    },
    "province": "South Dakota"
  },
  {
    "country": "US",
    "county": "Anderson",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 237907,
      "deaths": 3011,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "36.12684348",
      "longitude": "-84.19965764"
    },
    "province": "Tennessee"
  },
  {
    "country": "US",
    "county": "Anderson",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 871453,
      "deaths": 17659,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "31.81534745",
      "longitude": "-95.65354823"
    },
    "province": "Texas"
  },
  {
    "country": "US",
    "county": "Bear River",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 99549,
      "deaths": 563,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "41.52106798",
      "longitude": "-113.0832816"
    },
    "province": "Utah"
  },
  {
    "country": "US",
    "county": "Addison",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 1987,
      "deaths": 58,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "44.03217337",
      "longitude": "-73.14130877"
    },
    "province": "Vermont"
  },
  {
    "country": "US",
    "county": "Accomack",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 169566,
      "deaths": 3520,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "37.76707161",
      "longitude": "-75.63234615"
    },
    "province": "Virginia"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 100525,
      "deaths": 2289,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "46.98299757",
      "longitude": "-118.5601734"
    },
    "province": "Washington"
  },
  {
    "country": "US",
    "county": "Barbour",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 21057,
      "deaths": 420,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "39.1307219",
      "longitude": "-80.00350858"
    },
    "province": "West Virginia"
  },
  {
    "country": "US",
    "county": "Adams",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 186100,
      "deaths": 1703,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "43.96974651",
      "longitude": "-89.76782777"
    },
    "province": "Wisconsin"
  },
  {
    "country": "US",
    "county": "Albany",
    "updatedAt": "2020-10-23 04:24:46",
    "stats": {
      "confirmed": 10119,
      "deaths": 68,
      "recovered": 0
    },
    "coordinates": {
      "latitude": "41.65498705",
      "longitude": "-105.7235415"
    },
    "province": "Wyoming"
  }
]'''


class JHUCSSEHistoricalWorldData:
    def __init__(self):
        self.request_url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
        self.example_response = '''{
  "cases": {
    "1/22/20": 555,
    "1/23/20": 654,
    "1/24/20": 941,
    "1/25/20": 1434,
    "1/26/20": 2118,
    "1/27/20": 2927,
    "1/28/20": 5578,
    "1/29/20": 6167,
    "1/30/20": 8235,
    "1/31/20": 9927,
    "2/1/20": 12038,
    "2/2/20": 16787,
    "2/3/20": 19887,
    "2/4/20": 23898,
    "2/5/20": 27643,
    "2/6/20": 30803,
    "2/7/20": 34396,
    "2/8/20": 37130,
    "2/9/20": 40160,
    "2/10/20": 42769,
    "2/11/20": 44811,
    "2/12/20": 45229,
    "2/13/20": 60382,
    "2/14/20": 66909,
    "2/15/20": 69051,
    "2/16/20": 71235,
    "2/17/20": 73270,
    "2/18/20": 75152,
    "2/19/20": 75652,
    "2/20/20": 76212,
    "2/21/20": 76841,
    "2/22/20": 78602,
    "2/23/20": 78982,
    "2/24/20": 79546,
    "2/25/20": 80399,
    "2/26/20": 81376,
    "2/27/20": 82736,
    "2/28/20": 84121,
    "2/29/20": 86014,
    "3/1/20": 88397,
    "3/2/20": 90375,
    "3/3/20": 92959,
    "3/4/20": 95276,
    "3/5/20": 98040,
    "3/6/20": 102040,
    "3/7/20": 106102,
    "3/8/20": 110062,
    "3/9/20": 114025,
    "3/10/20": 119036,
    "3/11/20": 126717,
    "3/12/20": 132506,
    "3/13/20": 146887,
    "3/14/20": 157965,
    "3/15/20": 169258,
    "3/16/20": 184002,
    "3/17/20": 199932,
    "3/18/20": 219462,
    "3/19/20": 246618,
    "3/20/20": 277253,
    "3/21/20": 309223,
    "3/22/20": 343456,
    "3/23/20": 386823,
    "3/24/20": 428295,
    "3/25/20": 479279,
    "3/26/20": 542006,
    "3/27/20": 606988,
    "3/28/20": 674380,
    "3/29/20": 733777,
    "3/30/20": 799018,
    "3/31/20": 875842,
    "4/1/20": 952368,
    "4/2/20": 1033702,
    "4/3/20": 1116958,
    "4/4/20": 1197315,
    "4/5/20": 1269291,
    "4/6/20": 1342524,
    "4/7/20": 1420265,
    "4/8/20": 1504296,
    "4/9/20": 1590776,
    "4/10/20": 1678316,
    "4/11/20": 1754531,
    "4/12/20": 1849884,
    "4/13/20": 1920029,
    "4/14/20": 1991375,
    "4/15/20": 2073248,
    "4/16/20": 2170168,
    "4/17/20": 2257981,
    "4/18/20": 2331375,
    "4/19/20": 2411347,
    "4/20/20": 2485850,
    "4/21/20": 2561729,
    "4/22/20": 2639748,
    "4/23/20": 2727991,
    "4/24/20": 2812178,
    "4/25/20": 2895859,
    "4/26/20": 2968049,
    "4/27/20": 3037754,
    "4/28/20": 3113246,
    "4/29/20": 3190735,
    "4/30/20": 3274139,
    "5/1/20": 3361356,
    "5/2/20": 3441576,
    "5/3/20": 3518135,
    "5/4/20": 3595235,
    "5/5/20": 3675767,
    "5/6/20": 3765725,
    "5/7/20": 3854800,
    "5/8/20": 3946080,
    "5/9/20": 4031014,
    "5/10/20": 4106229,
    "5/11/20": 4183146,
    "5/12/20": 4267441,
    "5/13/20": 4352288,
    "5/14/20": 4449054,
    "5/15/20": 4545482,
    "5/16/20": 4639704,
    "5/17/20": 4717128,
    "5/18/20": 4805859,
    "5/19/20": 4903092,
    "5/20/20": 5005903,
    "5/21/20": 5112508,
    "5/22/20": 5218600,
    "5/23/20": 5323287,
    "5/24/20": 5417853,
    "5/25/20": 5504248,
    "5/26/20": 5597560,
    "5/27/20": 5700620,
    "5/28/20": 5820202,
    "5/29/20": 5941244,
    "5/30/20": 6078261,
    "5/31/20": 6184917,
    "6/1/20": 6280511,
    "6/2/20": 6401952,
    "6/3/20": 6520126,
    "6/4/20": 6647409,
    "6/5/20": 6778310,
    "6/6/20": 6913202,
    "6/7/20": 7025172,
    "6/8/20": 7127703,
    "6/9/20": 7252461,
    "6/10/20": 7387034,
    "6/11/20": 7525216,
    "6/12/20": 7653814,
    "6/13/20": 7789270,
    "6/14/20": 7922027,
    "6/15/20": 8041844,
    "6/16/20": 8183744,
    "6/17/20": 8326301,
    "6/18/20": 8466697,
    "6/19/20": 8646596,
    "6/20/20": 8803922,
    "6/21/20": 8932267,
    "6/22/20": 9070200,
    "6/23/20": 9235569,
    "6/24/20": 9406545,
    "6/25/20": 9584905,
    "6/26/20": 9776335,
    "6/27/20": 9954911,
    "6/28/20": 10116803,
    "6/29/20": 10273032,
    "6/30/20": 10447289,
    "7/1/20": 10664533,
    "7/2/20": 10872669,
    "7/3/20": 11075391,
    "7/4/20": 11269302,
    "7/5/20": 11452292,
    "7/6/20": 11617941,
    "7/7/20": 11828915,
    "7/8/20": 12041312,
    "7/9/20": 12269423,
    "7/10/20": 12501740,
    "7/11/20": 12718142,
    "7/12/20": 12910765,
    "7/13/20": 13103070,
    "7/14/20": 13324389,
    "7/15/20": 13555611,
    "7/16/20": 13808279,
    "7/17/20": 14050533,
    "7/18/20": 14287418,
    "7/19/20": 14501583,
    "7/20/20": 14708250,
    "7/21/20": 14941878,
    "7/22/20": 15222711,
    "7/23/20": 15505806,
    "7/24/20": 15786391,
    "7/25/20": 16042089,
    "7/26/20": 16255260,
    "7/27/20": 16481553,
    "7/28/20": 16733998,
    "7/29/20": 17023686,
    "7/30/20": 17304066,
    "7/31/20": 17594389,
    "8/1/20": 17845046,
    "8/2/20": 18073489,
    "8/3/20": 18275011,
    "8/4/20": 18533677,
    "8/5/20": 18805967,
    "8/6/20": 19090844,
    "8/7/20": 19371914,
    "8/8/20": 19631350,
    "8/9/20": 19854976,
    "8/10/20": 20082310,
    "8/11/20": 20337403,
    "8/12/20": 20615476,
    "8/13/20": 20901672,
    "8/14/20": 21206137,
    "8/15/20": 21454001,
    "8/16/20": 21666057,
    "8/17/20": 21876108,
    "8/18/20": 22132478,
    "8/19/20": 22407067,
    "8/20/20": 22674400,
    "8/21/20": 22944256,
    "8/22/20": 23209748,
    "8/23/20": 23415376,
    "8/24/20": 23641786,
    "8/25/20": 23883773,
    "8/26/20": 24172773,
    "8/27/20": 24452017,
    "8/28/20": 24733680,
    "8/29/20": 24994670,
    "8/30/20": 25221059,
    "8/31/20": 25483593,
    "9/1/20": 25747891,
    "9/2/20": 26030704,
    "9/3/20": 26311640,
    "9/4/20": 26624479,
    "9/5/20": 26887771,
    "9/6/20": 27109897,
    "9/7/20": 27343696,
    "9/8/20": 27585104,
    "9/9/20": 27869487,
    "9/10/20": 28168782,
    "9/11/20": 28488690,
    "9/12/20": 28766035,
    "9/13/20": 29002159,
    "9/14/20": 29281907,
    "9/15/20": 29565771,
    "9/16/20": 29870696,
    "9/17/20": 30184473,
    "9/18/20": 30507945,
    "9/19/20": 30789093,
    "9/20/20": 31029890,
    "9/21/20": 31329271,
    "9/22/20": 31608522,
    "9/23/20": 31875596,
    "9/24/20": 32236615,
    "9/25/20": 32566990,
    "9/26/20": 32844468,
    "9/27/20": 33084725,
    "9/28/20": 33361813,
    "9/29/20": 33645851,
    "9/30/20": 33972874,
    "10/1/20": 34290251,
    "10/2/20": 34585720,
    "10/3/20": 34905722,
    "10/4/20": 35153599,
    "10/5/20": 35483630,
    "10/6/20": 35806972,
    "10/7/20": 36156226,
    "10/8/20": 36515696,
    "10/9/20": 36876568,
    "10/10/20": 37207452,
    "10/11/20": 37475928,
    "10/12/20": 37802138,
    "10/13/20": 38130527,
    "10/14/20": 38511143,
    "10/15/20": 38917803,
    "10/16/20": 39329140,
    "10/17/20": 39670828,
    "10/18/20": 39955637,
    "10/19/20": 40395527,
    "10/20/20": 40783425,
    "10/21/20": 41227176,
    "10/22/20": 41695675
  },
  "deaths": {
    "1/22/20": 17,
    "1/23/20": 18,
    "1/24/20": 26,
    "1/25/20": 42,
    "1/26/20": 56,
    "1/27/20": 82,
    "1/28/20": 131,
    "1/29/20": 133,
    "1/30/20": 171,
    "1/31/20": 213,
    "2/1/20": 259,
    "2/2/20": 362,
    "2/3/20": 426,
    "2/4/20": 492,
    "2/5/20": 564,
    "2/6/20": 634,
    "2/7/20": 719,
    "2/8/20": 806,
    "2/9/20": 906,
    "2/10/20": 1013,
    "2/11/20": 1113,
    "2/12/20": 1118,
    "2/13/20": 1371,
    "2/14/20": 1523,
    "2/15/20": 1666,
    "2/16/20": 1770,
    "2/17/20": 1868,
    "2/18/20": 2008,
    "2/19/20": 2123,
    "2/20/20": 2248,
    "2/21/20": 2252,
    "2/22/20": 2459,
    "2/23/20": 2470,
    "2/24/20": 2630,
    "2/25/20": 2710,
    "2/26/20": 2771,
    "2/27/20": 2814,
    "2/28/20": 2873,
    "2/29/20": 2942,
    "3/1/20": 2996,
    "3/2/20": 3085,
    "3/3/20": 3160,
    "3/4/20": 3255,
    "3/5/20": 3348,
    "3/6/20": 3460,
    "3/7/20": 3559,
    "3/8/20": 3803,
    "3/9/20": 3987,
    "3/10/20": 4267,
    "3/11/20": 4611,
    "3/12/20": 4917,
    "3/13/20": 5414,
    "3/14/20": 5834,
    "3/15/20": 6475,
    "3/16/20": 7153,
    "3/17/20": 7964,
    "3/18/20": 8867,
    "3/19/20": 9981,
    "3/20/20": 11460,
    "3/21/20": 13181,
    "3/22/20": 14855,
    "3/23/20": 16798,
    "3/24/20": 19080,
    "3/25/20": 21878,
    "3/26/20": 24894,
    "3/27/20": 28389,
    "3/28/20": 32102,
    "3/29/20": 35572,
    "3/30/20": 39620,
    "3/31/20": 44368,
    "4/1/20": 49864,
    "4/2/20": 56101,
    "4/3/20": 62202,
    "4/4/20": 68355,
    "4/5/20": 73537,
    "4/6/20": 79478,
    "4/7/20": 87709,
    "4/8/20": 94461,
    "4/9/20": 102234,
    "4/10/20": 109626,
    "4/11/20": 115861,
    "4/12/20": 121671,
    "4/13/20": 127587,
    "4/14/20": 134564,
    "4/15/20": 142915,
    "4/16/20": 150218,
    "4/17/20": 158585,
    "4/18/20": 164598,
    "4/19/20": 169859,
    "4/20/20": 175723,
    "4/21/20": 182914,
    "4/22/20": 189641,
    "4/23/20": 196485,
    "4/24/20": 203142,
    "4/25/20": 208774,
    "4/26/20": 212708,
    "4/27/20": 217382,
    "4/28/20": 223929,
    "4/29/20": 230657,
    "4/30/20": 236657,
    "5/1/20": 241807,
    "5/2/20": 247285,
    "5/3/20": 250750,
    "5/4/20": 254843,
    "5/5/20": 260735,
    "5/6/20": 267283,
    "5/7/20": 272579,
    "5/8/20": 278054,
    "5/9/20": 282349,
    "5/10/20": 285932,
    "5/11/20": 289404,
    "5/12/20": 294925,
    "5/13/20": 299999,
    "5/14/20": 305183,
    "5/15/20": 310305,
    "5/16/20": 314483,
    "5/17/20": 317761,
    "5/18/20": 321454,
    "5/19/20": 326174,
    "5/20/20": 330936,
    "5/21/20": 335657,
    "5/22/20": 340851,
    "5/23/20": 344764,
    "5/24/20": 347881,
    "5/25/20": 349073,
    "5/26/20": 353180,
    "5/27/20": 358326,
    "5/28/20": 362944,
    "5/29/20": 367536,
    "5/30/20": 371610,
    "5/31/20": 374585,
    "6/1/20": 377659,
    "6/2/20": 382389,
    "6/3/20": 387828,
    "6/4/20": 392948,
    "6/5/20": 397506,
    "6/6/20": 401365,
    "6/7/20": 404106,
    "6/8/20": 407780,
    "6/9/20": 412626,
    "6/10/20": 417683,
    "6/11/20": 422371,
    "6/12/20": 426584,
    "6/13/20": 430772,
    "6/14/20": 434179,
    "6/15/20": 437591,
    "6/16/20": 444312,
    "6/17/20": 449403,
    "6/18/20": 454386,
    "6/19/20": 460545,
    "6/20/20": 464760,
    "6/21/20": 468761,
    "6/22/20": 472316,
    "6/23/20": 477540,
    "6/24/20": 482712,
    "6/25/20": 487411,
    "6/26/20": 492109,
    "6/27/20": 496574,
    "6/28/20": 499712,
    "6/29/20": 503435,
    "6/30/20": 508391,
    "7/1/20": 513315,
    "7/2/20": 518382,
    "7/3/20": 523317,
    "7/4/20": 527681,
    "7/5/20": 531153,
    "7/6/20": 534974,
    "7/7/20": 540995,
    "7/8/20": 546266,
    "7/9/20": 551676,
    "7/10/20": 556969,
    "7/11/20": 561761,
    "7/12/20": 565751,
    "7/13/20": 569556,
    "7/14/20": 575150,
    "7/15/20": 580582,
    "7/16/20": 586332,
    "7/17/20": 592988,
    "7/18/20": 598610,
    "7/19/20": 602662,
    "7/20/20": 606829,
    "7/21/20": 612998,
    "7/22/20": 619920,
    "7/23/20": 629817,
    "7/24/20": 635852,
    "7/25/20": 641398,
    "7/26/20": 645058,
    "7/27/20": 650233,
    "7/28/20": 656545,
    "7/29/20": 663118,
    "7/30/20": 669124,
    "7/31/20": 675341,
    "8/1/20": 680833,
    "8/2/20": 685100,
    "8/3/20": 689412,
    "8/4/20": 696332,
    "8/5/20": 703298,
    "8/6/20": 709793,
    "8/7/20": 716095,
    "8/8/20": 721523,
    "8/9/20": 726075,
    "8/10/20": 730983,
    "8/11/20": 737413,
    "8/12/20": 744030,
    "8/13/20": 750246,
    "8/14/20": 760370,
    "8/15/20": 765721,
    "8/16/20": 769920,
    "8/17/20": 774060,
    "8/18/20": 780938,
    "8/19/20": 787694,
    "8/20/20": 793732,
    "8/21/20": 799224,
    "8/22/20": 804804,
    "8/23/20": 808656,
    "8/24/20": 813014,
    "8/25/20": 819396,
    "8/26/20": 825684,
    "8/27/20": 831576,
    "8/28/20": 837091,
    "8/29/20": 842472,
    "8/30/20": 846381,
    "8/31/20": 850591,
    "9/1/20": 857077,
    "9/2/20": 863095,
    "9/3/20": 868805,
    "9/4/20": 874714,
    "9/5/20": 879659,
    "9/6/20": 883428,
    "9/7/20": 892740,
    "9/8/20": 897679,
    "9/9/20": 903766,
    "9/10/20": 909574,
    "9/11/20": 915454,
    "9/12/20": 920332,
    "9/13/20": 923981,
    "9/14/20": 928415,
    "9/15/20": 934965,
    "9/16/20": 940722,
    "9/17/20": 946181,
    "9/18/20": 951890,
    "9/19/20": 957125,
    "9/20/20": 960821,
    "9/21/20": 964873,
    "9/22/20": 970753,
    "9/23/20": 976362,
    "9/24/20": 983077,
    "9/25/20": 988993,
    "9/26/20": 994274,
    "9/27/20": 997876,
    "9/28/20": 1001797,
    "9/29/20": 1007892,
    "9/30/20": 1014298,
    "10/1/20": 1022998,
    "10/2/20": 1027966,
    "10/3/20": 1033319,
    "10/4/20": 1037083,
    "10/5/20": 1044090,
    "10/6/20": 1049875,
    "10/7/20": 1055683,
    "10/8/20": 1061927,
    "10/9/20": 1068045,
    "10/10/20": 1072868,
    "10/11/20": 1076762,
    "10/12/20": 1080685,
    "10/13/20": 1086146,
    "10/14/20": 1092149,
    "10/15/20": 1098254,
    "10/16/20": 1104354,
    "10/17/20": 1109833,
    "10/18/20": 1113178,
    "10/19/20": 1118159,
    "10/20/20": 1124745,
    "10/21/20": 1131308,
    "10/22/20": 1137193
  },
  "recovered": {
    "1/22/20": 28,
    "1/23/20": 30,
    "1/24/20": 36,
    "1/25/20": 39,
    "1/26/20": 52,
    "1/27/20": 61,
    "1/28/20": 107,
    "1/29/20": 126,
    "1/30/20": 143,
    "1/31/20": 222,
    "2/1/20": 284,
    "2/2/20": 472,
    "2/3/20": 623,
    "2/4/20": 852,
    "2/5/20": 1124,
    "2/6/20": 1487,
    "2/7/20": 2011,
    "2/8/20": 2616,
    "2/9/20": 3244,
    "2/10/20": 3946,
    "2/11/20": 4683,
    "2/12/20": 5149,
    "2/13/20": 6294,
    "2/14/20": 8057,
    "2/15/20": 9394,
    "2/16/20": 10864,
    "2/17/20": 12582,
    "2/18/20": 14351,
    "2/19/20": 16120,
    "2/20/20": 18176,
    "2/21/20": 18887,
    "2/22/20": 22883,
    "2/23/20": 23391,
    "2/24/20": 25224,
    "2/25/20": 27902,
    "2/26/20": 30381,
    "2/27/20": 33271,
    "2/28/20": 36705,
    "2/29/20": 39776,
    "3/1/20": 42710,
    "3/2/20": 45596,
    "3/3/20": 48222,
    "3/4/20": 51164,
    "3/5/20": 53790,
    "3/6/20": 55859,
    "3/7/20": 58351,
    "3/8/20": 60686,
    "3/9/20": 62485,
    "3/10/20": 64396,
    "3/11/20": 66994,
    "3/12/20": 68316,
    "3/13/20": 70243,
    "3/14/20": 72614,
    "3/15/20": 76024,
    "3/16/20": 78077,
    "3/17/20": 80829,
    "3/18/20": 83312,
    "3/19/20": 84949,
    "3/20/20": 87394,
    "3/21/20": 91660,
    "3/22/20": 97875,
    "3/23/20": 98341,
    "3/24/20": 107882,
    "3/25/20": 113592,
    "3/26/20": 121961,
    "3/27/20": 130665,
    "3/28/20": 138958,
    "3/29/20": 148425,
    "3/30/20": 163871,
    "3/31/20": 176233,
    "4/1/20": 191594,
    "4/2/20": 208232,
    "4/3/20": 223240,
    "4/4/20": 243255,
    "4/5/20": 256660,
    "4/6/20": 272996,
    "4/7/20": 295852,
    "4/8/20": 324205,
    "4/9/20": 348545,
    "4/10/20": 369654,
    "4/11/20": 395177,
    "4/12/20": 414057,
    "4/13/20": 440589,
    "4/14/20": 465226,
    "4/15/20": 501140,
    "4/16/20": 531228,
    "4/17/20": 556504,
    "4/18/20": 580004,
    "4/19/20": 610776,
    "4/20/20": 632070,
    "4/21/20": 666268,
    "4/22/20": 695427,
    "4/23/20": 723900,
    "4/24/20": 773563,
    "4/25/20": 800478,
    "4/26/20": 828213,
    "4/27/20": 854597,
    "4/28/20": 886905,
    "4/29/20": 927991,
    "4/30/20": 991860,
    "5/1/20": 1028773,
    "5/2/20": 1068602,
    "5/3/20": 1099811,
    "5/4/20": 1132789,
    "5/5/20": 1168353,
    "5/6/20": 1213181,
    "5/7/20": 1251573,
    "5/8/20": 1287144,
    "5/9/20": 1339671,
    "5/10/20": 1372418,
    "5/11/20": 1418514,
    "5/12/20": 1454487,
    "5/13/20": 1509221,
    "5/14/20": 1548010,
    "5/15/20": 1595214,
    "5/16/20": 1650882,
    "5/17/20": 1691058,
    "5/18/20": 1743291,
    "5/19/20": 1794578,
    "5/20/20": 1852782,
    "5/21/20": 1903109,
    "5/22/20": 2010883,
    "5/23/20": 2065144,
    "5/24/20": 2119904,
    "5/25/20": 2182974,
    "5/26/20": 2237487,
    "5/27/20": 2299984,
    "5/28/20": 2366128,
    "5/29/20": 2442530,
    "5/30/20": 2512371,
    "5/31/20": 2587995,
    "6/1/20": 2642014,
    "6/2/20": 2745503,
    "6/3/20": 2823826,
    "6/4/20": 2893201,
    "6/5/20": 2961470,
    "6/6/20": 3032661,
    "6/7/20": 3087174,
    "6/8/20": 3238069,
    "6/9/20": 3319577,
    "6/10/20": 3397617,
    "6/11/20": 3482583,
    "6/12/20": 3561404,
    "6/13/20": 3646521,
    "6/14/20": 3716489,
    "6/15/20": 3795899,
    "6/16/20": 3893306,
    "6/17/20": 4010712,
    "6/18/20": 4091352,
    "6/19/20": 4185831,
    "6/20/20": 4301148,
    "6/21/20": 4369462,
    "6/22/20": 4460616,
    "6/23/20": 4564277,
    "6/24/20": 4679639,
    "6/25/20": 4772159,
    "6/26/20": 4878560,
    "6/27/20": 4984662,
    "6/28/20": 5073538,
    "6/29/20": 5167095,
    "6/30/20": 5283995,
    "7/1/20": 5399644,
    "7/2/20": 5684046,
    "7/3/20": 5793586,
    "7/4/20": 5989144,
    "7/5/20": 6108201,
    "7/6/20": 6231444,
    "7/7/20": 6376192,
    "7/8/20": 6533754,
    "7/9/20": 6667978,
    "7/10/20": 6806999,
    "7/11/20": 6932390,
    "7/12/20": 7043899,
    "7/13/20": 7183816,
    "7/14/20": 7325684,
    "7/15/20": 7485111,
    "7/16/20": 7637115,
    "7/17/20": 7796577,
    "7/18/20": 7947379,
    "7/19/20": 8035128,
    "7/20/20": 8193713,
    "7/21/20": 8368087,
    "7/22/20": 8544221,
    "7/23/20": 8713949,
    "7/24/20": 8942699,
    "7/25/20": 9161755,
    "7/26/20": 9302027,
    "7/27/20": 9471172,
    "7/28/20": 9644787,
    "7/29/20": 9846171,
    "7/30/20": 10068306,
    "7/31/20": 10266349,
    "8/1/20": 10450780,
    "8/2/20": 10587354,
    "8/3/20": 10809716,
    "8/4/20": 11030677,
    "8/5/20": 11252054,
    "8/6/20": 11440723,
    "8/7/20": 11632924,
    "8/8/20": 11834176,
    "8/9/20": 12010869,
    "8/10/20": 12172470,
    "8/11/20": 12477198,
    "8/12/20": 12718339,
    "8/13/20": 12883121,
    "8/14/20": 13167174,
    "8/15/20": 13335911,
    "8/16/20": 13566898,
    "8/17/20": 13778252,
    "8/18/20": 14005580,
    "8/19/20": 14222698,
    "8/20/20": 14430350,
    "8/21/20": 14599873,
    "8/22/20": 14809755,
    "8/23/20": 15024776,
    "8/24/20": 15224364,
    "8/25/20": 15456791,
    "8/26/20": 15680883,
    "8/27/20": 15882199,
    "8/28/20": 16082358,
    "8/29/20": 16293834,
    "8/30/20": 16502222,
    "8/31/20": 16703225,
    "9/1/20": 16957810,
    "9/2/20": 17176145,
    "9/3/20": 17396635,
    "9/4/20": 17610095,
    "9/5/20": 17810872,
    "9/6/20": 18020878,
    "9/7/20": 18219583,
    "9/8/20": 18419412,
    "9/9/20": 18659074,
    "9/10/20": 18873782,
    "9/11/20": 19096627,
    "9/12/20": 19319699,
    "9/13/20": 19505318,
    "9/14/20": 19734071,
    "9/15/20": 19958200,
    "9/16/20": 20186689,
    "9/17/20": 20405603,
    "9/18/20": 20656875,
    "9/19/20": 20894482,
    "9/20/20": 21130007,
    "9/21/20": 21372265,
    "9/22/20": 21589319,
    "9/23/20": 21852080,
    "9/24/20": 22106105,
    "9/25/20": 22344699,
    "9/26/20": 22587506,
    "9/27/20": 22796955,
    "9/28/20": 23021164,
    "9/29/20": 23256631,
    "9/30/20": 23504751,
    "10/1/20": 23723999,
    "10/2/20": 23894627,
    "10/3/20": 24151919,
    "10/4/20": 24368329,
    "10/5/20": 24605065,
    "10/6/20": 24834868,
    "10/7/20": 25088883,
    "10/8/20": 25306497,
    "10/9/20": 25509440,
    "10/10/20": 25699675,
    "10/11/20": 25915457,
    "10/12/20": 26118771,
    "10/13/20": 26305933,
    "10/14/20": 26516041,
    "10/15/20": 26721132,
    "10/16/20": 26923627,
    "10/17/20": 27122176,
    "10/18/20": 27317865,
    "10/19/20": 27525512,
    "10/20/20": 27733819,
    "10/21/20": 27948066,
    "10/22/20": 28172518
  }
}'''


class GovtData:
    def __init__(self):
        self.request_url = "https://disease.sh/v3/covid-19/gov/"
        self.example_response = '''[
  "Austria",
  "Canada",
  "Germany",
  "India",
  "Indonesia",  
  "Israel",  
  "Italy",  
  "Mexico",  
  "New Zealand",  
  "Nigeria",  
  "S. Korea",  
  "South Africa",  
  "Switzerland",  
  "UK",  
  "Vietnam"
]'''


class VaccineData:
    def __init__(self):
        self.request_url = "https://disease.sh/v3/covid-19/vaccine"
        self.example_response = '''{
  "source":"https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-vaccine-tracker",
  "totalCandidates":"51",
  "phases":[
    {
      "phase":"Phase 3",
      "candidates":"7"
    },
    {
      "phase":"Phase 2/3",
      "candidates":"2"
    },
    {
      "phase":"Phase 2",
      "candidates":"3"
    },
    {
      "phase":"Phase 1/2",
      "candidates":"10"
    },
    {
      "phase":"Phase 1",
      "candidates":"14"
    },
    {
      "phase":"Pre-clinical",
      "candidates":"14"
    },
    {
      "phase":"Early research",
      "candidates":"1"
    }
  ],
  "data":[
    {
      "candidate":"Ad5-nCoV",
      "mechanism":"Recombinant vaccine (adenovirus type 5 vector)",
      "sponsors":
        [
          "CanSino Biologics"
        ],
      "details":"Background: China&rsquo;s CanSino Biologics has developed a recombinant novel coronavirus vaccine that incorporates the adenovirus type 5 vector (Ad5). Preliminary safety data from a Phase 1 (ChiCTR2000030906; NCT04313127) clinical trial of 108 participants between 18 and 60 years old who will receive low, medium, and high doses of Ad5-nCoV has allowed the company to plan to initiate a Phase 2 trial, according to an announcement. The Phase 2 (ChiCTR2000031781) trial has identical inclusion criteria. Outcomes: A single dose of Ad5-nCoV protected against upper respiratory infection of SARS-CoV-2 in ferrets, according to a paper published 14 August in Nature Communications. Results from the Phase 1 trial show a humoral and immunogenic response to the vaccine, according to a paper published in The Lancet. Adverse reactions such as pain (54%), fever (46%), fatigue (44%), headache (39%), and muscle pain (17%) occurred in 83% of patients in the low and medium dose groups and 75% of patients in the high dose group. In the Phase 2 trial, neutralizing antibodies and specific interferon γ enzyme-linked immunospot assay responses were observed at all dose levels for most participants. Status: On 25 June, China’s Central Military Commission announced the military had been approved to use Ad5-nCoV for a period of 1 year, according to reporting in Reuters. The Phase 3 trial is underway at sites in Saudi Arabia and Russia.",
      "trialPhase":"Phase 3",
      "institutions":
        [
          "Tongji Hospital",
          "Wuhan, China"
        ]
    },
    {
      "candidate":"AZD1222",
      "mechanism":"Replication-deficient viral vector vaccine (adenovirus from chimpanzees)",
      "sponsors":
        [
          "The University of Oxford",
          "AstraZeneca",
          "IQVIA",
          "Serum Institute of India"
        ],
      "details":"Background: AstraZeneca and the Oxford Vaccine Group at the University of Oxford are developing AZD1222 (previously ChAdOx1), a chimpanzee adenovirus vaccine. The team has previously developed a MERS vaccine. In India, the candidate is being jointly developed by the Serum Institute of India and AstraZeneca, and goes by the name Covishield. Preclinical data on the pre-print server bioRxiv showed a significantly reduced viral load and &ldquo;humoral and cellular immune response.&rdquo; Another pre-print paper showed an immune response in mice and pigs. Study Designs: A Phase 1/2 (NCT04324606) single-blinded, multi-center study of 1,090 healthy adult volunteers aged 18-55 years with four treatment arms. A Phase 3 trial (NCT04516746), for which AstraZeneca released the clinical study protocol, is underway and aims to enroll up to 30,000 participants. An inhaled version of the vaccine candidate is being tested in a small trial of 30 people.  Outcomes: Preliminary results from the trial published in The Lancet showed the vaccine candidate had an &ldquo;acceptable safety profile&rdquo; with most patients demonstrating an antibody response after one dose and all patients showing a response after two doses. There has been one death in a Phase 3 trial in Brazil, which was confirmed by the Brazilian National Health Surveillance Agency (Anvisa). Status: The AstraZeneca trials are funded in part by BARDA and Operation Warp Speed. IQVIA&nbsp;announced&nbsp;they are partnering with AstraZeneca to advance clinical trials for the vaccine. Phase 3 trials are being conducted in the&nbsp;United States&nbsp;and in&nbsp;study sites&nbsp;in India, but were put on hold following a serious adverse event. While trials have resumed in most countries, the FDA has not allowed them to resume in the US. Further, the agency has broadened its&nbsp;safety inquiry into AZD1222 to include data from similar vaccines, Reuters reported on 30 September. EMA&rsquo;s human medicines committee (CHMP) has&nbsp;started&nbsp;a rolling review of AZD1222 to reduce the amount of time before a decision is made on safety and effectiveness, as has Health Canada In Australia, the Australian Therapeutic Good Administration (TGA) granted AZD1222 provisional determination, the first step in the process for approval for the vaccine.",
      "trialPhase":"Phase 3",
      "institutions":
        [
          "The University of Oxford,&nbsp",
          "the Jenner Institute"
        ]
    },
    {
      "candidate":"CoronaVac",
      "mechanism":"Inactivated vaccine (formalin with alum adjuvant)",
      "sponsors":
        [
          "Sinovac"
        ],
      "details":"Background: CoronaVac (formerly PiCoVacc) is a formalin-inactivated and alum-adjuvanted candidate vaccine. Results from animal studies showed &ldquo;partial or complete protection in macaques&rdquo; exposed to SARS-CoV-2, according to a&nbsp;paper&nbsp;published by researchers in the journal&nbsp;Science.  Study Design: A Phase 1/2 trial enrolled 743 healthy volunteers (18-59 years old) who received two different dosages of the vaccine or placebo. There were 143 participants in Phase 1 (NCT04352608) and 600 participants in Phase 2 (NCT04383574). Sinovac said a Phase 3 trial in collaboration with Instituto Butantan in Brazil is underway (NCT04456595), and the company plans to enroll around 9,000 patients in the healthcare industry. Trials are also underway in Turkey (NCT04582344) and in Indonesia (NCT04508075).  Outcomes: Results from the Phase 1/2 trials posted to the pre-print server medRxiv indicate the vaccine has good safety and immunogenicity, with 92.4% of participants receiving the 3 μg dose on a 0-14 day schedule and 97.4% of individuals receiving the dose on a 0-28 day schedule achieving seroconversion.  Status:  Representatives from Sinovac told Reuters that the vaccine appeared to be safe in older trial participants, and did not cause any severe side effects. Preliminary results from the Instituto Butantan trial announced by the company indicate CoronaVac is safe so far, with no serious adverse events reported.",
      "trialPhase":"Phase 3",
      "institutions":
        [
          "Sinovac Research and Development Co., Ltd."
        ]
    },
    {
      "candidate":"JNJ-78436735 (formerly Ad26.COV2-S)",
      "mechanism":"Non-replicating viral vector",
      "sponsors":
        [
          "Johnson & Johnson"
        ],
      "details":"Background: Johnson & Johnson is developing a COVID-19 vaccine, JNJ-78436735 (formerly known asd Ad26.COV2-S), using their AdVac and PER.C6 systems, which were also used to develop the company's Ebola vaccine. The work is being done in J&J's Janssen Pharmaceuticals division. In partnership with BARDA, J&J has committed to investing more than $1 billion in vaccine research and development. JNJ-78436735 is a part of Operation Warp Speed.  Study Design: A randomized, double-blind, placebo-controlled, Phase 1/2a study of recombinant JNJ-78436735 in 1,045 healthy participants 18-55 years of age, and adults 65 years or older. Study sites are planned in the U.S. and Belgium (NCT04436276). The Phase 3 ENSEMBLE trial will enroll up to 60,000 participants in the United States and internationally (NCT04505722). On 23 September, J&J released the study protocol for the ENSEMBLE trial. Outcomes: Results from the Phase 1/2a study in humans posted to the pre-print server MedRxiv found a single dose of the vaccine showed immunogenicity and a good safety profile. In animal studies, researchers reported in a paper published in Nature that a single injection of JNJ-78436735 "induced robust neutralizing antibody responses and provided complete or near-complete protection in bronchoalveolar lavage and nasal swabs following SARS-CoV-2 challenge," in rhesus macaques, while another paper published in Nature Medicine indicated the vaccine protected against severe disease when tested in hamsters. Status: On 10 June, J&J announced it is accelerating Phase 1/2 trials and human trials are underway. The Phase 3 trial, expected to enroll up to 60,000 people, is also underway, according to the company. The ENSEMBLE trial is currently on hold pending a review of an adverse event a participant developed in one of the study arms.  Funding: JNJ-78436735 is  funded by Janssen, BARDA, NIAID and Operation Warp Speed. ",
      "trialPhase":"Phase 3",
      "institutions":
        [
          "Johnson & Johnson"
        ]
    },
    {"candidate":"mRNA-1273","mechanism":"mRNA-based vaccine","sponsors":["Moderna"],"details":"Background: mRNA-1273 was developed by Moderna based on prior studies of related coronaviruses such as those that cause severe acute respiratory syndrome (SARS) and Middle East respiratory syndrome (MERS). A Phase 1 trial (NCT04283461) of 105 healthy participants provided the basis for Moderna&rsquo;s investigational new drug application (IND), which was successfully reviewed by the FDA and set the stage for Phase 2 testing. A Phase 2 trial of 600 healthy participants evaluating 25 µg, 100 µg, and 250 µg dose levels of the vaccine was completed, and mRNA-1273 has advanced to a Phase 3 trial (NCT04405076). Study Design: A Phase 3 trial of 30,000 participants at high risk for SARS-CoV-2 infection who will receive a 100 µg dose of mRNA-1273 or placebo and then followed for up to 2 years (COVE trial; NCT04470427). Moderna  posted the full trial protocol for COVE on 17 September.  Outcomes: Animal studies - Results from a challenge in a mouse model showed mRNA-1273 prevented viral replication in the lungs, and neutralizing titers in the mouse model were similar in participants receiving 25 µg or 100 µg doses of the vaccine. A study of nonhuman primates challenged with SARS-CoV-2 published in the New England Journal of Medicine had neutralizing activity, and limited inflammation and lung activity after being administered the vaccine. A paper published in Nature also showed mRNA-1273 induced neutralizing antibodies in mice. Human studies - Phase 1 data published in the New England Journal of Medicine showed mRNA-1273 successfully produced neutralizing antibody titers in 8 participants who received either 25 µg or 100 µg doses. The response was dose dependent in 45 participants across 25 µg, 100 µg, and 250 µg dose levels. In participants with available antibody data, neutralizing antibody titers were on par with what has been in seen in convalescent sera from people who have successfully fought off COVID-19. The vaccine also appears to be safe for older adults, with participants who received two 25 μg or 100 μg doses of the vaccine experiencing mild or moderate effects consisting of fatigue, chills, headache, myalgia, and injection site pain, according to data from the Phase 1 trial published in the New England Journal of Medicine.  Status: On 12 May, the FDA granted Fast Track designation to mRNA-1273. A Phase 3 trial of the vaccine is underway, which is being funded by Operation Warp Speed.","trialPhase":"Phase 3","institutions":["Kaiser Permanente Washington Health Research Institute"]},{"candidate":"No name announced","mechanism":"Inactivated vaccine","sponsors":["Wuhan Institute of Biological Products","China National Pharmaceutical Group (Sinopharm)"],"details":"Background: Researchers at Sinopharm and the Wuhan Institute of Virology under the Chinese Academy of Sciences are developing an inactivated COVID-19 vaccine candidate. They have initiated a randomized, double-blind, placebo parallel-controlled Phase 1/2 clinical trial (ChiCTR2000031809) of healthy individuals starting at 6 years old.  Outcomes: The vaccine has shown a "strong neutralizing antibody response" in Phase 1/2 trials, according to a release from China National Biotec Group. Results from a Phase 1 and a Phase 2 trial published in JAMA show the vaccine candidate has demonstrated immunogenicity. Status: A Phase 3 trial is underway in Peru, Morocco, and in the United Arab Emirates. Funding: This candidate is being supported by the Ministry of Science and Technology in China.","trialPhase":"Phase 3","institutions":["Henan Provincial Center for Disease Control and Prevention"]},{"candidate":"NVX-CoV2373","mechanism":"Nanoparticle vaccine","sponsors":["Novavax"],"details":"Background: Novavax announced in March that it has produced a stable, prefusion protein nanoparticle vaccine candidate for COVID-19. A Phase 1/2 trial evaluating NVX-CoV2373 began on 25 May.  Study Design: A randomized, observer-blinded, placebo-controlled trial of 130 healthy participants 18 to 59 years of age at two sites in Australia is being conducted. Patients will receive a two-dose regimen of 5 μg or 25 μg of NVX-CoV2373 with or without Novavax's Matrix‑M adjuvant (NCT04368988). A Phase 2b trial is underway in South Africa, which includes two cohorts: a group of 2,665 healthy adults and a group of 240 adults who are HIV positive (NCT04533399). Outcomes: On 4 August, Novavax announced positive Phase 1 results for NVX-CoV2373 indicating participants who had received the vaccine developed an antibody response in participants at multiple dose levels. The data were later published in the New England Journal of Medicine. NVX-CoV2373 also has a favorable safety profile, according to the company.  Status: On May 11, CEPI announced they had provided Novavax with an additional $384 million towards the development and manufacturing of NVX-CoV2373. Novavax plans to manufacture 1 billion doses of NVX-CoV2373 by 2021 as part of their recent acquision of Praha Vaccines. Novavax was awarded a $60 million US Department of Defense contract towards manufacturing NVX-CoV2373, according to a company press release, and another $1.6 billion from Operation Warp Speed if the candidate is effective in clinical trials. The candidate is officially begun a Phase 3 trial in the United Kingdom, which will evaluate the vaccine in up to 10,000 participants, the company said in a press release.","trialPhase":"Phase 3","institutions":["Novavax"]},{"candidate":"Bacillus Calmette-Guerin (BCG) vaccine","mechanism":"Live-attenuated vaccine","sponsors":["University of Melbourne and Murdoch Children&rsquo","s Research Institute","Radboud University Medical Center","Faustman Lab at Massachusetts General Hospital"],"details":"Background: The BCG vaccine is indicated to prevent tuberculosis in those who have a higher risk of the disease. It has been implicated in helping to combat other infections outside TB by boosting the immune system to fight similar infections. In 2017, the World Health Organization (WHO)&nbsp;reported&nbsp;the BCG vaccine may be effective against leprosy and other nontuberculous mycobacteria such as buruli ulcer disease. Other papers have posited the vaccine is effective in preventing acute&nbsp;respiratory tract infections&nbsp;in elderly patients, other&nbsp;respiratory infection and sepsis. A non-peer reviewed paper posted in March 2020 on the preprint server medRxiv has suggested countries with BCG vaccination programs at childhood are&nbsp;faring better&nbsp;in the fight against COVID-19 compared with countries that do not require BCG vaccination. Trials: BCG vaccines are being studied in the randomized, controlled, Phase 3 BRACE trial, which aims to recruit 4,170 healthcare workers in hospitals in Australia (NCT04327206). Researchers in The Netherlands launched the randomized, parallel-assignment, phase 3 BCG-CORONA trial on 31 March and plan to enroll 1,500 healthcare workers to receive the BCG vaccine or placebo (NCT04328441). The Faustman Lab is currently evaluating the BCG vaccine&rsquo;s effectiveness in&nbsp;type 1 diabetes&nbsp;and is seeking funding to launch trial to assess whether the vaccine helps prevent COVID-19 in healthcare workers, according to&nbsp;independent reporting&nbsp;from the&nbsp;New York Times. Outcomes: A paper published in Science Advances found countries that required BCG vaccination until the year 2000 had significantly slower growth rates of COVID-19 compared with countries that did not mandate the vaccine. However, a birth cohort study published in Clinical Infectious Diseases found the BCG tuberculosis vaccine did not have a protective effect against COVID-19 in more than 1 million individuals born in Sweden who received the vaccine. A letter published in the journal PNAS where researchers analyzed mortality rates in countries with higher rates of BCG vaccination such as Bolivia, Panama, Columbia, Peru, Brazil, Mexico, South Africa, and Germany found that the negative association between the BCG vaccination and COVID-19 related deaths appears to be diminishing. Status: Trials are still currently recruiting.","trialPhase":"Phase 2/3","institutions":["University of Melbourne and Murdoch Children&rsquo","s Research Institute","Radboud University Medical Center","Faustman Lab at Massachusetts General Hospital"]},{"candidate":"BNT162","mechanism":"mRNA-based vaccine","sponsors":["Pfizer, BioNTech"],"details":"Background: Pfizer and BioNtech are&nbsp;collaborating BNT162, a series of vaccine candidates for COVID-19. BNT162 was initially four vaccine candidates originally developed by BioNTech, two candidates consisting of nucleoside modified mRNA-based (modRNA), one of uridine containing mRNA-based (uRNA), and the fourth candidate of self-amplifying mRNA-based (saRNA). The companies have selected the modRNA candidate BNT162b2 to move forward in a Phase 2/3 trial. &nbsp; Study Designs: A Phase 1/2 trial in the US and Germany of 200 healthy participants between aged 18-55 years, with a vaccine dose range of 1 &micro;g to 100 &micro;g is currently recruiting (NCT04380701) as is a Phase 2/3 trial of about 32,000 healthy participants&nbsp;(NCT04368728) Pfizer and BioNTech are also planning a combined Phase 1/2 trial of 160 participants between 20-85 years old (NCT04588480).  &nbsp; Outcomes:&nbsp;On 20 August, Pfizer and BioNTech researchers posted non-peer-reviewed data showing similar immunogencity between BNT162b1 and BNT162b2 but fewer adverse effects with BNT162b2. Another&nbsp;study of BNT162b1&nbsp;was reported 1 July on the non-peer-reviewed preprint server medRxiv and later published in the journal Nature. Robust immunogenicity was seen after vaccination at all three doses (10 &mu;g, 30 &mu;g and 100 &mu;g). Adverse events were elevated at the highest dose; therefore, participants did not receive a second dose at that level. Participants who received two doses between 1 and 50 µg of BNT162b1 had Ȣrobust RBD-specific antibody, T-cell and favourable cytokine responses," according to a paper published in Nature on 30 September. Pre-clinical results of BNT162b2 posted to the pre-print server bioRxiv showed the vaccine had "protective anti-viral effects in rhesus macaques, with concomitant high neutralizing antibody titers and a TH1-biased cellular response in rhesus macaques and mice."   Status: Pfizer and BioNTech have received FDA Fast Track designation for BNT162b1 and BNT162b2. BNT162b2 was&nbsp;selected&nbsp;to advance to a Phase 2/3 safety study &quot;based on the totality of available data from our preclinical and clinical studies, including select immune response and tolerability parameters." The companies have asked the FDA to consider an expanded protocol for the Phase 3 trial to include up to 44,000 participants. EMA has initiated a rolling review of BNT162b2, which could accelerate approval of the candidate. Pfizer and BioNTech could be ready to file for an  EUA in November and have vaccine ready for use in December, according to the Wall Street Journal. In Australia, BNT162b2 received provisional determination from Australia’s Therapeutic Goods Administration (TGA), which is the first step on the road for approval for the vaccine in the country.","trialPhase":"Phase 2/3","institutions":["Multiple study sites in Europe and North America"]},{"candidate":"Covaxin","mechanism":"Inactivated vaccine","sponsors":["Bharat Biotech","National Institute of Virology"],"details":"Background: Bharat Biotech, an Indian biotechnology company, is partnering with the National Institute of Virology to develop an inactivated vaccine candidate for COVID-19 called Covaxin. A Phase 1/2 trial of about 1,100 healthy participants is underway after approval by the Drug Controller General of India. In addition to Covaxin, Bharat Biotech is working on two other vaccine candidates: one with the University of Wisconsin–Madison and FluGen, and the other with Thomas Jefferson University. Outcomes: Results of a two-dose regimen given to rhesus macaques posted to the pre-print server Research Square showed an increase in SARS-CoV-2 specific IgG and neutralizing antibodies and reduced viral replication in the nasal cavity, the throat, and the lung. Status: Early results in the first 50 people who received the vaccine candidate appear to be "encouraging," according to a comment from the trial's principal investigator. The Indian Council of Medical Research has reported this candidate has entered Phase 2 trials.","trialPhase":"Phase 2","institutions":[""]},{"candidate":"No name announced","mechanism":"Recombinant vaccine","sponsors":["Anhui Zhifei Longcom Biopharmaceutical, Institute of Microbiology of the Chinese Academy of Sciences"],"details":"Background: China's National Medical Products Administration has approved a Phase 1 trial of a COVID-19 vaccine candidate developed by the Anhui Zhifei Longcom Biopharmaceutical and the Institute of Microbiology of the Chinese Academy of Sciences. A Phase 2 trial is underway, with results from Phase 1 expected in September, according to Reuters.","trialPhase":"Phase 2","institutions":[""]},{"candidate":"ZyCoV-D","mechanism":"DNA vaccine (plasmid)","sponsors":["Zydus Cadila"],"details":"Background: India’s Zydus Cadila is researching ZyCoV-D, a plasmid DNA vaccine candidates for COVID-19 that targets the viral entry membrane protein of the virus. The company has launched an adaptive Phase 1/2 dose escalation trial and plans to enroll about 1,000 healthy volunteers. On 5 August, Zydus announced that Phase 1 was complete and the candidate was entering Phase 2 trials.","trialPhase":"Phase 2","institutions":["Zydus Cadila"]},{"candidate":"AG0301-COVID19","mechanism":"DNA vaccine","sponsors":["AnGes, Inc."],"details":"Background: Biopharmaceutical company AnGes, based in Japan, is developing a DNA vaccine candidate for COVID-19 called AG0301-COVID19. A Phase 1/2 trial of 30 participants evaluating the candidate is underway at Osaka City University Hospital in Japan (NCT04463472). ","trialPhase":"Phase 1/2","institutions":["AnGes, Inc.","Japan Agency for Medical Research and Development"]},{"candidate":"BBIBP-CorV","mechanism":"Inactivated vaccine","sponsors":["Beijing Institute of Biological Products","China National Pharmaceutical Group (Sinopharm)"],"details":"Background: Sinopharm is developing a second inactivated COVID-19 vaccine candidate, BBIBP-CorV, with the Beijing Institute of Biological Products. BBIBP-CorV is currently being evaluated in a Phase 2 trial (ChiCTR2000032459).  Outcomes: Results from a paper published in the journal Cell appear to show BBIBP-CorV provides "highly efficient protection" against SARS-CoV-2 in rhesus macaques who underwent challenge against the virus. Phase 1 results published in The Lancet Infectious Diseases show BBIBP-CorV was safe and tolerated at all dose levels, with all participants showing a humoral response to the vaccine at 42 days after administration.  Status: Both vaccine candidates could be ready for market by the end of the year, according to reporting from Reuters. Funding: This candidate is being supported by the Ministry of Science and Technology in China.","trialPhase":"Phase 1/2","institutions":["Henan Provincial Center for Disease Control and Prevention"]},{"candidate":"EpiVacCorona","mechanism":"Peptide vaccine","sponsors":["Federal Budgetary Research Institution State Research Center of Virology and Biotechnology"],"details":"Background: The Federal Budgetary Research Institution State Research Center of Virology and Biotechnology in Russia, also known as the "Vector" Institute, is developing a peptide vaccine candidate for COVID-19 called EpiVacCorona. A Phase 1/2 trial in Russia is active, but not recruiting, which is evaluating the effectiveness of the vaccine in up to 100 participants (NCT04527575). On 30 September, clinical trials of the vaccine had been completed after beginning in July, according to reporting from Reuters. Regulatory Actions: Russia has granted regulatory approval to EpiVacCorona despite the candidate not yet entering Phase 3 trials, which are expected to begin in November or December.","trialPhase":"Phase 1/2","institutions":["Federal Budgetary Research Institution State Research Center of Virology and Biotechnology"]},{"candidate":"GX-19","mechanism":"DNA vaccine","sponsors":["Genexine"],"details":"Background: Genexine, a biotechnology based in South Korea, is testing GX-19, a DNA vaccine candidate for COVID-19. The company has been approved for a Phase 1/2a clinical trial of 190 healthy participants randomized to receive the vaccine or placebo (NCT04445389). The company aims to complete Phase 1 in 3 months before moving to a multinational Phase 2 trial.","trialPhase":"Phase 1/2","institutions":[""]},{"candidate":"INO-4800","mechanism":"DNA vaccine (plasmid)","sponsors":["Inovio  Pharmaceuticals"],"details":"Background: Inovio is developing a&nbsp;DNA vaccine&nbsp;for SARS-CoV-2 that is in line with other DNA vaccines the company is developing, such as for the MERS coronavirus. The vaccine is injected intradermally through a device which Inovio plans to scale production of while they wait for study results. Study Design: As of 28 April, the company had enrolled 40 healthy volunteers in a a non-randomized, open label Phase 1 (NCT04336410) trial, according to a&nbsp;press release. Participants were to receive one or two intradermal injections (1.0 mg) of INO-4800 at baseline and at 4 weeks, followed by electroporation. Preclinical data were published in Nature Communications and showed that mice and guinea pigs who received INO-4800 demonstrated neutralizing antibodies as well as humoral and T cell responses. In guinea pigs, researchers observed protein binding antibody titers and blocking of angiotensin-converting enzyme 2 (ACE2)/SARS-CoV-2 S proteins. Outcomes: On 30 July, Inovio reported positive results from a trial where rhesus macaques received INO-4800 and were challenged with SARS-CoV-2. After 4 months, durable antibody and T cell responses were observed in the animals as well as memory T and B cell responses. Status: On 16 April, Inovio, the Center for Epidemic Preparedness Innovations (CEPI) and the International Vaccine Institute (IVI)&nbsp;announced&nbsp;they are working with the&nbsp;Korea National Institute of Health (KNIH) to conduct a Phase 1/2 clinical trial of INO-4800 in South Korea. In a press release, Inovio said early results from the vaccine showed immune responses in nearly all Phase 1 trial participants, noting that INO-4800 also inhibited replication of SARS-CoV-2 in mice. Plans for a Phase 2/3 trial were put on hold on 28 September by FDA questions about vaccine's delivery device. Inovio expects  to answer FDA by October, the company said.","trialPhase":"Phase 1/2","institutions":["Center for Pharmaceutical Research, Kansas City. Mo.","University of Pennsylvania, Philadelphia"]},{"candidate":"LNP-nCoVsaRNA","mechanism":"Self-amplifying RNA vaccine","sponsors":["Imperial College London"],"details":"Background: Imperial College London researchers are developing a self-amplifying RNA vaccine for COVID-19. They developed a vaccine candidate within 14 days of receiving the sequence from China. Animal testing is underway. The investigators have received two rounds of funding from the United Kingdom&rsquo;s government &ndash; one on 22 April and another on 17 May. Study Design: The Phase 1/2 COVAC1 trial will enroll approximately 300 healthy participants between 18 and 75 years old, with an efficacy trial for 6,000 participants planned for October. An inhaled version of the vaccine candidate is also being tested in a small trial of 30 people. Status: On 7 June, Imperial College London announced it had partnered with Morningside Ventures to establish VacEquity Global Health, an initiative that would help keep costs down for their COVID-19 vaccines down for citizens in the UK and internationally. Funding: This candidate is being supported by the UK Secretary of State for Health and the UK Secretary of State for Business, Energy and Industrial Strategy.","trialPhase":"Phase 1/2","institutions":["Imperial College London"]},{"candidate":"LUNAR-COV19 (ARCT-021)","mechanism":"Self-replicating RNA vaccine","sponsors":["Arcturus Therapeutics&nbsp","and&nbsp","Duke-NUS Medical School"],"details":"Background: Arcturus and Duke-NUS Singapore are partnering to develop a COVID-19 vaccine candidate that uses Arcturus&rsquo; self-replicating RNA and nanoparticle non-viral delivery system. Pre-clinical data from the company indicates LUNAR-COV19 provides an adaptive cellular (CD8+ cells) and balanced (Th1/Th2) immune response. Trial: A Phase 1/2 study of up to 92 healthy participants in Singapore is underway, where researchers will evaluate sequential escalating doses of the vaccine, followed by two different dose levels in the second phase of the study (NCT04480957). Outcomes: Results from a study in mice posted to the pre-print sever bioRxiv show the candidate protects against mortality and infection when challenged with SARS-CoV-2.","trialPhase":"Phase 1/2","institutions":["Duke-NUS Medical School, Singapore"]},{"candidate":"No name announced","mechanism":"Protein subunit vaccine","sponsors":["Sanofi","GlaxoSmithKline"],"details":"Background: Sanofi Pasteur and GSK announced in April that they were collaborating on a COVID-19 vaccine candidate using Sanofi's recombinant protein-based technology. According to a press release from GSK, the candidate has performed well in pre-clinical studies, demonstrating an acceptable safety profile and neutralizing antibodies. Trial: A Phase 1/2 trial is underway in up to 440 participants across multiple study sites in the United States (NCT04537208). Funding: This candidate is being supported by Operation Warp Speed and the U.S. Department of Defense.","trialPhase":"Phase 1/2","institutions":["Various"]},{"candidate":"No name announced","mechanism":"Inactivated vaccine","sponsors":["Chinese Academy of Medical Sciences, Institute of Medical Biology"],"details":"Background: Institute of Medical Biology under the Chinese Academy of Medical Sciences is developing an inactivated vaccine candidate for COVID-19. Phase 1/2 trials in up to 942 participants between the ages of 18 and 59 (NCT04412538) and in up to 471 participants at least 60 years old (NCT04470609) are underway. Outcomes: Results from 191 adults aged 18-59 years in one of the Phase 1/2 trials posted to the pre-print server medRxiv indicate the vaccine generates an immune response and is safe across low, medium and high doses. ","trialPhase":"Phase 1/2","institutions":["West China Second University Hospital, Yunnan Center for Disease Control and Prevention"]},{"candidate":"Sputnik V","mechanism":"Non-replicating viral vector","sponsors":["Gamaleya Research Institute, Acellena Contract Drug Research and Development"],"details":"Background: The Gamaleya Research Institute in Russia is testing their non-replicating viral vector COVID-19 vaccine candidate, Sputnik V (formerly Gam-COVID-Vac), in two Phase 1/2 trials. The trials recruited about 38 participants each to receive the vaccine candidate (NCT04436471) (NCT04437875). Outcomes: Results from the two small Phase 1/2 trials published in The Lancet appear to show the vaccine has a good safety profile and "induced strong humoral and cellular immune response" in participants. Status: The institute plans to test the vaccine candidate on up to 40,000 people at 45 different medical centers across Russia, which would be the equivalent of a Phase 3 trial, and in a smaller trial of 110 participants older than 60 years alongside the Phase 3 trial. The vaccine is also being tested outside Russia in the United Arab Emirates and in Belarus. Regulatory Actions: The Health Ministry of the Russian Federation has approved Sputnik V as the first vaccine for COVID-19. However, no trial data has been published to date and a Phase 3 trial of the candidate has not been initiated. The approval has drawn criticism in the medical community due to lack of data on safety and efficacy. Funding: This candidate is being supported by the Health Ministry of the Russian Federation.","trialPhase":"Phase 1/2","institutions":["Various"]},{"candidate":"AdimrSC-2f","mechanism":"Protein subunit vaccine","sponsors":["Adimmune"],"details":"Background: Taiwanese company Adimmune is developing a COVID-19 vaccine candidate, AdimrSC-2f, that targets the SARS-CoV-2 spike protein. The candidate has seen positive results in animal testing, and the company is currently planning a randomized, Phase 1 study to evaluate the candidate in 70 healthy participants (NCT04522089) after receiving conditional approval in Taiwan.","trialPhase":"Phase 1","institutions":["Adimmune"]},{"candidate":"COVAX-19","mechanism":"Monovalent recombinant protein vaccine","sponsors":["Vaxine Pty Ltd."],"details":"Background: Vaxine Pty Ltd. has developed a monovalent recombinant protein vaccine. &nbsp; Study Design: A Phase 1 (NCT04453852) randomized, placebo controlled trial of 40 healthy adults aged 18-65 years who will receive either Covax-19 (25 μg of spike antigen plus 15 mg of Advax-2 adjuvant) or saline to assess generation of neutralizing antibodies to the spike proteins of SARS-CoV-2, as well as induction of T-cells against the spike proteins. Participants will receive two dose given three weeks apart."  Funding: This candidate is being supported by NIAID.","trialPhase":"Phase 1","institutions":["Royal Adelaide Hospital"]},{"candidate":"CVnCoV","mechanism":"mRNA-based vaccine","sponsors":["CureVac"],"details":"Background: CureVac is developing an mRNA-based vaccine, named CVnCoV, to produce an immune response against COVID-19. The vaccine works by using non-chemically modified nucleotides within mRNA to "provide a strong and balanced activation of the immune system". Pre-clinical results have shown virus neutralizing titers and T-cell response to the candidate, according to a 14 May company release.  Trial: CureVac is evaluating CVnCoV in a Phase 1 trial of 168 healthy subjects  in Germany and Belgium (NCT04449276). A Phase 2 dose-confirmation trial with up to 691 participants is planned, but not yet recruiting (NCT04515147). A mid-stage Phase 2a study in Peru and Panama is also underway. Status: In a prospectus document filed with the SEC, CureVac said a Phase 3 trial with up to 20,000 participants is planned.  Funding: This candidate is being supported by the German federal government. ","trialPhase":"Phase 1","institutions":["CureVac"]},{"candidate":"DelNS1-2019-nCoV-RBD-OPT1","mechanism":"Replicating viral vector","sponsors":["Xiamen University, Beijing Wantai Biological Pharmacy"],"details":"Background: A replicating viral vector nasal spray, developed by the University of Hong Kong and Beijing Wantai Biopharmaceutical in China, is being evaluated in a Phase 1 trial as a COVID-19 vaccine candidate. The trial, which began in Jiangsu province on September 1, will examine the immunogenicity and safety of the vaccine in up to 48 participants (ChiCTR2000037782).","trialPhase":"Phase 1","institutions":["Jiangsu Provincial Centre For Disease Control and Prevention"]},{"candidate":"GRAd-COV2","mechanism":"Adenovirus-based vaccine","sponsors":["ReiThera","Leukocare","Univercells"],"details":"Background: Biotechnology companies ReiThera (Italy), Leukocare (Germany) and Univer cells (Belgium) are partnering to develop an adenovirus-based COVID-19 vaccine. A Phase 1 trial is currently underway in Italy.","trialPhase":"Phase 1","institutions":["Lazzaro Spallanzani National Institute for Infectious Diseases"]},{"candidate":"No name announced","mechanism":"Plant-based adjuvant vaccine","sponsors":["Medicago","GSK","Dynavax"],"details":"Background: Medicago, which recently developed a seasonal recombinant quadrivalent virus-like particle (VLP) influenza vaccine, reported they created a coronavirus VLP 20 days after working with the SARS-CoV-2s genome. Medicago is also testing the candidate with two additional vaccine adjuvants from GSK and Dynavax. Status: A single dose of Medicago&rsquo;s plant-based vaccine candidate in mice yielded a positive antibody response after 10 days, according to a company release. A Phase 1 trial of 180 healthy participants is underway, and Medicago expects to begin a Phase 2 trial in October of 2020.","trialPhase":"Phase 1","institutions":["Medicago"]},{"candidate":"No name announced","mechanism":"Protein subunit vaccine","sponsors":["CSL","The University of Queensland"],"details":"Background: Researchers at the University of Queensland have developed a molecular clamp vaccine candidate for COVID-19. The vaccine helps the body to better recognize the protein on the virus surface by locking the unstable, prefusion version of the surface proteins in a way the immune system recognizes. The candidate has generated a neutralizing immune response, according to a press release from the university. Status: A Phase 1 trial is underway evaluating 120 healthy volunteers aged 18-55 years old. The university has announced it is partnering with CSL and CEPI to develop and manufacture the vaccine pending results from a Phase 1 trial. If clinical trials are successful, the vaccine may be available by the end of 2021, according to a joint press release.  Funding: This candidate is being supported by CEPI. ","trialPhase":"Phase 1","institutions":[""]},{"candidate":"SCB-2019","mechanism":"Protein subunit vaccine","sponsors":["GlaxoSmithKline,&nbsp","Sanofi,&nbsp","Clover Biopharmaceuticals, Dynavax&nbsp","and Xiamen Innovax"],"details":"Background: Chinese company Clover Biopharmaceuticals is collaborating with GSK, Dynavax, Xiamen Innovax Biotech and Sanofi to develop SCB-2019, a COVID-19 vaccine candidate that uses Clover's S-Trimer platform, GSK's AS03 adjuvant, and Dynavax's CpG 1018 adjuvant. Positive pre-clinical data indicate the candidate has a strong neutralizing response in animals, according to a press release from Clover. Study Design: A Phase 1 trial of 150 healthy volunteers who will receive the SCB-2019 vaccine candidate alone, with the AS03 adjuvant, or with the CpG 1018 adjuvant with potassium aluminum sulfate (Alum) (NCT04405908). Status: The first participants in the trial have been dosed as of 19 June, and results are expected in August, according to a press release. CEPI has said they will provide an additional $66 million in funding pre-clinical and Phase 1 trials of a vaccine candidate.  Funding: This candidate is being supported by CEPI.","trialPhase":"Phase 1","institutions":["Linear Clinical Research (Australia)"]},{"candidate":"UB-612","mechanism":"Multitope peptide-based vaccine","sponsors":["COVAXX"],"details":"Background: COVAXX, a subsidiary of United Biomedical Inc (UBI), is developing a multitope vaccine candidate for COVID-19. The company designed the candidate to activate both T-cell and B-cell immunity in the body and has demonstrated neutralizing antibody activity in mice, rats, and guinea pigs. A Phase 1 trial of the vaccine is underway in Taiwan in up to 60 participants (NCT04545749). COVAXX is also partnering with medical company Dasa for a Phase 2/3 trial in Brazil, and with the University of Nebraska Medical Center for Phase 1/2 trials in the United States.","trialPhase":"Phase 1","institutions":["United Biomedical Inc. (UBI)"]},{"candidate":"V590","mechanism":"Recombinant vaccine (vesicular stomatitis virus)","sponsors":["Merck","IAVI"],"details":"Background: Merck and nonprofit scientific research organization IAVI are collaborating to develop a COVID-19 vaccine candidate based on Merck's recombinant vesicular stomatitis virus (rVSV) technology used in the company's Ebola vaccine. A Phase 1 trial of 90 participants across two centers is currently recruiting (NCT04497298).  Funding: This candidate is being supported by BARDA. ","trialPhase":"Phase 1","institutions":[""]},{"candidate":"V591","mechanism":"Measles vector vaccine","sponsors":["University of Pittsburgh’s Center for Vaccine Research"],"details":"Background: The Center for Vaccine Research at the University of Pittsburgh School of Medicine is developing a measles vector vaccine together with Themis Biosciences and Institute Pasteur. On 26 May, Merck announced they had acquired Themis and will help develop and scale up the vaccine candidate. Trial: A Phase 1 trial is underway to evaluate the candidate against the placebo in up to 90 participants in Belgium and France (NCT04497298). Outcomes: According to a paper&nbsp;published in EBioMedicine, the vaccine creates antibodies in mice that the researchers believe is sufficient to neutralize the virus.","trialPhase":"Phase 1","institutions":["University of Pittsburgh","Themis Biosciences","Institut Pasteur"]},{"candidate":"VXA-CoV2-1","mechanism":"Recombinant vaccine (adenovirus type 5 vector)","sponsors":["Vaxart"],"details":"Background: Vaxart is working with Emergent Biosolutions and KindredBio to develop and manufacture their oral recombinant vaccine candidate, named VXA-CoV2-1. The company has received &ldquo;positive pre-clinical results&rdquo; for its oral vaccine candidate and selected the oral vaccine candidate over several others moving forward for testing and manufacturing. Study Design: VXA-CoV2-1 is being evaluated in a Phase 1 trial of up to 48 healthy participants (NCT04563702). Outcomes: Animal testing of the oral vaccine yielded SARS-CoV-2 antibodies after first and second doses, according to a statement. Status: Vaxart's candidate was selected to participate in a non-human primate challenge funded by Operation Ward Speed. The company is currently being investigated by US federal prosecutors and the US Securities and Exchange Commission for potentially overstating the company's involvement with Operation Warp Speed. The Phase 1 trial is underway and participants are receiving their first doses, the company announced in a press release on 13 October.","trialPhase":"Phase 1","institutions":["Vaxart"]},{"candidate":"AAVCOVID","mechanism":"Gene-based vaccine","sponsors":["Massachusetts Eye and Ear","Massachusetts General Hospital","University of Pennsylvania"],"details":"Background: Voltron Therapeutics and Hoth Therapeutics are working with the Vaccine and Immunotherapy Center (VIC) of Massachusetts General Hospital to develop a COVID-19 vaccine candidate using the VIC's Self-Assembling Vaccine (SAV) platform. Two sets of vaccine candidates are currently in pre-clinical animal testing. Funding: This candidate is being supported by entrepreneurs Wyc Grousbeck and Emilia Fazzalari.","trialPhase":"Pre-clinical","institutions":[""]},{"candidate":"AdCOVID","mechanism":"Intranasal vaccine","sponsors":["Altimmune"],"details":"Background: Altimmune has developed a COVID-19 vaccine candidate using the same technology they used build their influenza vaccine, NasoVAX. The vaccine is delivered intranasally in a single dose to activate humoral, cellular and mucosal immunity. Pre-clinical results announced by the company show "serum neutralizing activity and potent mucosal immunity" and a strong antibody response in mice; further pre-clinical results showed a strong T-cell response in mice. Clinical testing is expected to begin in the fourth quarter of 2020. ","trialPhase":"Pre-clinical","institutions":["University of Alabama at Birmingham"]},{"candidate":"bacTRL-Spike","mechanism":"Monovalent oral vaccine (bifidobacteria)","sponsors":["Symvivo"],"details":"Background: bacTRL-Spike is a bifidobacteria monovalent SARS-CoV-2 DNA oral vaccine candidate. Symvivo also separately is developing two other vaccine candidates: a trivalent vaccine that uses the spike protein, nucleocapsid protein, and matrix glycoprotein; and an immunoprophylaxis agent that uses prophylactic nanobody therapy. bacTRL-Spike is currently being evaluated in a phase 1 trial (NCT04334980) of 84 healthy participants at varying doses tested against a placebo group. Status: Phase 1 of the trial is underway, according to a press released by Symvivo on 19 October.","trialPhase":"Phase 1","institutions":["Symvivo Corporation"]},{"candidate":"ChAd-SARS-CoV-2-S","mechanism":"Adenovirus-based vaccine","sponsors":["Washington University School of Medicine in St. Louis"],"details":"Background: Researchers at the Washington University School of Medicine in St. Louis are developing a chimpanzee adenovirus vectored vaccine as a COVID-19 vaccine candidate. ChAd-SARS-CoV-2-S is an intranasal vaccine candidate that encodes the spike protein of the SARS-CoV-2 virus. Pre-clinical results in mice published in the journal Cell show ChAd-SARS-CoV-2-S is effective at inducing neutralizing antibodies, particularly in the upper and lower respiratory tracts. The researchers note they are planning a study of the candidate in nonhuman primates and in humans.","trialPhase":"Pre-clinical","institutions":["Washington University School of Medicine in St. Louis"]},{"candidate":"HaloVax","mechanism":"Self-assembling vaccine","sponsors":["Voltron Therapeutics, Inc.","Hoth Therapeutics, Inc."],"details":"Background: Voltron Therapeutics and Hoth Therapeutics are working with the Vaccine and Immunotherapy Center (VIC) of Massachusetts General Hospital to develop a COVID-19 vaccine candidate using the VIC's Self-Assembling Vaccine (SAV) platform. Results from pre-clinical testing show the vaccine has a positive response to COVID-19 peptides. Two sets of vaccine candidates are currently in pre-clinical animal testing.","trialPhase":"Pre-clinical","institutions":["MGH Vaccine and Immunotherapy Center"]},{"candidate":"HDT-301","mechanism":"RNA vaccine","sponsors":["University of Washington","National Institutes of Health Rocky Mountain Laboratories","HDT Bio Corp"],"details":"Background: Researchers from the University of Washington have developed a replicon RNA vaccine candidate named HDT-301 in collaboration with the National Institutes of Health Rocky Mountain Laboratories and HDT Bio Corp. HDT-301 had shown a "robust" antibody response in mice and primates during pre-clinical testing, and a Phase 1 trial is being planned, according to a press release from the University of Washington School of Medicine.","trialPhase":"Pre-clinical","institutions":[""]},{"candidate":"LineaDNA","mechanism":"DNA vaccine","sponsors":["Takis Biotech"],"details":"Background: A partnership between Takis Biotech and Applied DNA Sciences has resulted in five DNA vaccine candidates for COVID-19. Results from pre-clinical testing showed all five LineaDNA vaccine candidates produced "strong antibody and T-cell responses" against SARS-CoV-2, Takis said&nbsp; in a press release. Their final vaccine candidate could begin human testing by fall, according to a company press release.","trialPhase":"Pre-clinical","institutions":["Takis Biotech"]},{"candidate":"No name announced","mechanism":"Ii-Key peptide COVID-19 vaccine","sponsors":["Generex Biotechnology"],"details":"Background: Generex subsidiary NuGenerex Immuno-Oncology is spearheading a vaccine project to create an Ii-Key peptide vaccine against COVID-19. In a company press release&nbsp;dated 27 February, Generex said they wanted to produce a vaccine candidate that could be tested in humans "within 90 days."","trialPhase":"Pre-clinical","institutions":["Generex"]},{"candidate":"No name announced","mechanism":"Protein subunit vaccine","sponsors":["University of Saskatchewan Vaccine and Infectious Disease Organization-International Vaccine Centre"],"details":"Background: The University of Saskatchewan&rsquo;s Vaccine and Infectious Disease Organization-International Vaccine Centre (VIDO-InterVac) is developing a protein subunit vaccine for COVID-19 and recently received $1 million to accelerate testing. Early results show the vaccine candidate produces an immune response. Animal testing is underway, according to an interview with the center&rsquo;s director posted on the university&rsquo;s website.","trialPhase":"Pre-clinical","institutions":["University of Saskatchewan Vaccine and Infectious Disease Organization-International Vaccine Centre"]},{"candidate":"No name announced","mechanism":"Adenovirus-based vaccine","sponsors":["ImmunityBio","NantKwest"],"details":"Background: ImmunityBio is developing a COVID-19 adenovirus vaccine candidate that targets both spike and nucleocapsid DNA in SARS-CoV-2. ImmunityBio announced in a statement that their candidate has been selected to participate in Operation Warp Speed. The vaccine demonstrated CD4+ and CD8+ antigen-specific T cell responses in mice, according to results published in the pre-print server bioRxiv. Study Design: A Phase 1 trial of up to 35 healthy participants is underway (NCT04591717). ","trialPhase":"Phase 1","institutions":[""]},{"candidate":"MRT5500","mechanism":"Recombinant vaccine","sponsors":["Sanofi, Translate Bio"],"details":"Background: Sanofi is partnering with Translate Bio to develop a COVID-19 vaccine candidate under its recombinant DNA platform using work from a previous SARS vaccine and in partnership with BARDA. The companies plan to enroll patients in a Phase 1/2 trial in the fourth quarter of 2020. Results from non-human studies show the vaccine produces an immune response, according to a pre-print paper published in bioRxiv.","trialPhase":"Pre-clinical","institutions":[""]},{"candidate":"No name announced","mechanism":"mRNA-based vaccine","sponsors":["Chulalongkorn University’s Center of Excellence in Vaccine Research and Development"],"details":"Background: The Chulalongkorn University’s Center of Excellence in Vaccine Research and Development in Thailand is developing an mRNA vaccine candidate for COVID-19 similar to one in development by biotechnology company Moderna. The candidate has been successful in animal trials, generating an antibody response in monkeys and mice. Clinical trials in humans are planned for September of 2020, with 100 healthy volunteers enrolled in the first phase of the study.","trialPhase":"Pre-clinical","institutions":[""]},{"candidate":"No name announced","mechanism":"gp96-based vaccine","sponsors":["Heat Biologics"],"details":"Background: Heat Biologics announced it is pairing with the University of Miami to use the gp96 heat shock protein backbone to develop at least one COVID-19 vaccine. Pre-clinical data released by the company in July and later posted to bioRxiv demonstrated an immune response in animal models. "Specifically, our latest pre-clinical studies demonstrated immunogenicity proof-of-concept, illustrating that our vaccine can expand human-HLA-restricted T-cells against immunodominant epitopes of SARS-CoV-2 Spike protein, and validating that the selected vaccine antigen may be appropriate for human testing," the CEO of Heat Biologics said.","trialPhase":"Pre-clinical","institutions":["University of Miami Miller School of Medicine"]},{"candidate":"No name announced","mechanism":"Inactivated vaccine","sponsors":["Shenzhen Kangtai Biological Products"],"details":"Background: Shenzhen Kangtai Biological Products, based in China, is planning a clinical trial in humans of its inactivated vaccine candidate after it received regulatory approval to process with the clinical trial. The company said the vaccine had proven effective in animals, with monkeys demonstrating a resistance to being exposed to SARS-CoV-2, according to Reuters.","trialPhase":"Pre-clinical","institutions":[""]},{"candidate":"PittCoVacc","mechanism":"Recombinant protein subunit vaccine (delivered through microneedle array)","sponsors":["UPMC/University of Pittsburgh School of Medicine"],"details":"Background: Researchers at the University of Pittsburgh have received a $4.9 million grant from the Coalition for Epidemic Preparedness Innovations (CEPI) to develop a COVID-19 vaccine candidate. On 2 April, investigators announced that PittCoVacc was effective in mice, delivered through a fingertip patch.  Funding: This candidate is being supported by CEPI. ","trialPhase":"Pre-clinical","institutions":["University of Pittsburgh"]},{"candidate":"T-COVIDTM","mechanism":"Intranasal vaccine","sponsors":["Altimmune"],"details":"Background: Altimmune has developed a COVID-19 vaccine candidate using the same technology they used build their influenza vaccine, NasoVAX. The vaccine would be delivered intranasally in a single dose to activate humoral, cellular and mucosal immunity. Although it is the same technology as Altimmune's other intranasal vaccine candidate for COVID-19, AdCOVID, the company says it works through a different mechanism. Status: On 1 June, Altimmune announced the FDA has approved a Phase 1/2 trial to begin in June, according to a company press release.","trialPhase":"Pre-clinical","institutions":[""]},{"candidate":"No name announced","mechanism":"mRNA lipid nanoparticle (mRNA-LNP) vaccine","sponsors":["CanSino Biologics, Precision NanoSystems"],"details":"Background: In addition to Ad5-nCoV, CanSino is developing an mRNA-LNP vaccine candidate for COVID-19 using Precision NanoSystems&rsquo; RNA vaccine platform. The company said in a press release that it will &ldquo;rapidly advance a COVID-19 mRNA-LNP vaccine candidate towards human clinical testing,&rdquo; but did not provide a timeline for development and testing.","trialPhase":"Early research","institutions":[""]}]}'''


class Theraputics:
    def __init__(self):
        self.request_url = "https://disease.sh/v3/covid-19/therapeutics"
        self.example_request = '''{"source":"https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-therapeutics-tracker","totalCandidates":"52","phases":[{"phase":"Phase 3","candidates":"14"},{"phase":"Phase 2/4","candidates":"1"},{"phase":"Phase 2/3","candidates":"10"},{"phase":"Phase 1","candidates":"4"},{"phase":"Phase 2","candidates":"14"},{"phase":"Phase 1/2/3","candidates":"2"},{"phase":"Phase 1/2","candidates":"1"},{"phase":"No longer being studied for COVID-19","candidates":"1"},{"phase":"Phase 1b","candidates":"4"},{"phase":"Phase 2b/3","candidates":"1"}],"data":[{"medicationClass":"IL-6 receptor agonist","tradeName":["Actemra (tocilizumab)"],"details":"Background: Actemra is a indicated to treat autoimmune diseases such as rheumatoid arthritis as well as cytokine release syndrome. Research from China has shown Actemra may be an effective treatment for patients with severe cases of COVID-19.  Trials: Actemra is being evaluated in the following high-profile trials: COVACTA (NCT04320615) and EMPACTA (NCT04372186). The Hôpitaux de Paris (CORIMUNO-19) is assessing Actemra in a trial for COVID-19 associated pneumonia (NCT04331808) in a Phase 2 trial.  Outcomes: Evidence is beginning to point to Actemra having a beneficial outcome for COVID-19 patients in some, but not all, scenarios. Evidence for benefit: - Results from EMPACTA indicate Actemra reduced the need for mechanical ventilation in patients with COVID-19 associated pneumonia. In EMPACTA, patients taking Actemra were &ldquo;44% less likely to progress to mechanical ventilation or death compared to patients who received placebo plus standard of care,&rdquo; Roche said in a press release. - Preliminary results from CORIMUNO-19 showed Actemra “improves significantly clinical outcomes” of pneumonia associated with COVID-19. - The drug may also improve survival in patients with cytokine release syndrome, according to a study in CHEST. - Results from the University of Michigan published in the journal Clinical Infectious Diseases showed a 45% reduction in hazard of death for COVID-19 patients and improved status compared with patients who did not receive the drug. - In a multicenter cohort study of 4,485 adults with COVID-19 published in JAMA Internal Medicine, researchers found a lower risk of mortality in adults who received Actemra within 2 days of admission to the ICU compared with patients who did not receive Actemra as part of their care. Evidence showing mixed results: - Researchers on behalf of the Niguarda COVID-19 Working Group released a comparative analysis in the Journal of Infection that noted Actemra is potentially effective, but recommended caution when using the drug. - A randomized, double-blind, placebo-controlled trial published in the New England Journal of Medicine by researchers at Massachusetts General Hospital found Actemra was not effective in reducing need for intubation, disease progression, or death but left open the opportunity that the drug did carry some benefit due to wide confidence intervals in comparisons of efficacy. Evidence showing no benefit: - In the COVID-BioB Study, patients who received Actemra instead of standard of care had improved clinical outcomes (69% vs. 61%; P = .61) and reduced mortality (15% vs. 33%; P = .15), but neither result was statistically significant. - Results posted in medRxiv by researchers at the University of North Carolina, Chapel Hill, showed that of 11 patients with severe COVID-19 requiring ventilation, Actemra reduced C-reactive protein levels but did not result in significant improvement in temperature and oxygen requirements. - An Italian study sponsored by the Italian Medicine Agency (AIFA) was stopped after Actemra failed to perform better than standard of care in reducing respiratory symptoms, intensive care visits and mortality. - Roche also provided an update for COVACTA indicating the drug did not meet its primary or secondary endpoints of improved clinical status and reduced mortality.  Status: COVACTA has been completed; EMPACTA and CORIMUNO-19 are active, but not recruiting.","developerResearcher":["Roche"],"sponsors":["Various"],"trialPhase":"Phase 3","lastUpdate":"10/23/2020"},{"medicationClass":"H2 blocker","tradeName":["Pepcid (famotidine)"],"details":"Background: Pepcid is mainly used to treat peptic ulcer disease, GERD, and Zollinger-Ellison syndrome. Pepcid was identified by computer models as having the potential for inhibiting 3-chymotrypsin-like protease, which controls coronavirus replication.  Trials: The drug is currently being evaluated in the Phase 3 MATCH trial, where up to 1,170 participants will receive hydroxychloroquine either with and without Pepcid (NCT04370262).  Outcomes: Evidence of benefit: A large retrospective study performed by researchers from the MATCH trial found patients with COVID-19 taking Pepcid (n = 84) were significantly less likely to experience death or intubation as a composite outcome (P small observational study of 83 patients hospitalized for COVID-19 at a tertiary care center who received Pepcid had reduced mortality, lower rates of intubation, and reduced serum markers. A small case series of 10 patients with COVID-19 in a non-hospital setting found high doses of the medication (most commonly 80 mg three times per day over median 11 days) improved disease-related symptoms. However, results from a pre-print paper suggest Pepcid is not a \u0022direct-acting inhibitor\u0022 of the virus. Evidence of no benefit: In a large study published in the journal Gastroenterology of 1,127 patients with COVID-19 who received Pepcid and 6,031 patients who did not, results showed Pepcid did not reduce the risk of death. ","developerResearcher":["Yamanouchi Pharmaceutical Co.","J&J","Merck"],"sponsors":["Northwell Health"],"trialPhase":"Phase 3","lastUpdate":"10/23/2020"},{"medicationClass":"HIV protease inhibitor","tradeName":["Kaletra (lopinavir-ritonavir)"],"details":"Background: Kaletra is indicated in combination with other antiretrovirals to treat HIV-1 infection in adults and in pediatric patients 14 days and older. Kaletra has been effective against SARS, showing in vitro activity against the disease in a 2004 study. Countries hard hit by COVID-19, such as Italy, have recommended the drug combination as a treatment for the novel coronavirus.  Trials: High-profile trials of Kaletra are evaluating the drug alone and in combination with other COVID-19 therapeutic candidates:  Tongji Hospital (Recruiting; NCT04255017).  A study in South Korea pitting Kaletra against hydroxychloroquine in mild cases of COVID-19 (NCT04307693).  Kaletra alone and in combination with interferon-beta are two arms of the WHO SOLIDARITY trial, but have been discontinued due to lack of efficacy.  The UK-based RECOVERY trial is also evaluating Kaletra, but has stopped randomization to this treatment arm.  Lopinavir and ritonavir are also being evaluated together with abacavir and lamivudine as the drug QuadraMune in a trial sponsored by Therapeutic Solutions International (NCT04421391).  Outcomes: Findings are beginning to indicate that Kaletra may not result in clinical improvement from COVID-19. - Evidence for use: A study published in The Lancet found a combination of interferon beta-1b, Kaletra and ribavirin was more effective than treating with Kaletra on its own. - Evidence showing no benefit: A randomized, controlled trial published in the New England Journal of Medicine showed no therapeutic benefit for Kaletra in patients with cases of severe COVID-19. Results from the RECOVERY trial, which were published in The Lancet, researchers found no clinical benefit for hospitalized patients taking Kaletra. In SOLIDARITY, interim results posted to the pre-print server medRxiv showed Kaletra and interferon did not reduce mortality, the need for ventilation, or duration of hospital stay.\n\n Status:  Trial completion dates of the studies based in China and South Korea vary, with the earliest completion dates listed in late April. SOLIDARITY is currently recruiting. RECOVERY has stopped randomizing to its Kaletra arm after finding no clinical benefit for the drug.","developerResearcher":["AbbVie"],"sponsors":["Various"],"trialPhase":"Phase 2/4","lastUpdate":"10/23/2020"},{"medicationClass":"Antiviral","tradeName":["Veklury (remdesivir)"],"details":"Background: Veklury, an intravenous drug that inhibits viral replication, has shown in vitro and in vivo activity against SARS-CoV-2. It was originally developed as a treatment for Ebola.  Regulatory actions: As studies of Veklury have shown reduced time to clinical improvement for COVID-19 patients, countries have started allowing its use outside of trial settings. United States: Veklury has been approved by the FDA for use in adults and adolescents hospitalized for COVID-19. The approval is based on results from the ACTT-1 trial, sponsored by NIAID, and the two SIMPLE trials sponsored by Gilead. FDA had previously allowed the use of Veklury for COVID-19 under an EUA based on preliminary results of ACTT, and expanded the EUA to include all hospitalized patients with COVID-19.  FDA has warned Veklury should not be used with hydroxychloroquine or chloroquine phosphate, as it may reduce antiviral activity. International: Japan has approved Veklury for COVID-19, but Singapore’s Health Sciences Authority, Australia’s Therapeutic Goods Administration (TGA), and the EMA in Europe have conditionally approved Veklury for use in patients 12 years and older with COVID-19.  In the UK, Veklury has received a positive scientific opinion under the Medicines and Healthcare products Regulatory Agency (MHRA) Early Access to Medicines Scheme, which will allow adults and children with COVID-19 access to the medication if they meet additional criteria.  Trials: Veklury is being evaluated in the following high-profile trials: - SOLIDARITY (ISRCTN83971151) (NCT04315948)) - SIMPLE (NCT04292730; NCT04292899) - ACTT (NCT04280705), ACTT-2 (NCT04401579), and ACTT-3 (NCT04492475). - Capital Medical University (NCT04252664; NCT04257656). - A late-stage trial evaluating Veklury in pediatric patients with COVID-19. - A Phase 2 trial of 40 participants across multiple trial sites in the U.S. of Veklury with and without the oral broad-spectrum anti-viral drug merimepodib (NCT04410354). - Gilead is testing an inhaled version of Veklury in a Phase 1a trial.  Outcomes: Veklury shows promise as a therapy that improves time to clinical improvement—but not improvement in mortality—for patients with COVID-19. - ACTT-1 and ACTT-2: Results from 1,059 patients in the ACTT study showed Veklury improved time to clinical recovery from 15 days to a median of 11 days, which was reaffirmed in a final report published in the New England Journal of Medicine. In ACTT-2, where patients received baricitinib in combination with Veklury, the group that received baricitinib had a reduced time to recovery compared with patients who received Veklury alone.- Capital Medical University: Veklury did not significantly improve clinical symptoms (hazard ratio, 1.23; 95% CI, 0.87-1.75). - SIMPLE: Results from Gilead’s two trials showed greater clinical improvement in moderate and severe COVID-19 cases, but results have not been statistically significant. Further results from the SIMPLE trial evaluating severe COVID-19 cases showed an improved time to clinical improvement and 62% reduction in mortality. In patients with moderate COVID-19, results from a large international trial published in JAMA appeared to show clinical improvement in patients taking a 5-day course of Veklury compared with patients randomized to standard of care at 11 days, \u0022but the difference was of uncertain clinical importance.\u0022 - SOLIDARITY: Interim trial results from SOLIDARITY posted to the pre-print server medRxiv showed none of the study drugs, including Veklury, reduced mortality, need for ventilation, or duration of hospital stay. ","developerResearcher":["Gilead Sciences"],"sponsors":["Gilead Sciences"],"trialPhase":"Phase 2/3","lastUpdate":"10/23/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["Remicade (infliximab)"],"details":"Background: Remicade is a tumor necrosis factor inhibitor that been proposed as a potential treatment for cytokine release syndrome associated with COVID-19.  Trials: Together with the monoclonal antibody namilumab, Remicade is being tested in patients hospitalized with COVID-19 in the multi-arm CATALYST trial of therapeutics led by researchers from the Universities of Birmingham and Oxford. Researchers hope one or both therapies will help alleviate serious symptoms of the disease.\nRemicade is also a treatment arm of the ACTIV-1 IM trial led by the National Center for Advancing Translational Sciences (NCATS), which is part of the National Institutes of Health (NCT04593940).\n\n\n","developerResearcher":["Janssen"],"sponsors":["UHB","Birmingham National Institute for Health Research Biomedical Research Centre (NIHR BRC)","NCATS","BARDA"],"trialPhase":"Phase 2/3","lastUpdate":"10/23/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["AZD7442"],"details":"Background: AstraZeneca is testing AZD7442, a combination of two monoclonal antibodies, AZD8895 and AZD1061, as a prevention and treatment for COVID-19. The monoclonal antibodies were discovered by researchers at Vanderbilt University and licensed to AstraZeneca. The company has launched a Phase 1 randomized, double-blind, placebo-controlled trial evaluating in up to 48 participants in the United Kingdom (NCT04507256). Status: The company is advancing AZD7442 to two Phase 3 trials after receiving $486 million from BARDA: a safety and efficacy trial in up to 5,000 participants, and a trial of up to 1,100 participants that will evaluate post-exposure prophylaxis. ","developerResearcher":["AstraZeneca","Vanderbilt University Medical Center"],"sponsors":["AstraZeneca","BARDA"],"trialPhase":"Phase 1","lastUpdate":"10/23/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["Lenzilumab"],"details":"Background: Lenzilumab has been shown to have a protective effect against cytokine release syndrome associated with CAR-T therapy. It’s believed that lenzilumab can aid cytokine-mediated immunopathology of lung injury and ARDS.  Regulatory Actions: On 2 April, FDA authorized use of lenzilumab in COVID-19 patients under an eIND application.  Trials: A multicenter, Phase 3, randomized, double-blinded, controlled, clinical trial with lenzilumab for the prevention of ARDS in patients with pneumonia associated with COVID-19 (NCT04351152), which is taking place in the U.S. and Brazil. Lenzilumab is being evaluated in NIAID\u0027s Big Effect trial in combination with Veklury compared with Veklury plus a placebo (NCT04583956).  Outcomes: Early results from the first 12 patients who received lenzilumab at Mayo Clinic locations showed 11 of 12 (92%) had clinical improvement, with a median discharge time of 5 days. Oxygenation also was improved in patients taking lenzilumab. Further results published in Mayo Clinic Proceedings showed lenzilumab was associated with an 80% reduction in risk of mechanical ventilation and mortality. ","developerResearcher":["Humanigen","Catalent"],"sponsors":["NIAID"],"trialPhase":"Phase 3","lastUpdate":"10/16/2020"},{"medicationClass":"Anthelmintic","tradeName":["Niclocide (niclosamide)"],"details":"Background: Niclosamide, an antiparasitic drug used to manage tapeworm infections, is being investigated by several centers as a COVID-19 therapeutic. Trials: Biotech company ANA Therapeutics is evaluating niclosamide in capsule form under the name ANA001 in a clinical trial authorized by the FDA. Niclosamide is also being investigated in a randomized Phase 2 trial of 100 participants with mild-to-moderate COVID-19 at Tufts Medical Center (NCT04399356), a Phase 2 trial of 100 participants with moderate COVID-19 sponsored by First Wave Bio, Inc. (NCT04436458), and at Lille University Hospital in France in combination with diltiazem against hydroxychloroquine and standard of care (NCT04372082) The drug is also being tested in a Phase 1 trial in the Philippines, South Korea, and India by Daewoong Pharmaceutical.","developerResearcher":["ANA Therapeutics"],"sponsors":["Tufts Medical Center","First Wave Bio, Inc.","Lille University Hospital"],"trialPhase":"Phase 2/3","lastUpdate":"10/16/2020"},{"medicationClass":"Synthetic human vasoactive intestinal peptide (VIP)","tradeName":["RLF-100 (aviptadil)"],"details":"Background: RLF-100 is thought by researchers to help decrease mortality and improve oxygenation in the blood for patients with COVID-19 through its anti-inflammatory activity. It currently has an Orphan Drug designation from the FDA and EMA for acute lung injury.  Trials: NeuroRx is planning several clinical trials for RLF-100: the 144-person AVINALI  study evaluating the candidate’s effectiveness in treating non-acute lung injury (NCT04360096), and the COVID-AIV trial evaluating patients with critical COVID-19 who have respiratory failure (NCT04311697). FDA has also granted Expanded Access Protocol for patients ineligible for enrollment in COVID-AIV (NCT04453839).  Regulatory Actions: NeuroRx has fast-track approval from the FDA to evaluate RLF-100 in COVID-19 patients. Outcomes: Early results from the first 30 patients enrolled in the COVID-AIV trial show no significant drug-related adverse events among patients taking RLF-100 compared with placebo. Topline results from an open-label, prospective study show survival of 81% for patients hospitalized for COVID-19 who received RLF-100 compared with the placebo group.","developerResearcher":["NeuroRx","Relief Therapeutics"],"sponsors":["NeuroRx"],"trialPhase":"Phase 2/3","lastUpdate":"10/16/2020"},{"medicationClass":"Tyrosine kinase inhibitor","tradeName":["STI-5656 (abivertinib)"],"details":"Background: Sorrento Therapeutics is testing a tyrosine kinase inhibitor STI-5656 (abivertinib maleate) in patients hospitalized with COVID-19 related pneumonia. The company recently licensed abivertinib from ACEA Therapeutics for use as a therapy for COVID-19. The FDA has approved a Phase 2 trial of 80 participants receiving STI-5656 or standard of care (NCT04440007), and a Phase 2 trial of up to 400 participants is planned in Brazil (NCT04528667).","developerResearcher":["Sorrento Therapeutics"],"sponsors":["Sorrento Therapeutics"],"trialPhase":"Phase 2","lastUpdate":"10/16/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["CT-P59"],"details":"Background: Celltrion, based in South Korea, is evaluating the human monoclonal antibody CT-P59 as a potential treatment for COVID-19. The candidate was selected through a screening process where CT-P59 was found to neutralize the SARS-CoV-2 and several variants such as the mutated G-variant strain (D614G). Trials: A Phase 1 trial of up to 32 participants is underway (NCT04525079). The Korean Ministry of Food and Drug Safety (MFDS) approved a phase 2/3 trial in up to 1,000 patients in 12 countries in September, and a Phase 3 trial in up 1,000 participants evaluating the post-exposure prophylaxis of the candidate has been approved by MDFS. Outcomes: Interim data from the Phase 1 trial indicate that CT-P59 is safe and tolerable without any adverse events.","developerResearcher":["Celltrion"],"sponsors":["Celltrion"],"trialPhase":"Phase 1","lastUpdate":"10/16/2020"},{"medicationClass":"Anticoagulant","tradeName":["Heparin (UF and LMW)"],"details":"Background: Researchers from NIH have launched NIH ACTIV-4 Inpatient trial, which will evaluate if heparin has an effect on reducing clotting events that develop as a result of COVID-19. In the Phase 3 ACTIV-4 Inpatient trial, participants will receive various doses of unfractionated or low-molecular-weight heparin. Outcomes: In a paper published in the journal Circulation, researchers cautioned against using therapeutic doses of anticoagulation in patients with severe COVID-19, as it may result in heparin-induced thrombocytopenia. ","developerResearcher":["NHLBI"],"sponsors":["Operation Warp Speed"],"trialPhase":"Phase 3","lastUpdate":"10/9/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["VIR-7831 (GSK4182136)"],"details":"Background: Vir Biotechnology, Inc. and GlaxoSmithKline are evaluating their monoclonal antibody VIR-7831 (GSK4182136) as a COVID-19 therapeutic candidate. The monoclonal antibody has shown the ability to neutralized SARS-CoV-2 in vitro, according to the companies.\n\nThe Phase 2/3 COMET-ICE trial will enroll up to 1,360 participants who will receive VIR-7831 or placebo and followed for up to 24 weeks (NCT04545060).\n\nStatus: After an independent data monitoring committee reviewed positive, unblinded safety data of VIR-7831, the companies announced a global expansion of the COMET-ICE trial on 6 October, with additional study sites planned in North America, South America and Europe.\n","developerResearcher":["Vir Biotechnology, Inc.","GSK"],"sponsors":["Vir Biotechnology, Inc."],"trialPhase":"Phase 2/3","lastUpdate":"10/9/2020"},{"medicationClass":"Antibody cocktail","tradeName":["REGN-COV2"],"details":"Background: REGN-COV2 is a novel antibody cocktail combining two of Regeneron’s antibodies, REGN10933 and REGN10987, that targets the spike protein of SARS-CoV-2, and has shown effectiveness in mouse models.  Trial: Regeneron launched a Phase 1/2/3 trial in June that established safety (NCT04426695), and is proceeding with the Phase 2/3 portion of the trial to evaluate whether the antibody cocktail can effectively treat hospitalized and non-hospitalized COVID-19 patients. The company also launched a separate Phase 3 trial in collaboration with NIAID and NIH to assess whether REGN-COV2 can treat and prevent COVID-19. On 14 September, the RECOVERY trial added REGN-COV2 to its list of treatments being evaluated for COVID-19.  Outcomes: In a press release, Regeneron announced results from the first 275 patients in the trial, which showed REGN-COV2 was effective in reducing viral load, with patients who enrolled with a higher baseline viral level demonstrating greater decrease in viral load, reduction in symptoms, and hospital visits. Status: US President Donald Trump was treated with REGN-COV2 after developing COVID-19. Regeneron has asked the FDA to consider approving REGN-COV2 under an EUA.","developerResearcher":["Regeneron"],"sponsors":["Regeneron"],"trialPhase":"Phase 1/2/3","lastUpdate":"10/9/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["LY-CoV555"],"details":"Background: LY-CoV555 binds to the spike protein receptor in SARS-CoV-2 and can block viruses from binding to the ACE2 host cell surface receptor.  Trials: Lilly has announced a Phase 1 trial evaluating LY-CoV555 in up to 40 patients hospitalized with COVID-19 who will receive the monoclonal antibody or placebo (NCT04411628). LY-CoV555 also is being evaluated in the Phase 2 BLAZE-1 study of 800 participants receiving LY-CoV555 or JS016 (LY-CoV016) as a combination therapy (NCT04427501), and the Phase 3 BLAZE-2 study of residents with COVID-19 at long-term care facilities, which is being conducted together with NIAID, and in ACTIV-2 for patients with symptoms of COVID-19 but who have not been hospitalized. LY-CoV555 is additionally being tested together with Veklury in the ACTIV-3 trial. If Phase 1 trial results are positive, Lilly said future research would focus on non-hospitalized COVID-19 patients.  Outcomes: Results from an interim analysis announced by Lilly on 16 September demonstrated that LY-CoV555 reduced viral clearance by day 11 at the 2800 mg dose. Junshi Biosciences said LY-CoV555 and met their primary endpoints in the BLAZE-1 trial. ACTIV-3 is currently paused due to a \u0022safety concern\u0022 for participants who received LY-CoV555, according to independent reporting from the New York Times.  Status: Lilly has submitted a request for an EUA for LY-CoV555 monotherapy based on results from the BLAZE-1 trial.","developerResearcher":["Lilly","AbCellera"],"sponsors":["Lilly","Operation Warp Speed"],"trialPhase":"Phase 1/2/3","lastUpdate":"10/9/2020"},{"medicationClass":"Immunoglobulin","tradeName":["Convalescent plasma"],"details":"Background: Convalescent plasma has been studied as passive immunotherapy in&nbsp;other coronaviruses&nbsp;such as MERS and in&nbsp;SARS-CoV-2.   Trials: Convalescent plasma is being evaluated against placebos, other treatments, and standard of care in a number of high-profile trials:   NYU Langone Health and Albert Einstein (Recruiting;&nbsp;NCT04364737). Brigham and Women&rsquo;s Hospital (Recruiting;&nbsp;NCT04361253). Cedars-Sinai Medical Center (Recruiting;&nbsp;NCT04353206). Johns Hopkins University (Recruiting;&nbsp;NCT04323800;&nbsp;NCT04377672;&nbsp;NCT04373460). Baylor Research Institute (Not Recruiting;&nbsp;NCT04333251). Stanford University (Not Recruiting;&nbsp;NCT04355767). Stony Brook University (Invitation;&nbsp;NCT04344535). A novel biosynthetic convalescent plasma is also being&nbsp;developed&nbsp;by Immunome after a contract awarded by the Department of Defense.   Outcome: In the first&nbsp;peer-reviewed study&nbsp;of convalescent plasma, 19 of 25 patients (76%) with severe COVID-19 who received convalescent plasma had clinical improvement. In a&nbsp;safety update&nbsp;published in Mayo Clinic Proceedings, mortality improved from 12% as reported in the pre-print to 8.6%. Further evidence from Mayo Clinic researchers&nbsp;posted&nbsp;in the pre-print server&nbsp;medRxiv&nbsp;found convalescent plasma reduced mortality by about 57% compared with standard of care in patients hospitalized with COVID-19. A large study&nbsp;posted&nbsp;in the pre-print server&nbsp;medRxiv&nbsp;from the US Expanded Access Program (EAP) COVID-19 Plasma Consortium of more than 35,000 patients with COVID-19 in an expanded access program found patients had a 7-day mortality rate of 8.7% if they received convalescent plasma 3 days after diagnosis and 11.9% if they received convalescent plasma 4 days after diagnosis; however, the efficacy of the treatment has been&nbsp;called into question&nbsp;due to lack of a placebo group. In a group of 351 patients hospitalized with COVID-19 and given convalescent plasma, the &ldquo;optimal window&rdquo; for administration was within 44 hours, according to a paper of 60-day follow-up data posted to medRxiv.   Regulatory actions: &nbsp;On 23 August, FDA issued an EUA for the use of convalescent plasma for patients hospitalized with suspected or laboratory-confirmed COVID-19. The EUA decision was based on convalescent plasma&rsquo;s history of effectiveness in other coronaviruses, efficacy and safety data in animal models, published studies on safety and efficacy in humans, and data from the National Expanded Access Treatment Protocol led by the Mayo Clinic. However, to date, there has been no data from large-scale randomized clinical trials on the safety and efficacy of convalescent plasma. In a fact sheet issued to providers, FDA emphasized that convalescent plasma is not standard of care for COVID-19, and changes should not be made to current clinical trials of convalescent plasma based on the EUA. FDA previously had allowed the use of convalescent plasma from recovered cases of COVID-19 for patients with &ldquo;serious or immediately life-threatening COVID-19 infections under an&nbsp;emergency investigational new drug&nbsp;(eIND) application.&rdquo; On 23 September, FDA reaffirmed their decision to issue an EUA for convalescent plasma, saying it &ldquo;met the criteria for issuance of an EUA&rdquo; but clarified that convalescent plasma does not meet &ldquo;the same evidentiary standard as required for approval or licensure of a drug or biological product.&rdquo;","developerResearcher":["Various"],"sponsors":["Various"],"trialPhase":"Phase 1/2","lastUpdate":"10/9/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["JS016"],"details":"Background: JS106 binds to the spike protein receptor in SARS-CoV-2 and can block viruses from binding to the ACE2 host cell surface receptor.  Status: Lilly has announced a Phase 1 trial is underway evaluating JS016 in 40 patients with COVID-19, and also is being evalauted in the Phase 2 BLAZE-1 study of 800 participants receiving LY-CoV555 or JS016 (LY-CoV016) as a combination therapy (NCT04427501). Status: Junshi Biosciences said LY-CoV555 and met their primary endpoints in the BLAZE-1 trial. Lilly has submitted a request for an EUA for LY-CoV555 monotherapy based on results from the BLAZE-1 trial.","developerResearcher":["Lilly","Junshi Biosciences"],"sponsors":["Lilly"],"trialPhase":"Phase 1","lastUpdate":"10/9/2020"},{"medicationClass":"IL-6 receptor agonist","tradeName":["Kevzara (sarilumab)"],"details":"Background: Kevzara is indicated to treat moderately to severely active rheumatoid arthritis in adults with inadequate response or intolerance to one or more DMARDs. The drug is being evaluated for its potential benefit in reducing the inflammatory response in the lungs among patients with COVID-19 who develop acute respiratory distress syndrome.  Trials: A Phase 2/3&nbsp;trial&nbsp;of 400 patients sponsored by Sanofi and Regeneron has been completed in the United States (NCT04315298). A second, Phase 2/3 trial was conducted in Italy, Spain, Germany, France, Canada and Russia.  Outcome: Preliminary data from an Italian&nbsp;paper&nbsp;from the Gemelli Against COVID-19 group published in The Lancet indicates Kevzara may be a promising treatment for COVID-19, but concomitant administration of other treatments does not make it clear whether it was Kevzara that provided the benefit. The authors said 83% of patients had clinical improvement after administration. Results from a small study from the SARI-RAF Study Group&nbsp;published&nbsp;in&nbsp;Annals of the Rheumatic Diseases&nbsp;found Kevzara did not perform better than standard care for clinical improvement and mortality in patients with severe COVID-19.  Status: The international trial sponsored by Sanofi and the US trial sponsored by Regeneron have been halted. The international trial did not meet its primary endpoint, and the companies have&nbsp;said&nbsp;they are not continuing clinical studies for Kevzara. Results from the Phase 2 portion of the Regeneron trial&nbsp;released&nbsp;by the company on 27 April showed Kevzara was not effective in treating severe COVID-19 cases or critical cases requiring a ventilator. Regeneron continued the trial with critical cases only and discontinuing the lower-dose treatment arm (200 mg) in favor of the higher-dose arm (400 mg), but&nbsp;results&nbsp;from the Phase 3 portion of the trial showed Kevzara did not meet primary or secondary endpoints compared with supportive care.","developerResearcher":["Sanofi","Regeneron"],"sponsors":["Sanofi","Regeneron"],"trialPhase":"No longer being studied for COVID-19","lastUpdate":"10/9/2020"},{"medicationClass":"Recombinant fusion protein","tradeName":["SACCOVID (CD24Fc)"],"details":"Background: SACCOVID, formerly known as CD24Fc, was recently part of several trials for the prophylactic treatment of graft-versus-host disease (GVHD) in leukemia patients receiving hematopoietic stem cell transplantation. The recombinant fusion protein targets a novel immune pathway checkpoint and modulates immune response through binding to Danger-Associated Molecular Patterns (DAMPS) and sialic acid-binding immunoglobulin-type lectins (Siglecs). The developers of SACCOVID, OncoImmune, believe it can be an effective non-antiviral biological modifier in COVID-19 because of it also showed reduction of multiple inflammatory cytokines in animal models.  Trials: A Phase 3 trial of 230 COVID-19 patients with absolute lymphocyte counts ≤ 800/mm3 in peripheral blood is underway (NCT04317040).  Outcomes: Early results from the trial of the first 70 patients show no adverse reactions to infusion or drug-related adverse events. The mortality rate in the trial, 5%, is “low among severe and critical COVID-19 patients,” OncoImmune’s CEO said. Topline results announced by press release from the company indicate SACCOVID helped reduce time to clinical recovery from 10 days in the placebo group to 6 days, and had \u0022a 60% better chance to achieve clinical recovery\u0022 compared with placebo (P = .005), OncoImmune said. ","developerResearcher":["OncoImmune"],"sponsors":["OncoImmune"],"trialPhase":"Phase 3","lastUpdate":"10/2/2020"},{"medicationClass":"Antihelmintic","tradeName":["Ivermectin"],"details":"Background: Ivermectin is used to treat intestinal strongyloidiasis and onchocerciasis (tablets), lice and rosacea (topical). The drug has been proven effective in vitro of inhibiting SARS-CoV-2 within 48 hours of treatment with a 5,000-fold reduction in the virus, according to a paper published in Antiviral Research.  Trials: Ivermectin is being evaluated against placebo in patients with COVID-19 in the Phase 2/3 IVERCORCOVID19 trial in Argentina (NCT04529525), the Phase 2 COVER trial in Italy and Spain (NCT04438850), a Phase 2/3 trial in Colombia (NCT04405843), the Phase 2 SAINT trial in Spain (NCT04390022), the Phase 2 IFORS trial in Brazil (NCT04431466), and a Phase 3 outpatient study at Temple University in Philadelphia (NCT04530474). The Japanese government also plans to test ivermectin against COVID-19 in a clinical trial, according to Prime Minister Shinzo Abe reported in Pharma Japan. Phase 1 trial in France of ivermectin led by MedinCell is also underway. ","developerResearcher":["Various"],"sponsors":["Various"],"trialPhase":"Phase 2/3","lastUpdate":"10/2/2020"},{"medicationClass":"Anti-TNF","tradeName":["Humira (adalimumab)"],"details":"Background: The University of Oxford is testing whether adalimumab, an anti-tumor necrosis factor drug, helps prevent the progression of COVID-19 to severe disease among patients in community care homes in the United Kingdom. The AVID-CC trial, sponsored by the COVID-19 Therapeutics Accelerator, is planning to enroll up to 750 patients with COVID-19 in care homes across the United Kingdom who will receive adalimumab or standard of care.","developerResearcher":["University of Oxford"],"sponsors":["COVID-19 Therapeutics Accelerator"],"trialPhase":"Phase 2","lastUpdate":"10/2/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["COVI-GUARD (STI-1499)"],"details":"Background: Sorrento Therapeutics, Inc. is developing STI-1499, also called COVI-GUARD, a neutralizing antibody that binds to the S1 subunit of the spike protein in SARS-CoV-2. COVI-GUARD is also part of a neutralizing antibody cocktail of three molecules that Sorrento is calling COVI-SHIELD, which is being developed in partnership with Mount Sinai Hospital in New York City. Pre-clinical results from posted to the pre-print server bioRxiv indicate COVI-GUARD protects against SARS-CoV-2 in Syrian golden hamsters. Trial: The company is planning a Phase 1 trial of COVI-GUARD in 32 patients hospitalized with COVID-19 compared with placebo (NCT04454398). Status: On 16 September, Sorrento received approval from the FDA to proceed with the Phase 1 trial for COVI-GUARD. The company said the ultimate goal is to obtain an EUA for COVI-GUARD by the end of the year.","developerResearcher":["Sorrento Therapeutics"],"sponsors":["Sorrento Therapeutics"],"trialPhase":"Phase 1","lastUpdate":"10/2/2020"},{"medicationClass":"Glucocorticoid","tradeName":["Dexamethasone (Dextenza, Ozurdex, others)"],"details":"Background: Dexamethasone has been selected as a potential therapy due to its potential for reducing the inflammation associated with cytokine release syndrome in patients with COVID-19.  Trials: The drug is currently being evaluated as a treatment arm of the RECOVERY trial.  Outcomes: Preliminary results from the RECOVERY trial  published in the New England Journal of Medicine indicate dexamethasone may help reduce mortality in patients with COVID-19. Of 2,104 patients randomized to receive dexamethasone, the mortality rate was significantly lower in patients on mechanical ventilators compared with those who received usual care (29.3% vs. 41.4%) and in patients receiving oxygen compared with those who received usual care (23.3% vs. 26.2%). Results from the CoDEX trial (NCT04327401) in Brazil showed patients taking dexamethasone had a significant increase in the number of ventilator-free days at 28 days compared with standard of care, according to a paper published in JAMA. CoDEX was stopped early due to results from the RECOVERY trial.  Regulatory Actions: In response to positive preliminary results, the UK and Japan have approved dexamethasone to treat COVID-19; the therapy also has been endorsed by the EMA for use in patients who require oxygen therapy. It is provisionally approved in Taiwan.","developerResearcher":["Various"],"sponsors":["University of Oxford"],"trialPhase":"Phase 2/3","lastUpdate":"9/25/2020"},{"medicationClass":"VIP receptor agonist","tradeName":["PB1046"],"details":"Background: PhaseBio is evaluating their vasoactive intestinal peptide (VIP) receptor agonist PB1046 in hospitalized patients with COVID-19. Results in animal studies demonstrated PB1046 was effective in preventing acute lung injury and stopping inflammatory responses associated with ARDS. A Phase 2 trial of the candidate is underway in up to 210 participants hospitalized with COVID-19 (NCT04433546).","developerResearcher":["PhaseBio"],"sponsors":["PhaseBio"],"trialPhase":"Phase 2","lastUpdate":"9/25/2020"},{"medicationClass":"Antiviral","tradeName":["Galidesivir"],"details":"Background: BioCryst is testing whether galidesivir, an antiviral drug with demonstrated broad-spectrum activity in vitro against coronaviruses MERS and SARS, is effective in treating patients with COVID-19. The company is enrolling up to 132 participants in an NIAID-sponsored trial evaluating whether galidesivir is effective in treating yellow fever or COVID-19 (NCT03891420).","developerResearcher":["BioCryst Pharmaceuticals"],"sponsors":["NIAID"],"trialPhase":"Phase 1b","lastUpdate":"9/25/2020"},{"medicationClass":"Antirheumatic agent","tradeName":["Bucillamine"],"details":"Background: Revive Therapeutics is testing antirheumatic drug Bucillamine in a Phase 3 trial of patients with mild-to-moderate COVID-19. The trial is a randomized, placebo-controlled study of up to 1,000 participants who will receive Bucillamine or placebo three times per day for up to 14 days. Study sites will be located in the U.S., Canada, and Asia-Pacific countries (NCT04504734). Revive has received IRB approval to move forward with the Phase 3 trial. Bucillamine has also been granted compassionate use through IRB approval, the company announced.","developerResearcher":["Revive Therapeutics Ltd."],"sponsors":["Revive Therapeutics Ltd."],"trialPhase":"Phase 3","lastUpdate":"9/18/2020"},{"medicationClass":"Small-molecule inhibitor","tradeName":["PF-00835321 (PF-07304814)"],"details":"Background: Pfizer is evaluating its phosphate prodrug PF-07304814, which metabolizes to PF-00835321 and has shown antiviral activity in vitro against SARS-CoV-2. The company has started a Phase 1b study of up to 56 participants who will receive the therapeutic or placebo (NCT04535167).","developerResearcher":["Pfizer"],"sponsors":["Pfizer"],"trialPhase":"Phase 1b","lastUpdate":"9/18/2020"},{"medicationClass":"Anticoagulant","tradeName":["Eliquis (Apixaban)"],"details":"Background: Researchers from NIH have launched NIH ACTIV-4 Outpatient trial, which will evaluate if anticoagulants or antithrombotic therapy has an effect on reducing cardiovascular or pulmonary complications that develop as a result of COVID-19. In the Phase 3 ACTIV-4 Outpatient trial, participants will be randomized to receive the anticoagulant apixaban, aspirin, or a placebo.","developerResearcher":["NHLBI"],"sponsors":["Operation Warp Speed"],"trialPhase":"Phase 3","lastUpdate":"9/11/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["Takhzyro (lanadelumab)"],"details":"Background: Japanese pharmaceutical company Takeda is investigating whether lanadelumab, a monoclonal antibody currently being studied as a treatment for patients with hereditary angioedema, is effective in reducing fluid build-up in the lungs of patients with COVID-19. Lanadelumab blocks the activation of bradykinin, which has been theorized to be responsible for vascular dilation, vascular permeability and hypotension when bradykinin levels increase during COVID-19. Trial: Takeda is conducting a Phase 1 study of up to 24 participants analyzing lanadelumab against standard of care for COVID-19 associated pneumonia (NCT04460105).","developerResearcher":["Takeda (Shire)"],"sponsors":["Takeda (Shire)"],"trialPhase":"Phase 1b","lastUpdate":"9/11/2020"},{"medicationClass":"Glucocorticoid","tradeName":["Hydrocortisone"],"details":"Background: Hydrocortisone is being evaluated in several trials as a treatment to reduce or prevent lung injury and multisystem organ dysfunction associated with COVID-19. Other glucocorticoids such as dexamethasone have been shown to be effective in hospitalized patients who are mechanically ventilated. Trials: In Denmark, hydrocortisone is being evaluated in a Phase 3 trial of up to 1,000 participants with COVID-19 and severe hypoxia (NCT04348305). It also is being studied in France at Tours University Hospital in a subgroup of participants in the Phase 3 CAPE_COD trial evaluating its effect on treating community-acquired pneumonia (NCT02517489). Outcomes: A meta-analysis of studies from the WHO Rapid Evidence Appraisal for COVID-19 Therapies (REACT) Working Group analyzing the effect of dexamethasone, hydrocortisone, and methylprednisolone on mortality in patients with COVID-19 found systemic corticosteroids were effective in reducing 28-day mortality compared with usual care. Results from CAPE_COD published in JAMA found low-dose hydrocortisone was not effective in reducing mortality or persistent respiratory support compared with placebo, but researchers suggested the study may have been underpowered to detect a significant difference in outcomes. Results from the REMAP-CAP COVID-19 Corticosteroid Domain Randomized Clinical Trial, also published in JAMA, suggested hydrocortisone may be beneficial for patients with COVID-19, but the trial was stopped early. Status: Treatment guidelines released by NIH on 27 August recommend the use of dexamethasone at a dose of 6 mg per day for hospitalized patients with COVID-19 who meet certain criteria, or the use of prednisone, methylprednisolone, or hydrocortisone when dexamethasone is not available.","developerResearcher":["Various"],"sponsors":["Various"],"trialPhase":"Phase 3","lastUpdate":"9/4/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["Ilaris (canakinumab)"],"details":"Background: Ilaris is a monoclonal antibody that targets interleukin (IL)-1β. Two studies published in The Lancet of COVID-19 showed patients had elevated levels of IL-1β and other cytokines during cytokine release syndrome.  It is approved to treat cryopyrin-associated periodic syndromes (FDA, European Medicines Agency); tumor necrosis factor receptor associated periodic syndrome, hyperimmunoglobulin D syndrome/mevalonate kinase deficiency, and familial mediterranean fever (FDA).  Trials: Novartis is conducting the Phase 3 CAN-COVID trial to evaluate whether Ilaris can treat cytokine release syndrome in patients with COVID-19. The company plans to enroll 450 patients from France, Germany, Italy, Spain, UK and the US (NCT04362813). Ilaris is also being evaluated in the canakinumab in Covid-19 Cardiac Injury (The Three C Study) in up to 45 participants hospitalized for COVID-19 with elevations in troponin and C‐reactive protein (NCT04365153).  Outcomes: A retrospective review of 10 patients published in The Lancet found that Ilaris reduced serum C-reactive protein early in treatment (day 1 and day 3) and improved oxygenation at day 3 and day 7. At 45 days post-hospitalization, no patients had died and all had been discharged.  Status: Novartis expects results from the trial by “mid-summer,” according to a company press release.","developerResearcher":["Novartis"],"sponsors":["Novartis"],"trialPhase":"Phase 3","lastUpdate":"8/28/2020"},{"medicationClass":"Antigout agent","tradeName":["Colchicine (Mitigare, Colcrys)"],"details":"Background: Colchicine, an anti-inflammatory drug primarily used to treat gout, is being evaluated as a therapeutic candidate for COVID-19. Pre-clinical studies have shown use of colchicine reduces lung injury in patients with ARDS, and could be useful for the treatment of severe COVID-19 symptoms. Researchers at the Montreal Heart Institute are evaluating colchicine in a Phase 3 randomized, double-blind, placebo-controlled trial of up to 6,000 participants with high-risk COVID-19 (NCT04322682).","developerResearcher":["NHLBI","Bill and Melinda Gates Foundation","Government of Quebec"],"sponsors":["Montreal Heart Institute"],"trialPhase":"Phase 3","lastUpdate":"8/28/2020"},{"medicationClass":"Small-molecule protein inhibitor","tradeName":["BLD-2660"],"details":"Background: BLD-2660, an oral small-molecule inhibitor of calpain, is being investigated as a therapeutic candidate for treating pneumonia associated with COVID-19. Its developer, Blade Therapeutics, is performing a Phase 2 randomized, double-blinded, placebo-controlled trial of BLD-2660 in up to 120 participants hospitalized with COVID-19 (NCT04334460) The company said the candidate is also being tested with concomitant remdesivir, according to a press release.","developerResearcher":["Blade Therapeutics"],"sponsors":["Blade Therapeutics"],"trialPhase":"Phase 2","lastUpdate":"8/28/2020"},{"medicationClass":"Biguanide","tradeName":["Metformin (Glucophage, Glumetza, Riomet)"],"details":"Background: Metformin, an oral medication used to treat type 2 diabetes, is being evaluated as a therapeutic candidate for COVID-19. Early results from Wuhan, China, suggested metformin helped reduce the risk of mortality from COVID-19 in patients with type 2 diabetes. Trial: Researchers at the University of Minnesota are planning the Phase 2/3 MET-Covid trial with 1,522 participants to assess whether metformin is able to reduce COVID-19 severity, prevent symptomatic disease from COVID-19, and/or prevent SARS-CoV-2 infection (NCT04510194). Outcomes: In a retrospective study  of 25,326 patients with COVID-19 presented in the pre-print server medRxiv, diabetes carried a significantly higher risk of mortality (odds ratio, 3.62; 95% confidence interval, 2.11-6.2; P published in Diabetes & Metabolism notes the potential of metformin in reducing mortality in patients with diabetes, but cautions that randomized clinical trials are needed. ","developerResearcher":["University of Minnesota"],"sponsors":["University of Minnesota"],"trialPhase":"Phase 2/3","lastUpdate":"8/21/2020"},{"medicationClass":"Antiviral","tradeName":["Avigan (favilavir/avifavir)"],"details":"Background: Reports from officials in China have said Avigan is clinically effective against COVID-19.  Regulatory Actions: Avigan is approved in Italy to treat COVID-19, and in China as an experimental drug for COVID-19. Avifavir, a generic form of Avigan, has been approved to treat COVID-19 in Russia.  Trials: Six trials in China are evaluating favilavir against other antivirals such as baloxavir and marboxil in patients with COVID-19. Fujifilm announced a Phase 3 clinical trial to evaluate the safety and efficacy of Avigan in Japan for patients of COVID-19. In Canada, Appili Therapeutics announced they are conducting a Phase 2 trial of favilavir with 760 participants (residents and staff) in long-term care facilities. A 330-person trial of avifavir in Russia is ongoing. A randomized trial in the Philippines pitting Avigan against standard of care in four hospitals is also planned.  Outcomes: Recent data appears to show lack of efficacy of Avigan in treating COVID-19. A study presented in the pre-print server medRxiv of 240 patients that evaluated favilavir against Arbidol (umifenovir, a broad-spectrum antiviral used for influenza) showed neither drug was more effective at improving the clinical recovery rate of patients. Interim data from Japan suggested the favilavir was not effective in treating mild or moderate cases of COVID-19, which was confirmed by a press release from researchers in Fujita Health University.  Status: Trials have various dates of completion.","developerResearcher":["Fujifilm Toyama Chemical (as Avigan)","Zhejiang Hisun Pharmaceutical"],"sponsors":["Various"],"trialPhase":"Phase 2/3","lastUpdate":"8/21/2020"},{"medicationClass":"Recombinant human plasma","tradeName":["Rhu-pGSN (gelsolin)"],"details":"Background: BioAegis Therapeutics is assessing whether Rhu-pGSN, their recombinant human plasma product, is effective in treating hospitalized patients with COVID-19 who have developed pneumonia. Rhu-pGSN has shown in pre-clinical testing to regulate inflammation and has the potential to suppress cytokine release syndrome associated with COVID-19. Trial: The company has been approved by The Spanish Agency for Medicines and Health Products (AEMPS) to test whether Rhu-pGSN performs better than placebo in a randomized, blinded, placebo controlled trial (NCT04358406).","developerResearcher":["BioAegis Therapeutics"],"sponsors":["BioAegis Therapeutics"],"trialPhase":"Phase 2","lastUpdate":"8/21/2020"},{"medicationClass":"Dihydroorotate dehydrogenase (DHODH) inhibitor","tradeName":["PTC299"],"details":"Background: PTC has said PTC299 has the potential to address the high level of viral replication and inflammatory response associated with COVID-19. Results from a pre-print paper published in bioRxiv indicate the therapeutic is effective at inhibiting replication of SARS-CoV-2 and suppressed IL-6, IL-17A, IL-17F, and vascular endothelial growth factor in tissues cultures.  Trial: A Phase 2/3 trial is underway to evaluate PTC299 in the U.S. (NCT04439071), and additional trials are planned in Europe, Brazil and Australia. ","developerResearcher":["PTC"],"sponsors":["PTC"],"trialPhase":"Phase 2/3","lastUpdate":"8/14/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["PRO 140 (leronlimab)"],"details":"Background: PRO 140 is a CCR5 antagonist that blocks the CCR5 co-receptor on the surface of immune cells like CD4 cells. It is believed that PRO 140 can enhance the immune response in patients experiencing cytokine release syndrome from respiratory distress caused by COVID-19. PRO 140 has received FDA fast track designation for use with carboplatin to treat CCR5-positive metastatic triple-negative breast cancer and in combination with highly active antiretroviral therapy (HAART) in HIV.  Trials: CytoDyn has launched two Phase 2 clinical trials evaluating PRO 140 in patients with mild to moderate (NCT04343651) and severe (NCT04347239) cases of COVID-19. In the trial of severe COVID-19 cases, announced on 1 April, CytoDyn aims to enroll 342 patients and administer PRO 140 or placebo for 2 weeks with a primary endpoint of 14-day mortality. Another trial in collaboration with the Mexican National Institutes of Health is also planned.  Outcome: FDA authorized use of PRO 140 in COVID-19 patients under an eIND. Patients treated under the eIND have a lower level of cytokine release syndrome and lower levels of IL-6 and TNF-alpha. A pre-print of results from the trial evaluating severely or critically ill COVID-19 patients showed leronlimab was effective at reducing IL-6 expression and in reversing immunosuppression, which led to a lower plasma viral load. Topline results released by the company from a Phase 2 trial of mild-to-moderate COVID-19 patients found PRO 140 had an improvement in total clinical symptom score compared with placebo (90% vs. 71%).  Status: A Phase 2b trial has enrolled 15 patients with mild-to-moderate COVID-19 and one patient with severe disease has been treated in a Phase 2b/3 trial, CytoDyn announced. On 30 April, CytoDyn’s CEO noted that 49 patients treated with PRO 140 under eIND were responding “extremely well.” Preliminary safety data from the Phase 2 trial released as a press release by CytoDyn show PRO 140 performed better than placebo with regard to serious adverse events.","developerResearcher":["CytoDyn"],"sponsors":["CytoDyn"],"trialPhase":"Phase 2","lastUpdate":"8/14/2020"},{"medicationClass":"Antiviral","tradeName":["MK-4482"],"details":"Background: MK-4482 (formerly EIDD-2801) is an oral broad-spectrum antiviral that has shown effectiveness against infections such as influenza, chikungunya, Ebola and equine encephalitis. It has a similar mechanism of action to remdesivir and prevents replication of the virus. In animal models, MK-4482 inhibited the replication of SARS-CoV-2 and MERS, according to a recent paper.  Regulatory actions: On 8 April, the FDA authorized use of MK-4482 for COVID-19 under an investigative new drug (IND) application. On 13 April, MHRA cleared MK-4482 for human testing.  Status: Emory is launching a Phase 2 trial evaluating MK-4482 in humans after seeing success in humans with the therapeutic in Phase 1 trials. Merck has an agreement with Ridgeback Biotherapeutics to co-develop MK-4482 and related molecules. Merck is planning studies of MK-4482 in hospitalized (NCT04575584) and non-hospitalized (NCT04575597) adults with COVID-19, but the trials are not yet recruiting.","developerResearcher":["DRIVE","Ridgeback Biotherapeutics","Merck"],"sponsors":["Ridgeback Biotherapeutics"],"trialPhase":"Phase 2","lastUpdate":"8/6/2020"},{"medicationClass":"Angiotensin-(1–7) peptide","tradeName":["TXA127"],"details":"Background: Constant Therapeutics is testing its peptide angiotensin-(1-7) drug TXA127 in a Phase 2 clinical trial. The peptide is a Mas receptor agonist which has demonstrated efficacy in reducing inflammation, stabilizing endothelial and epithelial barriers, and reducing fibrosis in the lungs of animal models. Study Design: A randomized, parallel, double-blinded, placebo-control, Phase 2 trial of 100 patients with moderate COVID-19 (NCT04401423).","developerResearcher":["Constant Therapeutics"],"sponsors":["Columbia University Irving Medical Center"],"trialPhase":"Phase 2","lastUpdate":"7/30/2020"},{"medicationClass":"PIKfyve inhibitor","tradeName":["LAM-002A (apilimod dimesylate)"],"details":"Background: AI Therapeutics and the Yale Center for Clinical Investigation are examining the efficacy of LAM-002A, a PIKfyve kinase inhibitor, in newly diagnosed patients with COVID-19. Preliminary research has shown LAM-002A combats SARS-CoV-2, especially in lung cells. Study Design: A phase 2 randomized, double-blind, placebo-controlled trial of about 142 participants who will receive LAM-002A 125mg in five 25-mg capsules twice per day for 10 days, or microcrystalline cellulose as a placebo (NCT04446377).","developerResearcher":["AI Therapeutics, Inc."],"sponsors":["AI Therapeutics, Inc.","Yale University"],"trialPhase":"Phase 2","lastUpdate":"7/30/2020"},{"medicationClass":"RIPK1 inhibitor","tradeName":["DNL758 (SAR443122)"],"details":"Background: Biopharmaceutical company Denali Therapeutics and Sanofi are partnering to test DNL758, a peripherally-restricted small molecule inhibitor of RIPK1, in a Phase 1b study of patients hospitalized with severe COVID-19. DNL758 is thought to reduce excessive inflammation associated with severe cases of COVID-19, according to a company press release. Study Design: A Phase 1b, randomized, double-blinded, placebo-controlled trial of 67 participants hospitalized with severe COVID-19 (NCT04469621).","developerResearcher":["Sanofi","Denali Therapeutics"],"sponsors":["Sanofi"],"trialPhase":"Phase 1b","lastUpdate":"7/30/2020"},{"medicationClass":"Nitric oxide","tradeName":["INOpulse"],"details":"Background: Inhaled nitric oxide has been explored as a treatment for COVID-19 patients due to its success in improving arterial oxygenation in patients with ARDS due to SARS-CoV. Results from patients treated with INOpulse under an emergency expanded access program have proved promising, the company said.  Regulatory Actions: FDA allowed INOpulse for compassionate use in COVID-19 patients on 20 March.  Trials: Bellerophon is performing the Phase 3 randomized, placebo-controlled COViNOX study to evaluate the safety and efficacy of INOpulse in up to 500 COVID-19 patients where supplemental oxygen is needed prior to a patient requiring mechanical ventilation support. The primary endpoints are respiratory failure and mortality of patients in both groups (NCT04421508).  Status: The FDA approved an IND for the therapy to proceed to a Phase 3 trial, which is currently underway.","developerResearcher":["Bellerophon Therapeutics"],"sponsors":["Bellerophon Therapeutics"],"trialPhase":"Phase 3","lastUpdate":"7/16/2020"},{"medicationClass":"HIV-1 Rev protein inhibitor","tradeName":["ABX464"],"details":"Background: ABX464 has anti-inflammatory properties through its upregulation of miR-124 micro-RNA, which downregulates chemo- and cytokines causing cytokine release syndrome in patients with COVID-19. The candidate also has antiviral effects against HIV and has been effective in treating patients with ulcerative colitis. Trial: The company is enrolling patients in a Phase 2b/3 trial of 1,034 high-risk patients in Europe and Latin America across 50 study sites (NCT04393038).","developerResearcher":["Abivax"],"sponsors":["Abivax"],"trialPhase":"Phase 2b/3","lastUpdate":"7/9/2020"},{"medicationClass":"Autologous adipose-derived stem cells","tradeName":["AdMSCs"],"details":"Background: Previous research has shown ACE2- mesenchymal stem cells were safe and effective in treating pneumonia associated with COVID-19.  Trial: A Phase 2, multicenter, double-blinded study of 200 healthy participants where 100 participants who have already banked their AdMSCs with Celltex will receive three infusions of cells to test whether they have a prophylactic effect against COVID-19 (NCT04428801).  Regulatory Actions: FDA has approved an IND to evaluate AdMSCs in a Phase 2 study.","developerResearcher":["Celltex Therapeutics"],"sponsors":["Celltex Therapeutics"],"trialPhase":"Phase 2","lastUpdate":"7/2/2020"},{"medicationClass":"Mitogen-activated protein kinase (MAPK) inhibitor","tradeName":["Losmapimod"],"details":"Background: Losmapimod is a p38α/β MAPK inhibitor thought to reduce the inflammatory response associated with disease progression in COVID-19 by reducing inflammatory biomarkers such as C-reactive protein and IL-6.  Trials: Fulcrum is launching the Phase 3 LOSVID study, which will evaluate around 400 patients with COVID-19 who will receive a dose of the drug or placebo (NCT04511819).  Regulatory Actions: FDA has approved an IND to test losmapimod in the Phase 3 study.","developerResearcher":["Fulcrum Therapeutics"],"sponsors":["Fulcrum Therapeutics"],"trialPhase":"Phase 3","lastUpdate":"6/25/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["Mavrilimumab"],"details":"Background: The potential treatment is designed to antagonize GM-CSF signaling by binding to the alpha subunit of the GM-CSF receptor (GM-CSFRα). Kiniksa’s lead indication for mavrilimumab is giant cell arteritis.  Regulatory Actions: The FDA has approved an IND for a Phase 2/3 trial of mavrilimumab.  Trials: Researchers at the Cleveland Clinic are recruiting 60 participants in a prospective, Phase 2 trial evaluating early mavrilimumab treatment for respiratory failure in patients with COVID-19 (NCT04399980). Kiniksa is also conducting an international Phase 2/3 trial of about 570 participants evaluating two dose levels of mavrilimumab for patients with COVID-19 and pneumonia (NCT04447469).  Outcomes: Early reports of mavrilimumab showed early resolution of fever and improved oxygenation within one to three days without requiring mechanical ventilation, according to Kiniksa. Results from The Lancet show patients treated with mavrilimumab had better clinical outcomes compared with a control group at 28-day follow-up.  Status: A consortium of US academic sites is initiating parallel prospective, interventional studies with mavrilimumab in patients with severe COVID-19 pneumonia and hyperinflammation.","developerResearcher":["Kiniksa Pharmaceuticals"],"sponsors":["The Cleveland Clinic"],"trialPhase":"Phase 2","lastUpdate":"6/18/2020"},{"medicationClass":"Kinase inhibitor","tradeName":["Calquence (acalabrutinib)"],"details":"Background: Mantle cell lymphoma (MCL) for patients who have received at least one prior therapy and chronic lymphocytic leukemia (CLL) in the US. Calquence inhibits the enzyme Bruton’s tyrosine kinase (BTK). The BTK pathway has been implicated in TNF-alpha, IL-6, IL-10, and MCP-1 production and early data from the CALAVI trial has shown that Calquence is effective in reducing respiratory distress caused by COVID-19.  Trials: AstraZeneca is testing whether 428 participants in the CALAVI trial with COVID-19 and respiratory distress respond to standard of care with and without Calquence in the United States (NCT04380688) and internationally (NCT04346199).  Outcomes: A peer review of 19 individuals treated with Calquence published in the journal Science Immunology showed 8 of 11 patients (72.7%) requiring supplemental oxygen after being hospitalized for COVID-19 had their oxygenation improve to the point where they no longer required assistance, and 4 of 8 patients (50%) on mechanical ventilation had been extubated. C-reactive protein and IL-6 normalized in patients shortly after treatment.  Status: The trial is not currently recruiting. AstraZeneca has said preliminary results with Calquence are positive and hope they are confirmed in CALAVI.","developerResearcher":["AstraZeneca"],"sponsors":["AstraZeneca"],"trialPhase":"Phase 2","lastUpdate":"6/11/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["Gimsilumab"],"details":"Background: Gimsilumab targets the pro-inflammatory cytokine granulocyte-macrophage colony stimulating factor (GM-CSF), which researchers have seen elevated in the blood of patients with COVID-19 and may be associated with acute respiratory distress syndrome in these patients.  Trials: Roivant has announced their randomized, double-blinded, placebo-controlled BREATHE trial will evaluate the efficacy of intravenous gimsilumab in 270 patients with COVID-19 with ARDS or lung injury (NCT04351243) .  Status: On 15 April, Roivant announced the first patient in the trial had been treated. On 13 May, Roivant said they would allow participants in the BREATHE trial to use convalescent plasma or antiviral agents like remdesivir in addition to receiving gimsilumab or placebo.","developerResearcher":["Roivant Sciences"],"sponsors":["Roivant Sciences"],"trialPhase":"Phase 2","lastUpdate":"5/14/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["Otilimab"],"details":"Background: Otilimab is an anti-GM-CSF antibody developed and currently being evaluated for rheumatoid arthritis. GSK has identified the drug as a potential candidate for COVID-19 treatment in patients who experience cytokine release syndrome.  Trials: GSK is sponsoring the randomized Phase 2 OSCAR trial of 800 participants with COVID-19 who will receive standard of care plus either a single IV infusion of otilimab or placebo (NCT04376684).  Status: The trial is currently recruiting, and began testing as of 16 June, according to GSK.","developerResearcher":["MorphoSys","GSK"],"sponsors":["GSK"],"trialPhase":"Phase 2","lastUpdate":"5/7/2020"},{"medicationClass":"Oral sodium-glucose co-transporter 2 (SGLT2) inhibitor","tradeName":["Farxiga (dapagliflozin)"],"details":"Background: Farxiga is primarily used to treat type 2 diabetes by promoting glucosuria. In the DECLARE CV trial, the drug was associated with a lower rate of heart failure resulting in hospitalization and cardiovascular death. Other trials have shown Farxiga also has kidney-protective effects. Farxiga is used to treat type 2 diabetes and heart failure with reduced ejection fraction.  Trials: AstraZeneca is evaluating Farxiga in a Phase 3 trial of 900 participants with COVID-19 and comorbid conditions such as hypertension, type 2 diabetes, atherosclerotic cardiovascular disease, heart failure, and/or stage 3-4 chronic kidney disease (NCT04350593).","developerResearcher":["Bristol-Myers Squibb"],"sponsors":["AstraZeneca"],"trialPhase":"Phase 3","lastUpdate":"5/4/2020"},{"medicationClass":"Monoclonal antibody","tradeName":["Ultomiris (ravulizumab)"],"details":"Background: Ultomiris is C5 complement inhibitor originally engineered from eculizumab to have a longer-lasting half-life and longer intervals between dosing for treatment of paroxysmal nocturnal hemoglobinuria. Preclinical data of animal models published in the open-access journal mBio suggested the treatment lowers cytokine and chemokine levels in viral pneumonia. Alexion said patients with COVID-19 accessing eculizumab through compassionate use programs also have shown some clinical benefit.  Trials: Alexion is conducting a Phase 3 global study of 270 patients with COVID-19 hospitalized with severe pneumonia randomized to receive weight-based loading dose of Ultomiris followed by a weight-based dose on day 5 and day 10, and a 900-mg dose on day 15 (NCT04369469).  Regulatory Actions: The FDA has approved an IND for Ultomiris to treat patients with severe COVID-19, according to a company press release.  Status: The trial is slated to begin in May 2020.","developerResearcher":["Alexion"],"sponsors":["Alexion"],"trialPhase":"Phase 3","lastUpdate":"4/30/2020"}]}'''
