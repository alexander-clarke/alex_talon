code.language: c
code.language: cpp
-

state you prop:
    insert("UPROPERTY(BlueprintReadWrite, EditAnywhere)")

state you (property | prop) <user.uproperty_specifiers>:
    user.insert_between("UPROPERTY({uproperty_specifiers}", ")")

insert [you] (property | prop) <user.uproperty_specifiers>:
    user.smart_insert_specifiers(uproperty_specifiers)

state you (function | funk) [<user.ufunction_specifiers>]:
    user.insert_between("UFUNCTION({ufunction_specifiers or ''}", ")")

insert [you] (function | funk) [specifier] <user.ufunction_specifiers>:
    user.smart_insert_specifiers(ufunction_specifiers)

state log [{user.unreal_log_verbosity}]:
    user.insert_between('UE_LOG(LogTemp, {unreal_log_verbosity or "Display"}, TEXT("', '"));')

declare log category:
    user.insert_between("DECLARE_LOG_CATEGORY_EXTERN(Log", ", Log, All")

declare [{user.unreal_delegate_dynamic}] [{user.unreal_delegate_multicast}] delegate [{user.unreal_delegate_param_count} [(parameters | param)]]:
    insert("DECLARE")
    insert(unreal_delegate_dynamic or '')
    insert(unreal_delegate_multicast or '')
    insert("_DELEGATE")
    insert(unreal_delegate_param_count or '')
    user.insert_between("(F", ");")

{user.ue_types}: "{ue_types}"
