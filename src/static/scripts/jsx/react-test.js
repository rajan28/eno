var React = require('react');
var ReactDOM = require('react-dom');
var createReactClass = require('create-react-class');

var test = createReactClass({
	render: function() {
	  return (<h2>This is React!</h2>);
	}
});

ReactDOM.render(
	React.createElement(test, null),
	document.getElementById('content')
);