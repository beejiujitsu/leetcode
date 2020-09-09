function removeVowels(S: string): string {
    let vowels = /[aeiou]+/gi;
    let no_vowels = S.replace(vowels, "");
    return no_vowels;
};
