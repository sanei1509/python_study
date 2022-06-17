#!/usr/bin/env python3
"""Vamos a crear un script que busque trabajos"""
"""mediante web scrapping"""
import requests # python3 -m pip install requests beautifulsoup4
from bs4 import BeautifulSoup


"""url de la page a la que queremos realizar la busqueda"""
url = "https://www.seek.co.nz/python-jobs?salaryrange=100000-999999&salarytype=annual"
url_simple = "https://www.seek.co.nz/"

if __name__ == "__main__":
    """llamamos a la url en la que queremos buscar"""
    page = requests.get(url)
    """el contenido que nos esta extrayendo de esta url que lo parsee"""
    soup = BeautifulSoup(page.content, "html.parser")


    def buscador_data(tag):
        """
        cada bloque de oferta laboral en seek.co cuenta con
        un atributo que se ("data-search-sol-meta")
        """
        return tag.has_attr("data-search-sol-meta") #buscamos todas esas ofertas


    """guardamos todo el html que nuestra función haya interpretado""" 
    result = soup.find_all(buscador_data) #devuelve un listado de resultados html

    """iteramos ese listado"""
    for job in results:
        try:
            """vamos extraer los datos que queramos"""
            titulo = job.find("a", attrs={"data-automation": jobTitle}).get_text()
            compania = job.find("a", attrs={"data-automation": "jobCompany"}).get_text()
            linkTrabajo = url_simple + job.find("a", attrs={"data-automation": "jobTitle"})["href"]
            salario = job.find("span", attrs={"data-automation": "jobSalary"})

            """mostramos esta información como queramos verla"""
            job = "Titulo: {}\nEmpresa: {}\nSalario: {}\Link: {}a\n"
            job = job.format(titulo, compania, linkTrabajo, salario, jobLink)

        except Exception as e:
            print(f"Exception: {e}")
            pass


        #para usarlo -> ejecutar python3 >> file.txt

