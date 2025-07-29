#!/bin/bash

echo "Starting Frontend..."
cd frontend || exit
npm install
npm run dev
