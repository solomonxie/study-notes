# Project: Convert scanned PDF to Word with LAYOUTS

The most tricky part is maintaining the layouts, and that's the core technique of this whole thing, which is not well implemented at current tech world.

I have a very different logic for doing this:
- [x] Treat the scanned document as an image with PDFImages & ImageMagick
- [ ] Use OpenCV to make the document's direction straight
- [x] Use Cloud OCR to detect all text and **POSITIONS** of each letter
- [ ] Carve out all text from the image by the text's position (coordinates of a box), and left with an image without text
- [ ] Detect all **straight lines** and mark each line's position(head to tip) with OpenCV
- [ ] Recognize tables or headers/footers from the straight lines
- [ ] Carve out all straight lines
- [ ] Treat all the left parts(wether curves or colors or dots) as the background image of the document.
- [ ] Analyze all the relationships between the detected texts and tables/header/footer or just normal content.
- [ ] Start to create a Word document
- [ ] Set up the sizes of header/footer and page
- [ ] Create tables according to the detected information(size/rows/columns/)
- [ ] Put texts back in to their place 

