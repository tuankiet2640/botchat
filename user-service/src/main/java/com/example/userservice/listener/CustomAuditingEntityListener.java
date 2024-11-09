package com.example.userservice.listener;

import com.example.userservice.entity.AbstractAuditEntity;
import jakarta.persistence.PrePersist;
import jakarta.persistence.PreUpdate;
import org.springframework.beans.factory.ObjectFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Configurable;
import org.springframework.data.auditing.AuditingHandler;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

@Configurable
public class CustomAuditingEntityListener extends AuditingEntityListener {

    public CustomAuditingEntityListener() {
        super();
    }

    @Autowired
    public void setAuditingHandler(ObjectFactory<AuditingHandler> handler) {
        super.setAuditingHandler(handler);
    }
    public CustomAuditingEntityListener(ObjectFactory<AuditingHandler> handler) {
        super.setAuditingHandler(handler);
    }


}