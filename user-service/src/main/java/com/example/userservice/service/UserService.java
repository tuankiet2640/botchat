package com.example.userservice.service;


import com.example.userservice.dto.UserDTO;
import com.example.userservice.entity.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;
import java.util.UUID;

//create an interface UserService
public interface UserService {

    //create a method that returns a string
    String hello();

    // Create operations
    UserDTO createUser(UserDTO userDTO);

    // Read operations
    UserDTO getUserById(UUID id);

    UserDTO getUserByUsername(String username);

    UserDTO getUserByEmail(String email);

    List<UserDTO> getAllUsers();

    Page<UserDTO> getAllUsersPaged(Pageable pageable);

    // Update operations
    UserDTO updateUser(UUID id, UserDTO userDTO);

    UserDTO updatePartialUser(UUID id, UserDTO userDTO);  // for PATCH operations

    // Delete operations
    void deleteUser(UUID id);

    // Check operations
    boolean existsByUsername(String username);

    boolean existsByEmail(String email);
}

