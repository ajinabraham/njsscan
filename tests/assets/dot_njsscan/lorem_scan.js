import { LoremIpsum } from "lorem-ipsum";
// const LoremIpsum = require("lorem-ipsum").LoremIpsum;

const lorem = new LoremIpsum({
    sentencesPerParagraph: {
        max: 8,
        min: 4
    },
    wordsPerSentence: {
        max: 16,
        min: 4
    }
});
let decipher = crypto.createDecipheriv('aes-128-ecb', Buffer.from(ENCRYPTION_KEY), iv);
lorem.generateWords(1);
lorem.generateSentences(5);
lorem.generateParagraphs(7);
