function tasty(number, recipe) {
	const units = {
		
	};

	const newRecipe = {};
	for (key in recipe) {
		newRecipe[recipe[key]] = {
			recipe[key][0] * number, recipe[key][1]
		};
	}
	return newRecipe;
}

const recipe = {
	'mayonnaise': [2, 'c'],
	'brown sugar': [8, 't'],
	'cayenne': [2, 't']
};

console.log(tasty(2, recipe));

/*
{
	'mayonnaise': [1, 'q'],
	'brown sugar': [1, 'c'],
	'cayenne': [1.33, 'T']
}
*/
