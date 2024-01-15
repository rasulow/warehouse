const is_have = ()=>{  
    return !!localStorage.getItem("token");
}

export default is_have;