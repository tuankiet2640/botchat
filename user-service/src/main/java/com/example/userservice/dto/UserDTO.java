package com.example.userservice.dto;

import com.example.userservice.entity.User;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.modelmapper.ModelMapper;

import java.time.Instant;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class UserDTO {
    private UUID id;

    @NotBlank(message = "Username is required")
    private String username;

    @NotBlank(message = "First name is required")
    private String firstName;

    @NotBlank(message = "Last name is required")
    private String lastName;

    @Email(message = "Please provide a valid email address")
    @NotBlank(message = "Email is required")
    private String email;

    private Instant createdDate;
    private Instant lastModifiedDate;

    // Convert Entity to DTO
    public static UserDTO fromEntity(User user, ModelMapper mapper) {
        return mapper.map(user, UserDTO.class);
    }

    // Convert DTO to Entity
    public User toEntity(ModelMapper mapper) {
        return mapper.map(this, User.class);
    }

    // Convert List of entities to DTOs
    public static List<UserDTO> fromEntities(List<User> users, ModelMapper mapper) {
        return users.stream()
                .map(user -> fromEntity(user, mapper))
                .collect(Collectors.toList());
    }
}