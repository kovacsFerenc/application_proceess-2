import psycopg2
import sys


def init_database(query):
    connect_str = "dbname='ferenc' user='ferenc' host='localhost' password='Humu7894'"
    try:
        conn = psycopg2.connect(connect_str)
    except psycopg2.OperationalError:
        print("I think your connection string is not correct")
        print("...")
        return False
    cursor = conn.cursor()
    cursor.execute(query)
    rows = list(cursor)
    # convert sql request to list
    return rows
    # If nothing to stop you.


def show_mentors_and_school():
    query = """  SELECT mentors.last_name, mentors.first_name, schools.name, schools.country
                 FROM mentors
                    JOIN schools 
                      ON mentors.city = schools.city
                 ORDER BY mentors.id; """
    done = init_database(query)
    return done


def all_school():
    query = """ SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                FROM mentors
                  RIGHT OUTER JOIN schools
                     ON mentors.city = schools.city
                ORDER BY mentors.id; """
    final = init_database(query)
    return final


def mentors_by_country():
    query = """ SELECT schools.country
                FROM mentors
                LEFT JOIN schools
                        ON mentors.city = schools.city
                GROUP BY country; """
    bip = init_database(query)
    return bip


def contacts_page():
    query = """ SELECT schools.name, mentors.first_name, mentors.last_name
                FROM schools
                  INNER JOIN mentors
                          ON mentors.id = schools.contact_person
                ORDER BY schools.name; """
    finale = init_database(query)
    return finale


def applicants():
    query = """ SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                FROM applicants
                  JOIN applicants_mentors
                    ON applicants.id = applicants_mentors.applicant_id
                    WHERE applicants_mentors.creation_date > '2016-01-01'
                ORDER BY applicants_mentors.creation_date DESC; """
    doner = init_database(query)
    return doner


def applicants_and_mentor():
    query = """ SELECT applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name
                FROM applicants
                   LEFT JOIN applicants_mentors
                          ON applicants.id = applicants_mentors.applicant_id
                   LEFT JOIN mentors
                          ON applicants_mentors.mentor_id = mentors.id
                ORDER BY applicants.id; """
    finalé = init_database(query)
    return finalé





