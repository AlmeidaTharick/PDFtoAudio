import pyttsx3 as p3 # text to speech in python.
import PyPDF2 as pdf #PDF reader 

#read the pdf file
#'rb' read in binary mode
#'strict = false' helps with error handling in the pdf reading
#para utilizar, basta colocar o path da file que deseja transformar em áudio book.
pdf_file = open(r"***PDF FILE PATH YOU WANT TO READ***", 'rb')
reader = pdf.PdfFileReader(pdf_file, strict = False)

#Count the number of pages in our chosen document
number_of_pages = reader.getNumPages()

#init function to begin engine instance
#iterate for loop over selected pdf pages

engine = p3.init()
for i in range (0,1):
    #read the pdf page
    page = reader.getPage(i)

    #extract the text from the PDF page
    page_content = page.extractText()

    #set the audio speed and volume

    newrate = 200
    engine.setProperty('rate', newrate)
    newvolume = 200
    engine.setProperty('volume', newvolume)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # 1 is female 0 is male

    engine.save_to_file(page_content, 'pdf_audio.mp3')
    engine.runAndWait()
    engine.stop()







#ex:
#engine = pyttsx3.init()

#text = "This is really going to help me to consume my data analysis literature efficiently."

#engine.say(text)


#engine.runAndWait() #Plays the audio