package com.example.userservice.service;


import com.example.userservice.dto.UserDTO;
import com.example.userservice.entity.User;

import java.util.List;

//create an interface UserService
public interface UserService {

    //create a method that returns a string
    String hello();

    //get users method that returns a list of users
    List<UserDTO> getUsers();
}
