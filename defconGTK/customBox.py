from gi.repository import Gtk, Gdk

#Making the Page Heading
class PageHeading(Gtk.Alignment):

    def __init__(self, heading="", fontSize = '40000'):
        
        super(PageHeading, self).__init__(xalign=0,
                              yalign=0.5,
                              xscale=0,
                              yscale=0)
    
        #Making the Page Heading
        self.headingBox = Gtk.Box()

        HEADING_STRING = "<span foreground='black' size='" + fontSize + "' font='Cantarell' font_weight='bold'>" + heading + "</span>"

        self.pageHeading = Gtk.Label()
        self.pageHeading.set_markup(HEADING_STRING)
        self.headingBox.add(self.pageHeading)
        self.add(self.headingBox)

class DisplayData(Gtk.Alignment):

    def __init__(self, heading = None, text = None, headingSize = '15000', textSize = '10000'):
        super(DisplayData, self).__init__(xalign=0,
                              yalign=0.5,
                              xscale=0,
                              yscale=0)
        
        self.box = Gtk.VBox()

        if heading is None:
            self.heading = ''
        else:
            self.heading = heading

        if text is None:
            self.text = ''
        else:
            self.text = text

        HEADING_STRING = "<span foreground='black' size='" + headingSize + "' font='Cantarell' font_weight='bold'>" + self.heading + "</span>"
        TEXT_STRING = "<span foreground='black' size='" + textSize + "' font='Cantarell'>" + self.text + "</span>"
        
        self.headingLable = Gtk.Label()
        self.headingLable.set_markup(HEADING_STRING)
        self.headingLable.set_alignment(0, 0.5)

        self.textLable = Gtk.Label()
        self.textLable.set_markup(TEXT_STRING)
        self.textLable.set_alignment(0, 0.5)
        
        #buffer = Gtk.TextBuffer()
        #buffer.set_markup(TEXT_STRING) 
        #self.textView = Gtk.TextView(buffer)

        self.box.pack_start(self.headingLable, False, False, 5)
        self.box.pack_start(self.textLable, False, False, 5)
        self.add(self.box)
        self.show_all()

#Making a font info box
class FontInfoBox(Gtk.VBox):
    """
    Add all the info that needs to be displayed for the current selected font
    """
    def __init__(self, font):
        super(FontInfoBox, self).__init__()
        
        #Specify the info to be displayed
        fontName = DisplayData("Name", font.info.familyName)
        self.pack_start(fontName, False, False, 5)

        fontVersion = DisplayData("Version", str(font.info.versionMajor) + "." +  str(font.info.versionMinor))
        self.pack_start(fontVersion, False, False, 5)

        fontTrademark = DisplayData("Trademark", font.info.trademark)
        self.pack_start(fontTrademark, False, False, 5)


