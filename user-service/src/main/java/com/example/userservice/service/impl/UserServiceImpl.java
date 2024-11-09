package com.example.userservice.service.impl;

import com.example.userservice.dto.UserDTO;
import com.example.userservice.repository.UserRepository;
import com.example.userservice.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    //inject through constroctor injection
    private final UserRepository userRepository;



    @Override
    public String hello() {
        return "Hello from UserService";
    }

    @Override
    public List<UserDTO> getUsers() {
        return null;
    }
}
