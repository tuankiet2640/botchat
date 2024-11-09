package com.example.userservice.service.impl;

import com.example.userservice.dto.UserDTO;
import com.example.userservice.entity.User;
import com.example.userservice.exception.ResourceNotFoundException;
import com.example.userservice.repository.UserRepository;
import com.example.userservice.service.UserService;
import lombok.RequiredArgsConstructor;
import org.modelmapper.ModelMapper;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    //inject through constroctor injection
    private final UserRepository userRepository;
    private final ModelMapper modelMapper;


    @Override
    public String hello() {
        return "Hello from UserService";
    }

    public UserDTO createUser(UserDTO userDTO) {
        User user = userDTO.toEntity(modelMapper);
        User savedUser = userRepository.save(user);
        return UserDTO.fromEntity(savedUser, modelMapper);
    }

    public UserDTO getUserById(UUID id) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        return UserDTO.fromEntity(user, modelMapper);
    }

    @Override
    public UserDTO getUserByUsername(String username) {
        return null;
    }

    @Override
    public UserDTO getUserByEmail(String email) {
        return null;
    }

    public List<UserDTO> getAllUsers() {
        List<User> users = userRepository.findAll();
        return UserDTO.fromEntities(users, modelMapper);
    }

    @Override
    public Page<UserDTO> getAllUsersPaged(Pageable pageable) {
        return null;
    }

    public UserDTO updateUser(UUID id, UserDTO userDTO) {
        User existingUser = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));

        modelMapper.map(userDTO, existingUser);
        existingUser.setId(id); // Ensure ID doesn't get overwritten

        User updatedUser = userRepository.save(existingUser);
        return UserDTO.fromEntity(updatedUser, modelMapper);
    }

    @Override
    public UserDTO updatePartialUser(UUID id, UserDTO userDTO) {
        return null;
    }

    @Override
    public void deleteUser(UUID id) {

    }

    @Override
    public boolean existsByUsername(String username) {
        return false;
    }

    @Override
    public boolean existsByEmail(String email) {
        return false;
    }


}
