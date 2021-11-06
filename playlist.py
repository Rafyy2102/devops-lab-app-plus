from flask import Flask, request, render_template, json

playlist = Flask(__name__)

data = {}
data['playlist'] = []

@playlist.route('/')
def my_index():
    return render_template('index.html')

@playlist.route('/form', methods=['GET', 'POST'])
def func_form():
    if request.method == "POST":
       music = request.form["music"]
       singer = request.form["singer"]
       processed_music = music.upper()
       processed_singer = singer.upper()
       data['playlist'].append({'musica': processed_music, 'cantor': processed_singer})

       with open('playlist.data', 'a') as fileObject:
           fileObject.write(str(f'{processed_music},{processed_singer}\n'))
           fileObject.close()
       jsonFile = open('playlist.json', 'w')
       with open('playlist.json', 'w') as fileObject:
           json.dump(data, fileObject)
    return render_template('form.html')

@playlist.route('/read', methods=['GET'])
def func_read():
    fileObject = open('playlist.json', 'r')
    fileContent = fileObject.read()
    fileObject.close()
    return render_template('read.html', fileContent=fileContent)

if __name__ == '__main__':
    playlist.run(debug=True)
