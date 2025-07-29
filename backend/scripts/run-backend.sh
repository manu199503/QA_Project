#!/bin/bash

echo "Starting Backend..."
cd backend || exit
npm install
npm run server
