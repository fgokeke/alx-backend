#!/usr/bin/yarn dev
import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Promisify Redis GET method
const asyncGet = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await asyncGet(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
