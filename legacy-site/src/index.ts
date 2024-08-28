import Vue from 'vue'

function greet(name: string)
{
    return `Hello, ${name}`;
}

const message = greet('World');
console.log(message);