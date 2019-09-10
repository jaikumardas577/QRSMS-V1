var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry:{
 WEBPACT_initial: './src/index.js'

},

output: {
      path: path.resolve('./webpack_output/static/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.css$/,
        use: [{ loader: "style-loader" }, 
        { loader: "css-loader" },
       
       ],
      },
      { test: /\.svg$/, loader: 'svg-inline-loader' }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }

};