import gpt_2_simple as gpt2
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Generate(Resource):
    def get(self, length, temp, samples):

        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(sess,
                       run_name='PieBoy'
                       )

        text = gpt2.generate(sess,
                             length=length,
                             run_name='PieBoy',
                             temperature=temp,
                             include_prefix=False,
                             nsamples=samples,
                             batch_size=samples,
                             return_as_list=True
                             )
        result = {'data': text}
        return(jsonify(result))

api.add_resource(Generate, '/generate/<int:length>&<float:temp>&<int:samples>')

if __name__ == '__main__':
    app.run(port='8080')