# _*_ codinf:utf-8 _*_

'''
创建时间：2020-10-14
文件说明：打印机纸张设置
'''
import win32con

paperdict = {
	"DMPAPER_LETTER": win32con.DMPAPER_LETTER,                               # letter， 8 1/2×1 英寸
	# "MPAPER_LEGAL": win32con.MPAPER_LEGAL,                                 # Legal， 8 1/2×14 英寸  
	"DMPAPER_A4": win32con.DMPAPER_A4,                                       # A4 letter， 210×297 毫米
	"DMPAPER_CSHEET": win32con.DMPAPER_CSHEET,                               # C letter， 17×22 英寸
	"DMPAPER_DSHEET": win32con.DMPAPER_DSHEET,                               # D letter， 22×34 英寸
	"DMPAPER_ESHEET": win32con.DMPAPER_ESHEET,                               # E letter， 34×44 英寸
	"DMPAPER_LETTERSMALL": win32con.DMPAPER_LETTERSMALL,                     # letter small， 8 1/2×11 英寸
	"DMPAPER_TABLOID": win32con.DMPAPER_TABLOID,                             # Tabloid， 11×17 英寸
	"DMPAPER_LEDGER": win32con.DMPAPER_LEDGER,                               # Ledger， 17×11 英寸
	"DMPAPER_STATEMENT": win32con.DMPAPER_STATEMENT,                         # Statement， 5 1/2×8 1/2 英寸
	"DMPAPER_EXECUTIVE": win32con.DMPAPER_EXECUTIVE,                         # Executive， 7 1/4×10 1/2 英寸
	"DMPAPER_A3": win32con.DMPAPER_A3,                                       # A3 Sheet， 297×420 毫米
	"DMPAPER_A4SMALL": win32con.DMPAPER_A4SMALL,                             # A4 Small Sheet， 210×297 毫米
	"DMPAPER_A5": win32con.DMPAPER_A5,                                       # A5 Sheet， 148×210 毫米
	"DMPAPER_B4": win32con.DMPAPER_B4,                                       # B4 Sheet， 250×354 毫米
	"DMPAPER_B5": win32con.DMPAPER_B5,                                       # B5 Sheet， 182×257 毫米
	"DMPAPER_FOLIO": win32con.DMPAPER_FOLIO,                                 # Folio, 8 1/2×13 英寸
	"DMPAPER_QUARTO": win32con.DMPAPER_QUARTO,                               # Quarto, 215×275 毫米
	"DMPAPER_10X14": win32con.DMPAPER_10X14,                                 # 10×14 英寸
	"DMPAPER_11X17": win32con.DMPAPER_11X17,                                 # 11×17 英寸
	"DMPAPER_NOTE": win32con.DMPAPER_NOTE,                                   # Note, 8 1/2×11 英寸
	"DMPAPER_ENV_9": win32con.DMPAPER_ENV_9,                                 # #9 EnVelope， 3 7/8×8 7/8 英寸
	"DMPAPER_ENV_10": win32con.DMPAPER_ENV_10,                               # #10 EnVelope， 4 1/8×9 1/2 英寸
	"DMPAPER_ENV_11": win32con.DMPAPER_ENV_11,                               # #11 EnVelope， 4 1/2×10 3/8 英寸
	"DMPAPER_ENV_12": win32con.DMPAPER_ENV_12,                               # #12 EnVelope， 4 3/4×11 英寸
	"DMPAPER_ENV_14": win32con.DMPAPER_ENV_14,                               # #14 EnVelope， 5×11 1/2 英寸
	"DMPAPER_ENV_DL": win32con.DMPAPER_ENV_DL,                               # DL EnVelope， 110×220 毫米
	"DMPAPER_ENV_C5": win32con.DMPAPER_ENV_C5,                               # C5 EnVelope， 162×229 毫米
	"DMPAPER_ENV_C3": win32con.DMPAPER_ENV_C3,                               # C3 EnVelope， 324×458 毫米
	"DMPAPER_ENV_C4": win32con.DMPAPER_ENV_C4,                               # C4 EnVelope， 229×324 毫米
	"DMPAPER_ENV_C6": win32con.DMPAPER_ENV_C6,                               # C6 EnVelope， 114×162 毫米
	"DMPAPER_ENV_C65": win32con.DMPAPER_ENV_C65,                             # C65 EnVelope， 114×229 毫米
	"DMPAPER_ENV_B4": win32con.DMPAPER_ENV_B4,                               # B4 EnVelope， 250×353 毫米
	"DMPAPER_ENV_B5": win32con.DMPAPER_ENV_B5,                               # B5 EnVelope， 176×250 毫米
	"DMPAPER_ENV_B6": win32con.DMPAPER_ENV_B6,                               # B6 EnVelope， 176×125 毫米
	"DMPAPER_ENV_ITALY": win32con.DMPAPER_ENV_ITALY,                         # Italy EnVelope， 110×230 毫米
	"DMPAPER_ENV_MONARCH": win32con.DMPAPER_ENV_MONARCH,                     # Monarch EnVelope， 3 7/8×7 1/2 英寸
	"DMPAPER_ENV_PERSONAL": win32con.DMPAPER_ENV_PERSONAL,                   # 6 3/4 EnVelope， 3 5/8×6 1/2 英寸
	"DMPAPER_FANFOLD_US": win32con.DMPAPER_FANFOLD_US,                       # US Std Fanfold, 14 7/8×11 英寸
	"DMPAPER_FANFOLD_STD_GERMAN": win32con.DMPAPER_FANFOLD_STD_GERMAN,       # German Std Fanfold, 8 1/2×12 英寸
	"DMPAPER_FANFOLD_LGL_GERMAN": win32con.DMPAPER_FANFOLD_LGL_GERMAN,       # German Legal Fanfold, 8 1/2×13 英寸
}