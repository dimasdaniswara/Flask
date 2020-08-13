import flask
import numpy as np
import pickle

model = pickle.load(open('model/model_classifier.pkl', 'rb'))
app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in flask.request.form.values()] #[90,80,80,80]
    final_features = [np.array(int_features)] #[[90,80,80,80]]
    prediction = model.predict(final_features) #model.predict([[90,80,80,80]])

    output = {0: 'not placed', 1: 'placed'}

    return flask.render_template('main.html', prediction_text='Student must be {} to workplace'.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run(debug=True)