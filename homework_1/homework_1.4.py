#В строке "Ivanou Ivan" поменяйте местами слова:"Ivanou Ivan" => "Ivan Ivanou"

family_name="Ivanou Ivan"
print(family_name)
family,name= family_name.split(" ")
name_family = f"{name} {family}"
print(name_family)

