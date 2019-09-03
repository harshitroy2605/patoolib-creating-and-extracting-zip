import patoolib

#patoolib.create_archive("test.zip",("1.pdf","1.pptx"))

patoolib.extract_archive("test.zip",outdir="extract")