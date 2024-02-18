#!/usr/bin/node
// the api integration
// const { get } = require("https");
const request = require("request")

const STAR_WAR_API = "https://swapi-api.alx-tools.com/api/films/";


const getMovieCharacters = (movieId)=>{
    const url = `https://swapi.dev/api/films/${movieId}/`;
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (!error && response.statusCode == 200){
                const movie = JSON.parse(body);
                resolve(movie.characters);
            }
        })
    })
}
const printMovieCharacters = async (movieId)=>{
    try {
        const characters = await getMovieCharacters(movieId);
        // console.log()
        if (!Array.isArray(characters) ) {
            return;
        }
        characters.forEach(async (characterUrl) => {
            const character = await getCharacterName(characterUrl);
            if (character !== undefined && character !== ''){
                console.log(character);
            }
        });
    } catch (error) {
        console.error('Error feftching ovie characters:', error);
    }
}

const getCharacterName = (characterUrl)=>{
    return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body)=>{
            if (!error && response.statusCode == 200){
                const character = JSON.parse(body);
                resolve(character.name);
            }
        });
    });
}


let movieId = process.argv[2];

if (!movieId){
    console.error('Please provide a movie ID as the first argument');
}else{
    printMovieCharacters(movieId);
}
