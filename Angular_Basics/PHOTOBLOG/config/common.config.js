const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const extractCSS = new ExtractTextPlugin('[name].css');

const ROOT = path.resolve(__dirname, '..');

function root(pathParts) {
  if (typeof pathParts === 'string') {
    pathParts = pathParts.split('/');
  }
  return path.join.apply(path, [ROOT, ...pathParts]);
}

const context = root('src');

module.exports = {
    context,
    entry: {
        polyfills: './polyfills.ts',
        vendor: './vendor.ts',
        app: './main.ts'
    },

    output: {
        path: root('wwwroot'),
        publicPath: '/',
        filename: '[name].[hash].js',
        chunkFilename: '[id].[hash].chunk.js'
    },

    resolve: {
        extensions: ['', '.ts', '.js']
    },

    module: {
        loaders: [
            {
                test: /\.ts$/,
                loaders: ['awesome-typescript-loader?configFileName=' + root('src/tsconfig.json'), 'angular2-template-loader']
            },
            {
                test: /\.html$/,
                loader: 'html'
            },
            {
                test: /\.(png|jpe?g|gif|svg|woff|woff2|ttf|eot|ico)$/,
                loader: 'file?name=/assets/[name].[hash].[ext]'
            },
            {
                test: /\.css$/,
                exclude: root('src'),
                loader: ExtractTextPlugin.extract('style', 'css?sourceMap')
            },
            {
                test: /\.css$/,
                include: root('src'),
                loader: 'raw'
            },
            {
                test: /\.css$/,
                include: root('src/styles'),
                loader: extractCSS.extract(['css'])
            }
        ]
    },

    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: ['app', 'vendor', 'polyfills']
        }),

        new HtmlWebpackPlugin({
            template: 'index.html'
        }),

        extractCSS
    ]
};