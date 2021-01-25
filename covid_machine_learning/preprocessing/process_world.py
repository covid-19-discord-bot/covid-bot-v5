# coding=utf-8
import csv


def process_data(name: str = "OWID_WRL") -> list:
    all_data = []
    with open("../data_sources/all_data.csv") as f:
        data_reader = csv.reader(f)
        for i in data_reader:
            all_data.append(i)

    total_data = [["index",
                   "total_cases",
                   "new_cases",
                   "total_deaths",
                   "new_deaths",
                   "icu_patients",
                   "hosp_patients",
                   "weekly_icu_admissions",
                   "weekly_hosp_admissions",
                   "total_tests",
                   "tests_per_case",
                   "total_vaccinations",
                   "stringency_index"]]
    z = list(filter(lambda x: x[0] == name, all_data))
    for i, index in zip(z, range(1, len(z))):
        td = [index]
        for j in [4, 5, 7, 8, 17, 19, 21, 23, 25, 32, 34, 39]:
            if i[j] != "":
                td.append(int(float(i[j])))
            else:
                td.append("")
        total_data.append(td)
    return total_data


def process_world():
    world_data = process_data()

    with open("../data_sources/WRL_data.csv", "w") as f:
        data_writer = csv.writer(f)
        data_writer.writerows(world_data)


def process_country(iso_code: str):
    if len(iso_code) != 3:
        raise ValueError("A ISO3 code must be passed to process_country!")
    iso_code = iso_code.upper()
    world_data = process_data(iso_code)

    with open(f"../data_sources/{iso_code}_data.csv", "w") as f:
        data_writer = csv.writer(f)
        data_writer.writerows(world_data)


if __name__ == "__main__":
    process_world()
    process_country("USA")
