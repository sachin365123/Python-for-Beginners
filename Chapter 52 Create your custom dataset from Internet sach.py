from simple_image_download import simple_image_download as simpl
response = simpl.simple_image_download
keywords=['Sachin']
for kw in keywords:
  response().download(kw,10)
# response().download(keywords, limit) -> downloads images to new directory
