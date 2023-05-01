folder = r"/var/www/html/templating_project/main/firstapp"
workbook = "Arwal"
worksheet = "Arwal"
start_column = "A"
end_column = "N"
start_row = 1
end_row = 75
convert_to = "Unicode" #KrutiDev or Unicode

# Import packages
import pandas as pd
import sys
import utils

# const util = require('util');
# # // Set the default string encoding to UTF-8
# Buffer.defaultEncoding = 'utf-8';

# # reload(sys)
# sys.setdefaultencoding("utf-8")

# KrutiDev to Unicode function
def KrutiDev_to_Unicode(krutidev_substring):
    
    modified_substring = krutidev_substring.encode('utf-8')
    
    array_one = ["ñ","Q+Z","sas","aa",")Z","ZZ","‘","’","“","”",
    
    "å",  "ƒ",  "„",   "…",   "†",   "‡",   "ˆ",   "‰",   "Š",   "‹", 
    
    "¶+",   "d+", "[+k","[+", "x+",  "T+",  "t+", "M+", "<+", "Q+", ";+", "j+", "u+",
    "Ùk", "Ù", "Dr", "–", "—","é","™","=kk","f=k",  
    
    "à",   "á",    "â",   "ã",   "ºz",  "º",   "í", "{k", "{", "=",  "«",   
    "Nî",   "Vî",    "Bî",   "Mî",   "<î", "|", "K", "}",
    "J",   "Vª",   "Mª",  "<ªª",  "Nª",   "Ø",  "Ý", "nzZ",  "æ", "ç", "Á", "xz", "#", ":",
    
    "v‚","vks",  "vkS",  "vk",    "v",  "b±", "Ã",  "bZ",  "b",  "m",  "Å",  ",s",  ",",   "_",
    
    "ô",  "d", "Dk", "D", "[k", "[", "x","Xk", "X", "Ä", "?k", "?",   "³", 
    "pkS",  "p", "Pk", "P",  "N",  "t", "Tk", "T",  ">", "÷", "¥",
    
    "ê",  "ë",   "V",  "B",   "ì",   "ï", "M+", "<+", "M",  "<", ".k", ".",    
    "r",  "Rk", "R",   "Fk", "F",  ")", "n", "/k", "èk",  "/", "Ë", "è", "u", "Uk", "U",   
    
    "i",  "Ik", "I",   "Q",    "¶",  "c", "Ck",  "C",  "Hk",  "H", "e", "Ek",  "E",
    ";",  "¸",   "j",    "y", "Yk",  "Y",  "G",  "o", "Ok", "O",
    "'k", "'",   "\"k",  "\"",  "l", "Lk",  "L",   "g", 
    
    "È", "z", 
    "Ì", "Í", "Î",  "Ï",  "Ñ",  "Ò",  "Ó",  "Ô",   "Ö",  "Ø",  "Ù","Ük", "Ü",
    
    "‚",    "ks",   "kS",   "k",  "h",    "q",   "w",   "`",    "s",    "S",
    "a",    "¡",    "%",     "W",  "•", "·", "∙", "·", "~j",  "~", "\\","+"," ः",
    "^", "*",  "Þ", "ß", "(", "¼", "½", "¿", "À", "¾", "A", "-", "&", "&", "Œ", "]","~ ","@"]
    
    array_two = ["॰","QZ+","sa","a","र्द्ध","Z","\"","\"","'","'",
    
    "०",  "१",  "२",  "३",     "४",   "५",  "६",   "७",   "८",   "९",   
    
    "फ़्",  "क़",  "ख़", "ख़्",  "ग़", "ज़्", "ज़",  "ड़",  "ढ़",   "फ़",  "य़",  "ऱ",  "ऩ",    
    "त्त", "त्त्", "क्त",  "दृ",  "कृ","न्न","न्न्","=k","f=",
    
    "ह्न",  "ह्य",  "हृ",  "ह्म",  "ह्र",  "ह्",   "द्द",  "क्ष", "क्ष्", "त्र", "त्र्", 
    "छ्य",  "ट्य",  "ठ्य",  "ड्य",  "ढ्य", "द्य", "ज्ञ", "द्व",
    "श्र",  "ट्र",    "ड्र",    "ढ्र",    "छ्र",   "क्र",  "फ्र", "र्द्र",  "द्र",   "प्र", "प्र",  "ग्र", "रु",  "रू",
    
    "ऑ",   "ओ",  "औ",  "आ",   "अ", "ईं", "ई",  "ई",   "इ",  "उ",   "ऊ",  "ऐ",  "ए", "ऋ",
    
    "क्क", "क", "क", "क्", "ख", "ख्", "ग", "ग", "ग्", "घ", "घ", "घ्", "ङ",
    "चै",  "च", "च", "च्", "छ", "ज", "ज", "ज्",  "झ",  "झ्", "ञ",
    
    "ट्ट",   "ट्ठ",   "ट",   "ठ",   "ड्ड",   "ड्ढ",  "ड़", "ढ़", "ड",   "ढ", "ण", "ण्",   
    "त", "त", "त्", "थ", "थ्",  "द्ध",  "द", "ध", "ध", "ध्", "ध्", "ध्", "न", "न", "न्",    
    
    "प", "प", "प्",  "फ", "फ्",  "ब", "ब", "ब्",  "भ", "भ्",  "म",  "म", "म्",  
    "य", "य्",  "र", "ल", "ल", "ल्",  "ळ",  "व", "व", "व्",   
    "श", "श्",  "ष", "ष्", "स", "स", "स्", "ह", 
    
    "ीं", "्र",    
    "द्द", "ट्ट","ट्ठ","ड्ड","कृ","भ","्य","ड्ढ","झ्","क्र","त्त्","श","श्",
    
    "ॉ",  "ो",   "ौ",   "ा",   "ी",   "ु",   "ू",   "ृ",   "े",   "ै",
    "ं",   "ँ",   "ः",   "ॅ",  "ऽ", "ऽ", "ऽ", "ऽ", "्र",  "्", "?", "़",":",
    "‘",   "’",   "“",   "”",  ";",  "(",    ")",   "{",    "}",   "=", "।", ".", "-",  "µ", "॰", ",","् ","/"]
    
    array_one_length = len(array_one)
    
    # Specialty characters
    
    # Move "f"  to correct position and replace
    modified_substring = "  " + modified_substring + "  "
    position_of_f = modified_substring.rfind("f")
    while (position_of_f != -1):    
        modified_substring = modified_substring[:position_of_f] + modified_substring[position_of_f+1] + modified_substring[position_of_f] +  modified_substring[position_of_f+2:]
        position_of_f = modified_substring.rfind("f",0, position_of_f - 1 ) # search for f ahead of the current position.
    modified_substring = modified_substring.replace("f","ि")
    modified_substring = modified_substring.strip()
    
    # Move "half R"  to correct position and replace
    modified_substring = "  " + modified_substring + "  "
    position_of_r = modified_substring.find("Z")
    set_of_matras =  ["‚",    "ks",   "kS",   "k",     "h",    "q",   "w",   "`",    "s",    "S", "a",    "¡",    "%",     "W",   "·",   "~ ", "~"]
    while (position_of_r != -1):    
        modified_substring = modified_substring.replace("Z","",1)
        if modified_substring[position_of_r - 1] in set_of_matras:
            modified_substring = modified_substring[:position_of_r - 2] + "j~" + modified_substring[position_of_r - 2:]
        else:
            modified_substring = modified_substring[:position_of_r - 1] + "j~" + modified_substring[position_of_r - 1:]
        position_of_r = modified_substring.find("Z")
    modified_substring = modified_substring.strip()
    
    # Replace ASCII with Unicode
    for input_symbol_idx in range(0, array_one_length):
        modified_substring = modified_substring.replace(array_one[input_symbol_idx ] , array_two[input_symbol_idx] )
    
    
    return modified_substring

# Unicode to KrutiDev function
def Unicode_to_KrutiDev(unicode_substring):
    
    modified_substring = unicode_substring.encode('utf-8')
    
    array_one = ["‘",   "’",   "“",   "”",   "(",    ")",   "{",    "}",   "=", "।",  "?",  "-",  "µ", "॰", ",", ".", "् ", 
    "०",  "१",  "२",  "३",     "४",   "५",  "६",   "७",   "८",   "९", "x", 
    
    "फ़्",  "क़",  "ख़",  "ग़", "ज़्", "ज़",  "ड़",  "ढ़",   "फ़",  "य़",  "ऱ",  "ऩ",  
    "त्त्",   "त्त",     "क्त",  "दृ",  "कृ",
    
    "ह्न",  "ह्य",  "हृ",  "ह्म",  "ह्र",  "ह्",   "द्द",  "क्ष्", "क्ष", "त्र्", "त्र","ज्ञ",
    "छ्य",  "ट्य",  "ठ्य",  "ड्य",  "ढ्य", "द्य","द्व",
    "श्र",  "ट्र",    "ड्र",    "ढ्र",    "छ्र",   "क्र",  "फ्र",  "द्र",   "प्र",   "ग्र", "रु",  "रू",
    "्र",
    
    "ओ",  "औ",  "आ",   "अ",   "ई",   "इ",  "उ",   "ऊ",  "ऐ",  "ए", "ऋ",
    
    "क्",  "क",  "क्क",  "ख्",   "ख",    "ग्",   "ग",  "घ्",  "घ",    "ङ",
    "चै",   "च्",   "च",   "छ",  "ज्", "ज",   "झ्",  "झ",   "ञ",
    
    "ट्ट",   "ट्ठ",   "ट",   "ठ",   "ड्ड",   "ड्ढ",  "ड",   "ढ",  "ण्", "ण",  
    "त्",  "त",  "थ्", "थ",  "द्ध",  "द", "ध्", "ध",  "न्",  "न",  
    
    "प्",  "प",  "फ्", "फ",  "ब्",  "ब", "भ्",  "भ",  "म्",  "म",
    "य्",  "य",  "र",  "ल्", "ल",  "ळ",  "व्",  "व", 
    "श्", "श",  "ष्", "ष",  "स्",   "स",   "ह",     
    
    "ऑ",   "ॉ",  "ो",   "ौ",   "ा",   "ी",   "ु",   "ू",   "ृ",   "े",   "ै",
    "ं",   "ँ",   "ः",   "ॅ",    "ऽ",  "् ", "्" ]
    
    array_two = ["^", "*",  "Þ", "ß", "¼", "½", "¿", "À", "¾", "A", "\\", "&", "&", "Œ", "]","-","~ ", 
    "å",  "ƒ",  "„",   "…",   "†",   "‡",   "ˆ",   "‰",   "Š",   "‹","Û",
    
    "¶",   "d",    "[k",  "x",  "T",  "t",   "M+", "<+", "Q",  ";",    "j",   "u",
    "Ù",   "Ùk",   "Dr",    "–",   "—",       
    
    "à",   "á",    "â",   "ã",   "ºz",  "º",   "í", "{", "{k",  "«", "=","K", 
    "Nî",   "Vî",    "Bî",   "Mî",   "<î", "|","}",
    "J",   "Vª",   "Mª",  "<ªª",  "Nª",   "Ø",  "Ý",   "æ", "ç", "xz", "#", ":",
    "z",
    
    "vks",  "vkS",  "vk",    "v",   "bZ",  "b",  "m",  "Å",  ",s",  ",",   "_",
    
    "D",  "d",    "ô",     "[",     "[k",    "X",   "x",  "?",    "?k",   "³", 
    "pkS",  "P",    "p",  "N",   "T",    "t",   "÷",  ">",   "¥",
    
    "ê",      "ë",      "V",  "B",   "ì",       "ï",     "M",  "<",  ".", ".k",   
    "R",  "r",   "F", "Fk",  ")",    "n", "/",  "/k",  "U", "u",   
    
    "I",  "i",   "¶", "Q",   "C",  "c",  "H",  "Hk", "E",   "e",
    "¸",   ";",    "j",  "Y",   "y",  "G",  "O",  "o",
    "'", "'k",  "\"", "\"k", "L",   "l",   "g",      
    
    "v‚",    "‚",    "ks",   "kS",   "k",     "h",    "q",   "w",   "`",    "s",    "S",
    "a",    "¡",    "%",     "W",   "·",   "~ ", "~"]
    
    array_one_length = len(array_one)
    
    # Specialty characters
    modified_substring = modified_substring.replace ("क़", "क़")   
    modified_substring = modified_substring.replace ("ख़‌", "ख़")
    modified_substring = modified_substring.replace ("ग़", "ग़")
    modified_substring = modified_substring.replace ("ज़", "ज़")
    modified_substring = modified_substring.replace ("ड़", "ड़")
    modified_substring = modified_substring.replace ("ढ़", "ढ़")
    modified_substring = modified_substring.replace ("ऩ", "ऩ")
    modified_substring = modified_substring.replace ("फ़", "फ़")
    modified_substring = modified_substring.replace ("य़", "य़")
    modified_substring = modified_substring.replace ("ऱ", "ऱ")
    modified_substring = modified_substring.replace("ि","f")
    
    # Replace Unicode with ASCII
    for input_symbol_idx in range(0, array_one_length):
        modified_substring = modified_substring.replace(array_one[input_symbol_idx ] , array_two[input_symbol_idx] )
    
    # Move "f"  to correct position
    modified_substring = "  " + modified_substring + "  "
    position_of_f = modified_substring.find("f")
    while (position_of_f != -1):    
        modified_substring = modified_substring[:position_of_f-1] + modified_substring[position_of_f] + modified_substring[position_of_f-1] + modified_substring[position_of_f+1:]
        position_of_f = modified_substring.find("f", position_of_f +1 ) # search for f ahead of the current position.
    modified_substring = modified_substring.strip()
    
    # Move "half R"  to correct position and replace
    modified_substring = "  " + modified_substring + "  "
    position_of_r = modified_substring.find("j~")
    set_of_matras =  ["‚",    "ks",   "kS",   "k",     "h",    "q",   "w",   "`",    "s",    "S", "a",    "¡",    "%",     "W",   "·",   "~ ", "~"]
    while (position_of_r != -1):    
        modified_substring = modified_substring.replace("j~","",1)
        if modified_substring[position_of_r + 1] in set_of_matras:
            modified_substring = modified_substring[:position_of_r + 2] + "Z" + modified_substring[position_of_r + 2:]
        else:
            modified_substring = modified_substring[:position_of_r + 1] + "Z" + modified_substring[position_of_r + 1:]
        position_of_r = modified_substring.find("j~")
    modified_substring = modified_substring.strip()
    
    return modified_substring

# Read in Excel file
excel_file = pd.read_excel(folder+"/"+workbook+".xlsx", worksheet, index_col=None, keep_default_na=False, header=None)
excel_file.head()

# Define parameters
start_column_num = ord(start_column.upper()) - 65
end_column_num = ord(end_column.upper()) - 65
start_row_num = start_row - 1
end_row_num = end_row - 1
function_dict = {"Unicode":KrutiDev_to_Unicode, "KrutiDev":Unicode_to_KrutiDev}
function = function_dict[convert_to]

# Loop through columns
for col in range(start_column_num, end_column_num + 1):
    
    # Create new column with same values
    col_name = str(col) + "_NEW" 
    excel_file[col_name] = excel_file[col]
    
    # Replace with transformed values in selected rows
    # for row in range(start_row_num, end_row_num + 1):
    #     excel_file.ix[row, col_name] = function(excel_file.ix[row, col])

file_name = folder+u"\TRANSFORMED "+workbook+".xlsx"
excel_file.to_excel(file_name,sheet_name=worksheet, engine="xlsxwriter", encoding='utf-8', index=False, header=False)