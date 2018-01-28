import locale
from dialog import Dialog

locale.setlocale(locale.LC_ALL, '')


d = Dialog(dialog="dialog")

d. set_background_title("My little")

if d.yesno("ajsdfks ") == d.OK:
	d.msgbox("adfsdf")
