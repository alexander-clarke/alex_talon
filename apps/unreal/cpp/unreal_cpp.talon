code.language: c
code.language: cpp
-

state you property:
  insert("UPROPERTY(BlueprintReadWrite, EditAnywhere)")

state you property <user.uproperty_specifiers>:
  user.insert_between("UPROPERTY({uproperty_specifiers}", ")")

insert you property <user.uproperty_specifiers>:
  user.smart_insert_specifiers(uproperty_specifiers)

state read only you property:
  insert("UPROPERTY(BlueprintReadOnly, VisibleAnywhere)")

state you function <user.ufunction_specifiers>:
  user.insert_between("UFUNCTION({ufunction_specifiers}", ")")
  
insert you function [specifier] <user.ufunction_specifiers>:
  user.smart_insert_specifiers(ufunction_specifiers)

state log:
  user.insert_between("UE_LOG(LogTemp, ", ")")