const webpack = require('webpack');
const config = {
    entry:  __dirname + '/backend/static/source/index.js',
    output: {
        path: __dirname + '/backend/static/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css', '.scss']
    },

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            '@babel/preset-env',
                            ['@babel/preset-react', {"runtime": "automatic"}]
                        ]
                    }
                }
            },
            {
                test: /\.(css|scss)$/,
                use: [
                    'style-loader', 
                    'css-loader',
                ]
            },
        ]
    }
};
module.exports = config;
