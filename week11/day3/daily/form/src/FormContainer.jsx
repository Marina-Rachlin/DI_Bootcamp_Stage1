import {useState} from "react";
import FormComponent from "./FormComponent";

const FormContainer = () =>{
    const [userInfo, setUserInfo] = useState({
      firstName: "",
      lastName: "",
        age: "",
        gender: "",
        destination: "Please choose the destination", 
        nutsFree: false,
        lactoseFree: false,
        isVegan: false
})

const handleChange = (event) => {
    const { name, value, type, checked} = event.target;

    type === "checkbox"
      ? setUserInfo(prevValue => ({...prevValue,[name]: checked}))
      : setUserInfo(prevValue => ({...prevValue,[name]: value}));
  }

    return(
       <FormComponent handleChange={handleChange} {...userInfo} />
    );
}

export default FormContainer;
