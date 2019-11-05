from flask import jsonify

def bad_request():
  return jsonify({
    'success': False,
    'data': {},
    'messages': 'Bad request',
    'code': 400
  }), 400

def not_found():
  return jsonify(
    {
      'success': False,
      'data': {},
      'message': 'Resource not found',
      'code': 404
    }
  ), 404

def response(data):
    return jsonify(
      {
        'success': True,
        'data': data
      }  
    ), 200