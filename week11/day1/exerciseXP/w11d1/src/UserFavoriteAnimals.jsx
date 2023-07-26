//function component

const UserFavoriteAnimals = (props) => {
    //console.log(props);
    
    return (
        //props - object of {favAnimals: 'value'}
            <li>{props.favAnimals}</li>
    );
};

export default UserFavoriteAnimals;