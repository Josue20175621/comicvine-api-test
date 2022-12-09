def format_date(date: str) -> str:
    """ Converts ISO 8601 format to 'Month Day, Year' """
    year, month, day = date.split("-")
    d = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", 
            "06": "June", "07": "July", "08": "August", 
            "09": "September", "10": "October", "11": "November", "12": "December"}
    
    return f"{d[month]} {day}, {year}"
